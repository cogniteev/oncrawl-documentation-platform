---
title: Aggregation Guide
tags: [guide]
keywords: guide aggregation
last_update: October, 27, 2016
summary: "Learn how to consolidate your crawl's data."
sidebar: mydoc_sidebar
permalink: guide_aggregation
folder: guides
fa_icon: fa-bar-chart
complexity: 4
toc: false
---

## Rationale

A crawl aggregation allows you to build an analytic information over a set
of metrics extracted during a crawl of a site. It provides aggregated
data based on a search query.

## Making Requests

The `GET` and `POST` method of request `/api/crawls/{crawl_id}/aggs` allows
you to perform. It is designed to perform several aggregation in one single
call.

An aggregation query is formed by:

* One or more filters. Each filter selects a set of page and restrict
  the scope on which the aggregation is performed. If more than one filter
  is given, then the final scope of pages is the conjunction of all filters.
  A list of available filters can be obtained at `api/{project_id}/quickfilters`

* Zero or more aggregation fields. Each aggregation stage distribute the pages
  according to their value of the aggregation fields. If more than one
  field is provided, pages are first distributed according to field1 values,
  called bucket. Then for each bucket of field1, pages are distributed
  according to their values of field2, and so on.

By default, the result of aggregations is the number of pages in each bucket.
But it is also possible to retrieve:

  * the sum of values of a field, for instance: `nb_inlinks:sum`

  * the average value of a field, for instance: `nb_inlinks:avg`

## Examples

### Count number of pages per page group

Create one bucket per *page group* and count the number of pages in each of
them.

```python
{% include snippets/v1/agg-pages-per-pg.py %}
```

Below the request JSON response:

```
{% include snippets/v1/agg-pages-per-pg.py.outputs %}
```

### Count number of pages per depth and page group

This is a demonstration of how to use multiple aggregation fields to arrange
the buckets.

```python
{% include snippets/v1/agg-pages-per-depth-pg.py %}
```

Below the request JSON response:

```
{% include snippets/v1/agg-pages-per-depth-pg.py.outputs %}
```

### Count the sum of inlinks per page group

This example show how to retrieve a field instead of a number of pages.

```python
{% include snippets/v1/agg-inlinks-per-pg.py %}
```

Below the request JSON response:

```
{% include snippets/v1/agg-inlinks-per-pg.py.outputs %}
```

## `GET` method

Because it is not always possible to perform a `POST` request, a `GET` version
if available. The bad news is that it is necessary to encode the JSON payload
in the URL. The aggregation request must be serialized in
<a href="https://github.com/Nanonid/rison" target="_blank">Rison format</a>.
More details about the supported parameters in the [API Reference](reference_api)
guide.
