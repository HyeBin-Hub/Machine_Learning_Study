# -*- coding: utf-8 -*-
"""
1. text file 읽기 
2. 명사 추출 : Kkma object
3. 전처리 : 음절 길이(2~8), 숫자 제거 
4. word count : 단어 빈도수 
5. word cloud : 단어 구름 시각화
"""

from konlpy.tag import Kkma

# object
kkma = Kkma()

# 1. text file 읽기 
file = open("C:/python_ML/Chap06_TextMining/data/text_data.txt",mode="r",encoding="utf-8")
doc = file.read() # text 전체 읽기 
print(doc)
file.close() # object close

# 2. doc -> sentence
ex_sent = kkma.sentences(doc) # list
#print(ex_sent)
#len(ex_sent) # 4


# 3. doc -> noun
ex_nouns = kkma.nouns(doc)
#print(ex_nouns)
#len(ex_nouns) # 13


# 4. 중복 단어 추출 -> 전처리 
nouns_word = [] # list

import re
for sent in ex_sent :# 문장 단위('형태소 분석을 시작합니다.') 
    for noun in kkma.nouns(sent) : # 단어 단위('형태소', '분석')
        # 단어 전처리(1음절, 숫자 제거)
        if len(str(noun)) > 1 and not(re.match('^[0-9]', noun)) : 
            nouns_word.append(noun)
        
print(nouns_word)
len(nouns_word) # 15 -> 12


# 5. word count 
nouns_count = {} # set -> dict{key:value}

for noun in nouns_word :
    # key = value
    nouns_count[noun] = nouns_count.get(noun, 0) + 1

print(nouns_count)
# {'형태소': 1, '분석': 3, '데이터': 2, '직업': 1, '전문가': 1, '기법': 1, '초반': 1, '개발': 1, '기술': 1}

# 6. word cloud 
from collections import Counter

# 1) dict -> Counter
counter = Counter(nouns_count)

# 2) top word
word_top5 = counter.most_common(5)
print(word_top5)
# [('분석', 3), ('데이터', 2), ('형태소', 1), ('직업', 1), ('전문가', 1)]

# 3) word cloud 시각화 
import pytagcloud
'''
Anaconda Prompt에서 
  pip install pygame
  pip install pytagcloud
  pip install simplejson
'''

# tag에 color, size, tag 사전 구성 
word_count_list = pytagcloud.make_tags(word_top5, maxsize=80)
# maxsize : 최대 글자크기
print(word_count_list)
'''
[{'color': (91, 34, 34), 'size': 109, 'tag': '분석'}, {'color': (95, 159, 59), 'size': 80, 'tag': '데이터'}, {'color': (194, 214, 193), 'size': 47, 'tag': '형태소'}]
'''
pytagcloud.create_tag_image(word_count_list,
                            'wordcloud.jpg', 
                            size=(900, 600), 
                            fontname='korean', rectangular=False)
'''
한글 단어 구름 시각화 Error 수정 
C:\Users\user\Anaconda3\Lib\site-packages\pytagcloud\fonts 폴더에서
  1. fonts.json 파일 내용 수정 
  [
    {
        "name": "korean",
        "ttf": "malgun.ttf",
  2. C:\Windows\Fonts 폴더에서 '맑은 고딕' 서체 복사/fonts 폴더 붙여넣기
  3. create_tag_image(fontname='korean') 속성 추가
'''





