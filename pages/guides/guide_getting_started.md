---
title: Getting Started
tags: [guide, getting_started]
keywords: guide getting-started
last_update: October, 27, 2016
summary: "Help you get on track for using OnCrawl API."
sidebar: mydoc_sidebar
permalink: guide_getting_started
folder: guides
fa_icon: fa-linode
complexity: 0
toc: false
---

## 3rd Party Integration

If you want users of your service take benefits of their OnCrawl data within
your service, OnCrawl API supports OAuth2. But first you need to register
your application.

### Register your application

Despite every developer need to register their application before getting
started, as API is in beta state, registration is currently manual.

To do so, please send a mail to `{{ site.feedback_email }}` with subject
`[API] Application registration request` and provides us values for the fields
below:

```
User Name:
Application Name:
Application Description:
Image URL:
Default Scopes:
Redirect URLs:
Default Redirect URL:
```

Here is a description of the fields needed to create your application:

|Name|Type|Required|Description
|----|----|--------|-----------
|User Name|string|**yes**|Your OnCrawl username or email.|
|Application Name|string|**yes**|Something users will recognize.|
|Application Description|string|**yes**|Displayed to users when there are asked to share their data with you.|
|Application Logo URL|string|no|public URL to a picture of your application.|
|Default Scopes|string|no|Default [OAuth scopes](reference_oauth2#oauth-scopes) required by your application.|
|Redirect URLs|string|**yes**|Your application's callback URLs.|
|Default Redirect URL|string|**yes**|One of the redirect urls.|

We will then provides you a consumer key and consumer secret. Those keys are
required to perform an OAuth2 challenge to retrieve a session token, described
in the [OAuth2 page](reference_oauth2).

## Make request like an OnCrawl user

If it possible to authenticate using the username and password of OnCrawl users
to obtain a token that allows to request our API.

If you want to either tests our API or simply request your own data, this is
the simplest solution.

## Data Model

OnCrawl API allows to deal with objects and operations.

The top-level object is the *Project*. A *Project* is made of:

* Attributes: Name, Start URL, User agent, ...
* List of *Crawl Configurations*
* List of *Crawls*

A *CrawlConfiguration* is only made of attributes that belong to a *Crawl*.

A *Crawl* is made of attributes like the Crawl period, the *CrawlConfiguration*
that has been use. But the most important is its identifier, which allows you
to search for pages, or perform data aggregation.

More information about the available requests in the
[API Reference](reference_api).
