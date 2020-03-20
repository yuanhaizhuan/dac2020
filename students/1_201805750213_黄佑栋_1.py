#!/usr/bin/env python
# coding: utf-8

# # 《数据采集与清洗》
# ## 第一次作业内容： 网页抓取
# ### 具体目标：
# + 用``urllib.requests``库发起一次``get``请求，输出``response``文本信息；
# + 用``Requests``库伪装成火狐浏览器发起一次``post``请求，输出``response``文本信息；
# + 用``Requests``库中的``session``对象发出``get``请求，设置``cookies``并获取，输出获取的``cookies``内容；
# + 实现抓取网页的不去重深度遍历算法，自选合适的种子网站和相关参数，输出结果；
# + 编写抓取网页的广度遍历算法（含去重和不去重），自选合适的种子网站和相关参数，输出结果；
# + (选)将抓取网页的去重深度遍历算法封装成对象（类），并测试。
# 
# ### 注：
# + 代码要有注释，结果要有分析；
# + 本次作业提交截至时间：2020年3月10日(星期二)；
# + 文件命名规则: 班级号+学号+姓名+作业序号，示例：``1_20188989899_张三_1``；
# + 提交方式：1班发送至邮箱：632994085@qq.com；2班发送至邮箱：786888939@qq.com.

# ### 问题1：用``urllib.requests``库发起一次``get``请求，输出``response``文本信息。

# In[54]:


# 这里编写代码


# In[55]:


import requests  #导入urllib.request库
url='https://baike.baidu.com/'#赋值

r = requests.get(url)  #发起post请求

r.encoding = 'utf-8'  #将编码转换成utf—8

print(r.text) 


# 返回得到网页编码。

# ### 用``Requests``库伪装成火狐浏览器发起一次``post``请求，输出``response``文本信息。

# In[56]:


# 这里编写代码


# In[57]:


import requests     #导入requeses库
url='https://baike.baidu.com/'    #赋值
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.3974.400",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
    }#伪装浏览器（联想浏览器）
r=requests.post(url,headers)#发起post请求
print(r.text)


# 返回得到网页编码。

# ### 用``Requests``库中的``session``对象发出``get``请求，设置``cookies``并获取，输出获取的``cookies``内容。 

# In[58]:


# 这里编写代码


# In[59]:


import http.cookiejar, urllib.request #导入requeses库
s = requests.Session()  #构造session对象
s.get('http://httpbin.org/cookies/set/sessioncookie/1481872811') #用sessino对象发起get请求，并设置cookies
r = s.get("http://httpbin.org/cookies")  #用session对象发起另外一个get请求，获取cookies内容
print(r.text)  #输出cookies内容


# 返回得到cookies内容。

# ### 实现抓取网页的不去重深度遍历算法，自选合适的种子网站和相关参数，输出结果。
# 

# In[60]:


# 这里编写代码


# In[61]:


import requests, re  #导入requests库，re库
count = 10     #计数器设为10
r = re.compile(r'href=[\'"]?(http[^\'" >]+)')  
seed = 'http://cookdata.cn/' # 选择网站
queue = [seed]   #建立栈
storage = {}
while len(queue) > 0 and count > 0:  #while循环
    try:
        url= queue.pop(0)  
        html = requests.get(url).text #用requests库发起get请求
        new_urls = r.findall(html) 
        queue.extend(new_urls)  #将新返回的列表返回原列表中
        storage[url] = len(new_urls)
        count -= 1  #计数器减一
    except Exception as e:
        print(e)
    else:
        print(url) 


# 这里对结果进行分析。

# ### 编写抓取网页的广度遍历算法（含去重和不去重），自选合适的种子网站和相关参数，输出结果。 

# In[62]:


# 这里编写代码


# In[63]:


import requests, re    #导入requests库，re库
count = 10     #计数器设为10
r = re.compile(r'href=[\'"]?(http[^\'" >]+)')
seed = 'http://cookdata.cn/' # 导入网站
stack = [seed]   #建立栈
storage = set()  
while len(stack) > 0 and count > 0:    #while循环
    try:
        url = stack.pop(-1)
        html = requests.get(url).text
        new_urls = r.findall(html)
        storage.add(url)
        for n_url in new_urls:
            if n_url not in storage:
                stack.extend(new_urls) 
        count -= 1
    except Exception as e:
        print(e) 
    else:
        print(url)


# 这里对结果进行分析。

# ### (选)将抓取网页的去重深度遍历算法封装成对象（类），并测试。 

# In[64]:


# 这里编写代码


# In[65]:


# 测试


# 这里对结果进行分析。

# In[ ]:





# In[ ]:




