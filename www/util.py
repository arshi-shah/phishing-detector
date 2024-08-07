import re
import os
import pickle
import numpy as np
from tld import get_tld
from urllib.parse import urlparse

def abnormal_url(url):
    hostname = str(urlparse(url).hostname)
    match = re.search(hostname, url)
    return 0 if match else 1

def count_digit(url):
    digits = 0
    for i in url:
        if i.isnumeric(): digits = digits + 1
    return digits

def count_letter(url):
    letters = 0
    for i in url:
        if i.isalpha(): letters = letters + 1
    return letters

def is_https(url):
    return int(url.startswith("https://"))

def is_http(url):
    return int(url.startswith("http://"))

def count_dot(url):
    return url.count(".")

def count_www(url):
    return url.count("www")

def count_at(url):
    return url.count("@")

def count_dir(url):
    return urlparse(url).path.count("/")

def count_embed(url):
    return urlparse(url).path.count("//")

def count_percent(url):
    return url.count("%")

def count_ques(url):
    return url.count("?")

def count_dash(url):
    return url.count("-")

def count_equal(url):
    return url.count("=")

def url_length(url):
    return len(str(url))

def hostname_length(url):
    return len(urlparse(url).netloc)

def suspicious_words(url):
    match = re.search("PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr", url)
    return 1 if match else 0

# First Directory Length
def fd_length(url):
    urlpath = urlparse(url).path
    paths = urlpath.split("/")
    return len(paths[1]) if len(paths) > 1 else 0

def tld_length(url):
    domain = get_tld(url, fail_silently=True)
    return len(str(domain)) if domain else 0

def get_features(url):
    values = []
    for f in [abnormal_url, count_digit, count_letter, is_https, is_http, count_dot, count_www,
              count_at, count_dir, count_embed, count_percent, count_ques, count_dash, count_equal,
              url_length, hostname_length, suspicious_words, fd_length, tld_length]:
        values.append(f(url))
    return values

def get_prediction_from_url(url):
    model = pickle.load(open(os.path.join("..", "notebooks", "model"), "rb"))
    
    features_test = get_features(url)
    features_test = np.array(features_test).reshape((1, -1))
    pred = model.predict(features_test)
    return ["benign", "defacement", "phishing", "malware"][pred[0]]
