#kkma_실습.py
from konlpy.tag import Kkma

kkma=Kkma()

text="아버지가 방에 들어갑니다."

morphs=kkma.morphs(text)
print(morphs)

pos=kkma.pos(text)
print(pos)

nouns=kkma.nouns(text)
print(nouns)

sentences="오늘 날씨는 어때요? 내일은 덥다던데."
s=kkma.sentences(sentences)
print(s)