import json
import time
import requests

PAGE_URL_LIST = [
    'https://brickset.com/',
    'http://google.com/',
    'https://eunjin3786.tistory.com/311'
]

def fetch_pages():

    with open('crawler_info2.log', 'a') as f_info_log, \
        open('crawler_error2.log', 'a') as f_error_log:

        page_contents = {}

        msg = '[INFO] 크롤링을 시작합니다. \n'
        print(msg)
        f_info_log.write(msg)

        for page_url in PAGE_URL_LIST:
            try:
                r = requests.get(page_url, timeout=30)
                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                msg = f"[ERROR] {e}"
                print(msg)
                f_error_log.write(e)
                continue

        page_contents[page_url] = r.text
        time.sleep(1)

    return page_contents

if __name__ == '__main__':
    page_contents = fetch_pages()
    with open('page_contents.json','w') as f_page_contents :
        json.dump(page_contents, f_page_contents, ensure_ascii=False)
        