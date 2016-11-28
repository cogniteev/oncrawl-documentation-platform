---
title: URL Explorer Guide
#tags: [guide]
keywords: guide url_explorer
last_update: October, 27, 2016
summary: "Describe how to look for URLs of your site."
sidebar: mydoc_sidebar
permalink: guide_url_explorer
folder: guides
fa_icon: fa-link
complexity: 3
---


## Rationale

The URL explorer returns information about pages matching your criteria,
and for each page returns the selected fields.

## Making Requests

URL explorer with a `GET` request at `/api/crawls/{crawl_id}/url-explorer`.

An URL explorer query is formed by:

* One or more filters. Each filter selects a set of page and restrict
  the scope of pages to return. If more than one filter
  is given, then the final scope of pages is the conjunction of all filters.
  A list of available filters can be obtained at `api/{project_id}/quickfilters`
  
* A comma separated list of fields to return for each page.
  The list of available fields depends on each crawl and can be obtained at
  `/api/crawls/{crawl_id}/querybuilder/fields`
  
* Pagination controls: number of items to return, offset in the list, sort order.

## Examples

### List of all crawl pages, with a default set of fields

### List of pages having near duplicate content issues, order by group
