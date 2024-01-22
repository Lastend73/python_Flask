import datetime as d

# 데이터 : model
guestbook=[]
gb1={"gno" : 1, "content" : "첫번째 방명록", "writeday" : "2024-01-22"}
gno=3

# 파이썬에서 타입은 모두 클래스
# 클래스 이름으로 객체를 생성할 수 있다
# 클래스 이릅 함수처럼 사용할 수 있다
gb2 = dict(gno=2, content = "두번쨰 방명로", writeday = "2024-01-22")

guestbook.append(gb1)
guestbook.append(gb2)

def findall() :
    return guestbook

def save (content:str) :
    global gno
    writeday = d.datetime.now().date()
    gb = dict(gno = gno, content=content, writeday=writeday)
    guestbook.append(gb)
    gno+=1

def delete(gno :int):
    for gb in guestbook :
        if gb['gno'] == gno :
            guestbook.remove(gb)

# def hap(val1: int , val2 :int) -> int :
#     return val1 + val2
# hap(10,20)

# hap(val2 = 20, val1 = 10)
