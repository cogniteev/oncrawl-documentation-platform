import json, requests

token = 'TOKEN'
crawl_id = 'CRAWL-ID'
url = 'https://app.oncrawl.com/api/crawls/{}/url-explorer'.format(crawl_id)
resp = requests.get(url, headers={'x-oncrawl-token': token},
                    params=dict(base_filters='crawled_pages'))
print json.dumps(resp.json(), indent=2, sort_keys=True)
