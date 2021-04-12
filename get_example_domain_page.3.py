import json
import time
import requests


PAGE_URL_LIST = [
    'https://brickset.com/',
    'http://google.com/',
    'https://eunjin3786.tistory.com/311'
]

def fetch_page():
    """ 페이지의 내용을 추출합니다. """
    f_info_log = open('crawler_info.log', 'a')
    f_error_log = open('crawler_error.log', 'a')

    page_contents = {}

    msg = "크롤링을 시작합니다.\n"
    print(msg)
    f_info_log.write(msg)

    for page_url in PAGE_URL_LIST :
        r = requests.get(page_url, timeout=30)
        try:
            r.raise_for_status() # 응답에 문제가 있으면 예외를 발생시키는 코드
        except requests.exceptions.RequestException as e:
            # requets 와 관련된 예외가 발생하면
            msg = f"[ERROR] {e}"
            print(msg)
            f_error_log.write(e)
            continue
    page_contents[page_url] = r.text
    time.sleep(1) # 상대 사이트에 대한 부하를 고려해서 요청 간격을 설정

    f_info_log.close()
    f_error_log.close()

    return page_contents

if __name__ == "__main__":
    page_contents = fetch_page()
    f_page_contents = open('page_contents.json','w')
    json.dump(page_contents, f_page_contents, ensure_ascii=False)
    f_page_contents.close()