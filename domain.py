from urllib.parse import urlparse

#this file is to get the domain name of the url

def extractDomainName(url):
    try:
        # split by period
        # e.g. www.google.com
        result = extractSubDomainName(url).split('.')
        # return google + . + com
        return result[-2] + '.' + result[-1]
    except:
        return ""


def extractSubDomainName(url):
    try:
        return urlparse(url).netloc # network location
    except:
        return "" # failed