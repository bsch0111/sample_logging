import time
import requests

PAGE_URL_LIST = [
    'https://brickset.com/',
    'http://google.com/',
    'https://eunjin3786.tistory.com/311'
]

for page_url in PAGE_URL_LIST :
    res = requests.get(page_url, timeout=30)
    print(
        f"페이지 URL : {page_url} ," + \
        f"HTTP 상태  : {res.status_code}," + \
        f"처리 시간(초) : {res.elapsed.total_seconds()}"
    )
    time.sleep(1)