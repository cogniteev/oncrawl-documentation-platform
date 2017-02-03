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

OnCrawl API is still in beta. To register your application, please [fill the
form](https://docs.google.com/forms/d/e/1FAIpQLScCm9P2vSWTk0ZN1yTt9iyggizVdJ-T15C3-l_D1P4JJRZO_g/viewform?entry.602248975=My+OnCrawl+API+OAuth+application&entry.1442365639=seoguru&entry.816404965=My+app+allows+my+customer+to+access+OnCrawl+API's+data+through+my+customers+website&entry.1037603334=https://seo4ever.co/logo.png&entry.393669484=account:read&entry.393669484=project:read&entry.872577371=https://seo4ever.co/oauth_redirect&entry.481142999=https://seo4ever.co/oauth_redirect).

We will then provide you a consumer key and consumer secret. Those keys are
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
