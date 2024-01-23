# 웹프로그램을 이렇게 만들자 : MVC
# Model : 데이터 -> model의 조작을 담당하는 파일(Dao)
# View : 화면
# Controller : 모델과 뷰를 연결한다

import datetime 

guestbook = []
gh = dict(gno=1, nickname = "홍길동", content = "욕설. 비방은 경고없이 삭제합니다",writeday= '2025-01-23')
guestbook.append(gh)
gno = 2

# crd

def save(nickname : str, content:str) -> bool: 
    global gno
    writeday = datetime.datetime.now().date()
    gb = dict(gno=gno , nickname=nickname, content= content, writeday = writeday)
    guestbook.append(gb)
    gno+=1
    return True

def findall() -> list:
    return guestbook


def delete(gno : int) ->bool :
    for gb in guestbook :
        if gb['gno'] == gno:
            guestbook.remove(gb)
            return True
    return False