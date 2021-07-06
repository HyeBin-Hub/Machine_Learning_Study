# -*- coding: utf-8 -*-
"""
news crawling data file 
 - word cloud 시각화
"""

from konlpy.tag import Kkma

kkma = Kkma()

kkma.nouns("코로나19 우리나라 만세")
# ['코로나', '코로나19', '19', '우리', '나라', '만세']
kkma.pos("코로나19 우리나라 만세")
# ('코로나', 'NNG')

# 1. text file load 
file = open("D:/Python_ML/chap06_TextMining/data/crawling_data.txt", encoding='utf-8')
news_data = file.read() # 전체 news 읽기 
print(news_data)
file.close()


# 2. text data(docs) -> sentence 추출 
ex_sent = kkma.sentences(news_data) # list
print(ex_sent)
len(ex_sent) # 4

# 3. sentence -> nouns 추출 
nouns_word = [] # list

import re
for sent in ex_sent : # 문장 단위('형태소 분석을 시작합니다.') 
    for noun in kkma.nouns(sent) : # 단어 단위('형태소', '분석')
        # 단어 전처리(1음절, 숫자 제거)
        if len(str(noun)) > 1 and not(re.match('^[0-9]', noun)) : 
            nouns_word.append(noun)
        
print(nouns_word)
len(nouns_word) # 228


# 4. word count 
nouns_count = {} # set -> dict{key:value}

for noun in nouns_word :
    # key = value
    nouns_count[noun] = nouns_count.get(noun, 0) + 1

print(nouns_count)


# 5. word cloud 시각화 : top10 단어 시각화 
from collections import Counter

# 1) dict -> Counter
counter = Counter(nouns_count)

# 2) top word
word_top10 = counter.most_common(10)
print(word_top10)
# [('분석', 3), ('데이터', 2), ('형태소', 1), ('직업', 1), ('전문가', 1)]

# 3) word cloud 시각화 
import pytagcloud

# tag에 color, size, tag 사전 구성 
word_count_list = pytagcloud.make_tags(word_top10, maxsize=80)
# maxsize : 최대 글자크기
print(word_count_list)

pytagcloud.create_tag_image(word_count_list,
                            'news_crawling.jpg', 
                            size=(900, 600), 
                            fontname='korean', rectangular=False)

# image file name : news_crawling.jpg














