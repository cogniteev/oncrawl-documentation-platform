---
title: OAuth2
tags: [reference]
keywords: reference oauth2
last_update: October, 24, 2016
summary: "This describes the API OAuth2 authentication process."
sidebar: mydoc_sidebar
permalink: reference_oauth2
folder: reference
toc: false
---

OAuth2 is a protocol that lets external applications request authorization
to access private details in a user's OnCrawl account without the need to have
their password.

Developers need to register their application before getting started.
A registered OAuth application is assigned a unique ClientID and Client Secret.
The Client Secret should not be shared.

OnCrawl OAuth implementation supports the standard
[authorization code grant type](https://tools.ietf.org/html/rfc6749#section-4.1).
Developers may implement the web application flow as describe flow
in order to:

1. Obtain an authorization code
2. Exchange it for a token

## Web Application Flow

This is a description of the OAuth2 flow 3rf party web sites
may implement.

### 1. Redirect users to request OnCrawl access

```
GET https://app.oncrawl.com/oauth/authorize
```

Parameters

|Name|Type|Required|Description
|----|----|--------|----------|
|`client_id`|`string`|**yes**|The application client ID you received from OnCrawl|

### 2. OnCrawl redirects back to your site

If the user accepts your request to access its data, OnCrawl
redirects back to your site with a temporary code in a `code` parameter.

### 3. Exchange this code for an access token:

```
POST https://app.oncrawl.com/oauth/token
```

Parameters

|Name|Type|Required|Description
|`client_id`|`string`|**yes**|The client ID you received from OnCrawl when you created your application|
|`client_secret`|`string`|**yes**|The client secret you received from OnCrawl when you created your application|
|`code`|`string`|**yes**|The code you received as a response of Step 1|
|`grant_type`|`string`|**yes**|Must be `authorization_code`|
|`redirect_uri`|`string`|**yes**|Specify URL in your application where users will be sent after authorization|

Response

The response body contains a JSON payload providing the token.

```json
{
  "access_token": "gAWaGlVscCJhMR3kQQs184gn8bjB0g",
  "refresh_token": "86WkFa7TVOJ4vQOtl8jt7Ao3GJO7PR",
  "expires_in": 3600,
  "token_type": "Bearer",
  "scope": "account:read account:write"
}
```

### 4. Now use the access token to access the API

You can include the token in the `Authorization` header.

```
Authorization: Bearer OAUTH-TOKEN
```

For instance, with curl you can set the Authorization header like this:

```shell
curl -H "Authorization: Bearer OAUTH-TOKEN" https://app.github.com/projects
```


## Requested scopes vs. granted scopes

The `scope` attribute provides the list of scopes attached to the
token that were granted by the user. Normally, these scopes are the
the same that those you requested.
But future developments may allow OnCrawl users to edit
token scopes. You should be aware of this possibility and prepare
your application accordingly.

## OAuth Scopes


As of now, there are 4 different OAuth scopes available:

* `account:read`: provides capability to read user information
* `account:write`: provides capability to update user information
* `project:read`: provides capability to access:
  * configuration of projects, their configurations and crawls
  * perform queries and aggregation on crawls
* `project:write`: provides capability to update projects and related data
