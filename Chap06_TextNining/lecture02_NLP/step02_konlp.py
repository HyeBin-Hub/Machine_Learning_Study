


from konlpy.tag import Kkma   # object생성할수있는 class

Kkma = Kkma()  # object생성
print(Kkma)   # object info 를 확인할수 있다


# 문단 -> 문장 추출
para = "형태소 분석 시작합니다. 나는 홍길동이고, age는 28세 입니다."
ex_sent = Kkma.sentences(para)
print(ex_sent )   # list로 반환
#['형태소 분석 시작 합니다.', '나는 홍길동이고, age는 28세 입니다.']

# 문단 -> 명사 추출
ex_nouns = Kkma.nouns(para)
print(ex_nouns)
#['형태소', '분석', '나', '홍길동', '28', '28세', '세']

# 문단 -> 형태소(품사) 추출
ex_pos = Kkma.pos(para)
print(ex_pos)
"""
[('형태소', 'NNG'), ('분석', 'NNG'), ('시작하', 'VV'), ('ㅂ니다', 'EFN'), ('.', 'SF'), ('나', 'NP'), 
('는', 'JX'), ('홍길동', 'NNG'), ('이', 'VCP'), ('고', 'ECE'), (',', 'SP'), ('age', 'OL'), ('는', 'JX'), 
('28', 'NR'), ('세', 'NNM'), ('이', 'VCP'), ('ㅂ니다', 'EFN'), ('.', 'SF')]
=>(단어,품사)
"""

# NNG : 일반명사, NNP : 고유명사 , NP: 대명사 특정 품사만 뽀는다
ex_pos2=[]

for (text,tclass) in ex_pos:
    if tclass == "NNG" or tclass == "NNP" or tclass =="NP":
        ex_pos2.append(text)

print(ex_pos2)  # ['형태소', '분석', '나', '홍길동']  










