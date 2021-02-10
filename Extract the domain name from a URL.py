def domain_name(url):
    url = url.replace("http://", "").replace("www.", "").replace("https://", "").replace("bbs.", "").split(".")
    return url[0]


url = "hhhgoogle.co.jp"
print(domain_name(url))
