# -- coding:gbk --
import sys, time, os, re
import urllib, urllib2, cookielib

loginurl = 'https://www.douban.com/accounts/login'
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

params = {
"form_email":"27481991@qq.com",
"form_password":"skm7585999",
"source":"index_nav" #û�еĻ���¼���ɹ�
}

def post_group_topic(title,content):
    print '׼�����з���'
    global cookie,opener
    p={"ck":""}
    c = [c.value for c in list(cookie) if c.name == 'ck']
    if len(c) > 0:
        p["ck"] = c[0].strip('"')
        addtopicurl="http://www.douban.com/group/163816/new_topic"
        p["rev_title"] = title
        p["rev_text"] = content
        p["rev_submit"] = '���ˣ�����'

        request=urllib2.Request(addtopicurl)
        request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
        request.add_header("Accept-Charset", "GBK,utf-8;q=0.7,*;q=0.3")
        request.add_header("Origin", "http://www.douban.com")
        request.add_header("Referer", "http://www.douban.com/group/python/new_topic")
        resp = opener.open(request, urllib.urlencode(p))
#        print resp.getcode()
#        print resp.info()
#        print resp.geturl()
        print '�����ɹ�'
    else:
        print 'Error post'

def post_self_broadcast(content):
    print '׼�����㲥'
    global cookie,opener
    p={"ck":""}
    c = [c.value for c in list(cookie) if c.name == 'ck']
    if len(c) > 0:
        p["ck"] = c[0].strip('"')
        addtopicurl="http://www.douban.com/"
        p["comment"] = content
        request=urllib2.Request(addtopicurl)
        request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
        request.add_header("Accept-Charset", "GBK,utf-8;q=0.7,*;q=0.3")
        request.add_header("Origin", "http://www.douban.com")
        request.add_header("Referer", "http://www.douban.com/")
        resp = opener.open(request, urllib.urlencode(p))
#        print resp.getcode()
#        print resp.info()
#        print resp.geturl()
        print '���㲥�ɹ�'
    else:
        print 'Error broadcast'
        
    


#����ҳ�ύ��¼
response=opener.open(loginurl, urllib.urlencode(params))

#��֤�ɹ���ת����¼ҳ
if response.geturl() == "https://www.douban.com/accounts/login":
    html=response.read()
#��֤��ͼƬ��ַ
    imgurl=re.search(r'<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url=imgurl.group(1)
#��ͼƬ������ͬĿ¼��
        res=urllib.urlretrieve(url, 'v.jpg')
#��ȡcaptcha-id����
        captcha=re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>' ,html)
        if captcha:
            vcode=raw_input('������ͼƬ�ϵ���֤�룺')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "��¼"
#�ύ��֤����֤
            response=opener.open(loginurl, urllib.urlencode(params))
            
            if response.geturl() == "http://www.douban.com/":
                print 'login success ! '
                #post_group_topic('testdwqwe','just english')
                post_self_broadcast('posted by python for tests��')
