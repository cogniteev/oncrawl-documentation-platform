---
title: Authentication Guide
tags: [guide]
keywords: guide authentication
last_update: October, 27, 2016
summary: "Describe how to perform authentication."
sidebar: mydoc_sidebar
permalink: guide_authentication
folder: guides
fa_icon: fa-vcard
complexity: 1
toc: false
---

## User Session Authentication

You can request API by being authenticated as a real OnCrawl user. You
first need to request `POST /api/session` to retrieve a session token
that will be valid during one week.

The Python code snippets below performs such authenticate and then list
the user's projects:

```python
{% include snippets/v1/user-session-authentication-quick.py %}
```

Below what the output of this program may be:

```
{% include snippets/v1/user-session-authentication.py.outputs %}
```

## User Session Token Reusability

A user session token a valid during one week. For your tests, you can for
instance store the token in a file to prevent authenticating over and over
again. Below is the same example than above, but with more class:

```python
{% include snippets/v1/user-session-authentication.py %}
```

## OAuth Token

Once you have obtained an OAuth token, it must be passed in the
`Authorization` header of your requests:


```
curl -H "Authorization: Bearer OAUTH-TOKEN https://app.oncrawl.com/api/projects"
```

or in Python:


```python
import requests
TOKEN = 'OAUTH-TOKEN'
# List projects
resp = requests.get('https://app.oncrawl.com/api/projects',
                    headers=dict(Authorization='Bearer ' + TOKEN)
for project in resp.json()['projects']:
    print '{id}: {start_url}'.format(**project)
```
