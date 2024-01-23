# 게시판 dao 작성
board_list = []
bno = 1

# 게시판은 글번호,제목,내용,글쓴이 조회수

#save
def save(title :str , content : str , writer: str ) -> bool :
    global bno
    b0 = dict(bno = bno,title=title, content = content , writer=writer,readcnt=0)
    board_list.append(b0)
    bno += 1
    return True

def findak() -> list:
    return board_list
