board_list=[]
board_list.append(dict(bno=1,title='aa',content='a',nickname='gdgd',readcnt=0))
board_list.append(dict(bno=2,title='aa',content='a',nickname='gdgd',readcnt=0))
board_list.append(dict(bno=3,title='aa',content='a',nickname='gdgd',readcnt=0))
bno = 4

def findall():
    return board_list

def findone(bno : int) ->dict:
    for board in board_list:
        if board['bno'] == bno:
            board['readcnt']+=1
            return board
    return None

def save(title : str, content : str, nickname)-> bool:
    global bno 
    b = dict(bno = bno, title = title, content = content, nickname =nickname)
    board_list.append(b)
    bno+=1
    return True

