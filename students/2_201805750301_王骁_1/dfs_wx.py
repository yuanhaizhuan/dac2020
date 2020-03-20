import re 
import requests
try:
    import _locale
except ImportError:
    _locale = None

__version__ = "0.0.1"

__r = re.compile(r'href=[\'"]?(http[^\'" >]+)')

def findurl(url,n=5):
	'''
	返回从URL指定网址爬取的URL链接组成的列表变量，采用深度优先爬取算法。
	
	| url ： 指定的待爬取网址链接
	| n   ： 指定的爬取深度，默认深度为5
	'''
	stack = [url]
	used = set()
	storage = {}
	while len(stack) > 0 and n > 0:
		try:
			seed = stack.pop(-1)
			html = requests.get(seed).text
			storage[seed] = html
			used.add(seed)
			new_urls = __r.findall(html)
			for new_url in new_urls:
				if new_url not in used and new_url not in stack:
					stack.append(new_url)
			n -= 1
		except Exception as e:
			print(seed)
			print(e)
	return stack

if __name__ == '__main__':
	url = 'http://httpbin.org/'
	list_test = findurl(url)
	print('网址 “http://httpbin.org” 利用深度优先算法，深度为5时，爬取得到的url列表有 %d' % len(list_test))

# 
# 
# 暂时只封装了获取指定URL中的URL链接的函数
# 
# 仍缺少内存释放机制等
