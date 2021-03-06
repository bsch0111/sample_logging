from logging import (
    getLogger,
    Formatter,
    FileHandler,
    StreamHandler,
    DEBUG,
    ERROR
)

import requests

logger = getLogger(__name__)

# %(포맷될 변수명)타입 구성 
default_format = '[%(levelname)s] %(asctime)s %(name)s %(filename)s : %(lineno)d %(message)s'
default_formatter = Formatter(default_format)
funcname_formatter = Formatter(default_format + ' (%(funcName)s)')

# 로그 정용 핸들러 : 콘솔 출력 전용
log_stream_handler = StreamHandler()
log_stream_handler.setFormatter(default_formatter)
log_stream_handler.setLevel(DEBUG)

# 로그 저용 핸들러 : 파일 출력 전용
log_file_handler = FileHandler(filename='crawler2.log')
log_file_handler.setFormatter(funcname_formatter)
log_file_handler.setLevel(ERROR)

# 로거에 핸들러와 레벨 설정하기
logger.setLevel(DEBUG)
logger.addHandler(log_stream_handler)
logger.addHandler(log_file_handler)

def logging_example():
    logger.info('크롤링을 시작합니다.')
    logger.warning('외부 사이트 링크는 크롤링하지 않습니다.')
    logger.error('페이지를 찾을 수 없습니다.')

    try:
        r = requests.get('#invalid_url', timeout=1)
    except requests.exceptions.RequestException as e:
        logger.exception('요청 중에 예외가 발생했습니다 : %r', e)

if __name__ == '__main__':
    logging_example()