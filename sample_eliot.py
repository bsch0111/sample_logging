import json
import sys

from eliot import Message, start_action, to_file, write_traceback
import requests

#로그 출력을 표준 출력으로 설정 (터미널에 출력하기)
to_file(sys.stdout)

PAGE_URL_LIST = [
    'https://brickset.com/',
    'http://google.com/',
    'https://xxunjin3786.tistory.com/311'
]

def fetch_page():

    # 어떤 타입의 로그인지는 action_type으로 지정
    with start_action(action_type="fetch_pages"):
        page_contents = {}
        for page_url in PAGE_URL_LIST:
            
            with start_action(action_type="download", url=page_url):
                try:
                    r = requests.get(page_url, timeout = 30)
                    r.raise_for_status()
                except requests.exceptions.RequestException as e:
                    write_traceback() # 예외가 발생하면 트레이스백 출력
                    continue
                
                page_contents[page_url] = r.text

if __name__ == "__main__" :
    page_contents = fetch_page()
    with open('page-contents.json','w') as f_page_contents:
        json.dump(page_contents,f_page_contents, ensure_ascii=False)

    Message.log(message_type="info", msg="데이터를 저장했습니다")