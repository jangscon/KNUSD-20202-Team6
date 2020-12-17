# 보기 편한 문자열로 날짜 정보를 변경
def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime(fmt)