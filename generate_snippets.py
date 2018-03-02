#!/usr/bin/env python3
import urllib
import urllib.request
import pdb

from bs4 import BeautifulSoup


def get_page_soup(url):
    request = urllib.request.urlopen(url)

    if request.get_code() != 200:
        raise Exception("Request to {} returned {}.".format(
            url,
            request.get_code()
        ))

    html_doc = request.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    return soup


aws_docs = get_page_soup('https://www.terraform.io/docs/providers/aws/')
pdb.set_trace()