---
title: Versions
keywords: version
tags:
last_update: October, 27, 2016
summary: "Provides information related to API updates or releases"
sidebar: mydoc_sidebar
permalink: versions
toc: false
---

### Currently supported versions

* version 1

### Versioning Policy

OnCrawl provides several versions of its API at a given point in time.
Content of an API version is not frozen though and changes may arises without
notice. To prevent breaking our customers code, changes within a given version
is limited to:

* adding new parameters to existing endpoint as long as
  the behaviour without those parameters remain the same.
* Add new endpoints
* Add new fields in endpoint's output. The last point is the most dangerous
  for our customers since some models libraries may break if schema
  changes.

Any other type of changes requires the API version to be bumped.

### API Deprecation

When a new API version is released, the previous latest version
is marked **deprecated**. One year later, the deprecated version is shutdown.
A deprecated API provides a `Deprecation` HTTP header in response
providing the date when the API will be shutdown, formatted in ISO-8601.

Consequently:

* API consumers must pay attention to this header to prevent
  any breaking API change.
* Once an API is declared deprecated, API consumers have one year to migrate
  their code the latest one.
