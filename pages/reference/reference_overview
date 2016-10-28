---
title: Documentation Overview
tags: [getting_started]
keywords: reference overview
last_update: October, 24, 2016
summary: "Describes the API resources."
sidebar: mydoc_sidebar
permalink: reference_overview
folder: reference
toc: false
---

## Current Version

By default, all requests receive the latest version of the API. We encourage
you to explicitly request this version via the `Accept` header to prevent
any surprise when the OnCrawl API is updated in production.

```
Accept: application/vnd.oncrawl.v1
```

## Schema

All API access is over HTTPS, and accessed from the `https://app.oncrawl.com/api`.
Most data is sent and received as JSON. Aggregation API uses
[RISON](https://pypi.python.org/pypi/rison/1.1).

Timestamps are returned in milliseconds since EPOCH.

## Parameters

Many API methods take optional parameters. For GET requests, any parameters
not specified as a segment in the path can be passed as an HTTP query
string parameter.

{# FIXME add curl query when we release such call #}

for POST, PATCH, PUT, and DELETE requests, parameters not included in the URL
should be encoded as JSON with a **Content-Type** header of `application/json`.

## Client Errors

### Invalid request

Sending invalid JSON payload or request arguments will result in a `422 Unprocessable Entity`
response. Response body will provide in JSON the reason of the failure as follow:

```json
{
    "errors": {
        "FIELD-NAME": [
            "ERROR-DESCRIPTION-1",
            "ERROR-DESCRIPTION-2",
        ],
        "_other": [
            "ERROR-DESCRIPTION-3",
            "ERROR-DESCRIPTION-4",
        ]
    }
}
```

`_other` is a special field name when the request error is not due to the request
itself. For instance, if a user has consumed all its quota and is not able to
create another project, even if the request is valid, the request will result in a
`422 Unprocessable Entity` with the following JSON output:

```json
{
    "errors": {
        "_other":[
            "not enough remaining quota"
        ]
    }
}
```

### Unauthorized request

Accessing an unauthorized ressource or performing an unauthorized
operation will result in a `401 Unauthorized` with the following JSON output:

```json
{
    "errors": {
        "_other": [
            "unauthorized"
        ]
    }
}
```


## HTTP Verbs

When applicable, API tries to use appropriate HTTP verbs for each action.

| Verb | Description |
|------| ------ |
| GET | Retrieve ressources. |
| POST | Create ressources or trigger data computation. |
| PUT | Replace existing ressources.
| DELETE | Delete ressources. |

## Authentication

There are two ways to authenticate through OnCrawl API. Requests that require
authentication will return `401 Unauthorized`.

### Oauth2 Token sent in a header

```shell
curl -H "Authorization: Bearer OAUTH-TOKEN" https://app.github.com/projects
```

Read [more about OAuth2](reference_oauth2.html)

### User Session Token sent in a header

It is required to first login to generate an session token:

```shell
curl -X POST -H "Content-Type: application/json"
     -d '{"identification": "USERNAME-OR-EMAIL", "password": "USER-PASSWORD}' \
     https://app.oncrawl.com/session
```

The session token in sent in the request's JSON response:

```json
{
	"token": "SESSION-TOKEN",
	"username": "USERNAME",
	"user_id": "USER-ID",
	"user_hash": "USER-HASH"
}
```

The session token can then be passed via the `x-oncrawl-token` HTTP header:

```shell
curl -X POST \
     -H "Content-Type: application/json" \
     -H "x-oncrawl-token: SESSION-TOKEN" \
     https://app.oncrawl.com/session
```

### Check API health

You can request API to know if it is up and running.

```
curl https://app.oncrawl.com/api/is_alive
```

If it does not return a `200 OK` status code, then it means OnCrawl API service
is down.
