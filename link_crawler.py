# -*- coding: utf-8 -*-

import re
from urllib import parse
from url_download import download

def link_crawler(seed_url, link_regex):
  """Crawl from the given seed URL following links matched by link_regex
  """
  crawl_queue = [seed_url] # the queue of URL's to download
  seen = set(crawl_queue) # keep track which URL's have seen before
  while crawl_queue:
    url = crawl_queue.pop()
    html = download(url)
    if html:
      html = html.decode("utf-8")
    # filter for links matching our regular expression
    for link in get_links(html):
      if re.match(link_regex, link):
        # form absolute link
        link = parse.urljoin(seed_url, link)
        # check if have already seen this link
        if link not in seen:
          seen.add(link)
          crawl_queue.append(link)
          print(link)

def get_links(html):
  """Return a list of links from html
  """
  # a regular expression to extract all links from the webpage
  webpage_regex = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
  # list of all links from the webpage
  return webpage_regex.findall(html)

if __name__ == '__main__':
  link_crawler('http://example.webscraping.com', r'/places/default/(index|view)')
