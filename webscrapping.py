import requests
URL = 'https://www.amazon.in/Apple-iPhone-XR-64GB-White/dp/B07JGXM9WN/ref=sr_1_6?keywords=iphone&qid=1568472264&s=gateway&sr=8-6'

headers = {"userAgent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15'}

page = requests.get(URL)