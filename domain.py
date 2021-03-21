## @file domain.py
#
# @brief this file contains the functions to extract the domain out of the urls
#
# @author Jodie
#
# @section libraries_main Libraries/Modules
# - urllib.parse standard library
#   - access to urlparse function

# Imports
from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
    """! This method extracts the domain name out of the url
    @param url website link
    @return domain name of the url
    """
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    """! This method extracts the sub domain name out of the url
    @param url website link
    @return sub domain name of the url
    """
    try:
        return urlparse(url).netloc
    except:
        return ''
