from urllib.parse import urlparse

domains = [
    "https://github.com",
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
]


def domain(url):
    tmp = []
    for url in domains:
        tmp.append(urlparse(url).netloc)
    return tmp


print(domain(domains))
