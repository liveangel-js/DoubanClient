# -- coding:gbk --
import sys, time, os, re
import urllib, urllib2, cookielib

loginurl = 'https://www.douban.com/accounts/login'
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

params = {
"form_email":"27481991@qq.com",
"form_password":"skm7585999",
"source":"index_nav" #没有的话登录不成功
}

def post_group_topic(title,content):
    print '准备进行发帖'
    global cookie,opener
    p={"ck":""}
    c = [c.value for c in list(cookie) if c.name == 'ck']
    if len(c) > 0:
        p["ck"] = c[0].strip('"')
        addtopicurl="http://www.douban.com/group/163816/new_topic"
        p["rev_title"] = title
        p["rev_text"] = content
        p["rev_submit"] = '好了，发言'

        request=urllib2.Request(addtopicurl)
        request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
        request.add_header("Accept-Charset", "GBK,utf-8;q=0.7,*;q=0.3")
        request.add_header("Origin", "http://www.douban.com")
        request.add_header("Referer", "http://www.douban.com/group/python/new_topic")
        resp = opener.open(request, urllib.urlencode(p))
#        print resp.getcode()
#        print resp.info()
#        print resp.geturl()
        print '发帖成功'
    else:
        print 'Error post'

def post_self_broadcast(content):
    print '准备发广播'
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
        print '发广播成功'
    else:
        print 'Error broadcast'
        
    


#从首页提交登录
response=opener.open(loginurl, urllib.urlencode(params))

#验证成功跳转至登录页
if response.geturl() == "https://www.douban.com/accounts/login":
    html=response.read()
#验证码图片地址
    imgurl=re.search(r'<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url=imgurl.group(1)
#将图片保存至同目录下
        res=urllib.urlretrieve(url, 'v.jpg')
#获取captcha-id参数
        captcha=re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>' ,html)
        if captcha:
            vcode=raw_input('请输入图片上的验证码：')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "登录"
#提交验证码验证
            response=opener.open(loginurl, urllib.urlencode(params))
            
            if response.geturl() == "http://www.douban.com/":
                print 'login success ! '
                #post_group_topic('testdwqwe','just english')
                post_self_broadcast('posted by python for tests我')
