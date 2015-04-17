import urllib,urllib2
import cookielib

def download_source(url,values,headers,cookie_jar):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'
    user_agent_headers = { 'User-Agent' : user_agent }
    headers = dict(user_agent_headers.items() + headers.items())
    data = urllib.urlencode(values)
    if cookie_jar == None:
        cookie_jar = cookielib.LWPCookieJar()
    cookie = urllib2.HTTPCookieProcessor(cookie_jar)

    opener = urllib2.build_opener(cookie) 

    req = urllib2.Request(url, data, headers)
    res = opener.open(req)

    html_doc = res.read()
    res.close()
    return (html_doc,cookie_jar)
