def solution(id_pw, db):
    answer = ''
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            return 'login'
        elif i[0] == id_pw[0] and i[1] != id_pw[1]:
            answer = 'wrong pw'
    if answer == '':
        return 'fail'
    return answer