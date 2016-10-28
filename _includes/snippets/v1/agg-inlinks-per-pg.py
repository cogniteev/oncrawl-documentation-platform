import json, requests

token = 'TOKEN'
crawl_id = 'CRAWL-ID'
aggregation = {
  'aggs': [
    {
      'filters': 'all_pages',
      'fields': 'page_group',
      'value': 'nb_inlinks:sum'
    }
  ]
}
resp = requests.post('https://app.oncrawl.com/api/crawls/{}/aggs'.format(crawl_id),
                     headers={'x-oncrawl-token': token},
                     json=aggregation)
print json.dumps(resp.json(), indent=2)
