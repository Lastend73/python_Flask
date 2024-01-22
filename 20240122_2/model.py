import datetime as d

guestbook = []
gno = 2

gbtest = dict(gno = 1, name="테스트",content = "test" , time = "2024-01-21")
guestbook.append(gbtest)

def delete(gno : int) :
    for gb in guestbook :
        if gb["gno"] == gno :
            guestbook.remove(gb)
            break

def save(name :str , content : str) :
    global gno
    gbsave = dict(gno = gno, name=name,content = content , time = d.datetime.now().date())
    guestbook.append(gbsave)
    gno += 1

def list() :
    return guestbook

#변경
def update(gno:int, content :str) :
    for gb in guestbook :
        if gb["gno"] == gno :
            gb["content"] = content
            break