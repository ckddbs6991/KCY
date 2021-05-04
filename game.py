win = { '가위': '보',
        '바위': '가위',
        '보': '바위'
}

dict_a = {"가위", "바위", "보"}
print(type(dict_a))
print(dict_a)

def start(mine, yours):
    result = '0'
    if mine == yours:
        result = 'draw'
        return result
    elif win[mine] == yours:
        result = 'win'
        return result
    else:
        result = 'lose'
        return result

while 1:
    me = input('가위, 바위, 보 중 선택 종료는 "종료"를 입력하세요')
    if me == '종료':
        break
    elif (me != '가위') and (me != '바위') and (me != '보'):
        print('가위 바위 보를 입력하지 않았습니다.')
        continue
    else:
        import random
        list = ['가위', '바위', '보']
        you = random.choice(list)
        print('{} 나:{} 컴퓨터:{}'.format(start(me, you), me, you))
print('가위 바위 보 프로그램 종료')
        