import requests
import random

T4IR_5th = {
    "class": ["OA", "BD", "BC", "CC"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "members": {
        "1304":  {
            "lecturer": "juan",
            "manager": "yj",
            "class president": "윤현수",
            "groups": {
                "1조": ["강보성", "한수용", "최영선"],
                "2조": ["호유송", "전지나", "설동재"],
                "3조": ["강다영", "윤현수", "김소미"],
                "4조": ["홍성재", "이경준", "박찬우"], 
                "5조": ["김유정", "오현경", "고예성"],
                "6조": ["박건호", "이민우", "이영걸", "경현"]
            }
        },
        "1303": {
            "lecturer": "eric",
            "manager": "cw"
        }
    }
}


# 난이도* 1. 지역(location)은 몇개 있나요? : list length
# 출력예시)
# 4
print('===Q1===')
print(len(T4IR_5th['class']))


# 난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
# 출력예시)
# false
print('===Q2===')
list = T4IR_5th['language']['python']['python standard library']
if 'request' in list:
    print('true')
else:
    print('false')


# 난이도** 3. 1304호의 반장의 이름을 출력하세요. : depth 있는 접근
# 출력예시)
# ???
print('===Q3===')
print(T4IR_5th['members']['1304']['class president'])


# 난이도*** 4. T4IR_5th에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
# 출력 예시)
# python
# web
print('===Q4===')
for a in T4IR_5th['language'].keys():
    print(a)


# 난이도*** 5 T4IR_5th 1303호의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
# 출력 예시)
# eric
# cw
print('===Q5===')
for a in T4IR_5th['members']['1303'].values():
    print(a)


# 난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
# 출력 예시)
# flask는 micro이다.
# django는 full-functioning이다.
print('===Q6===')
dict_frameworks = T4IR_5th['language']['python']['frameworks']
for key in dict_frameworks:
    print(f'{key}는 {dict_frameworks[key]}이다.')


# 난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
# 출력예시)
# 오늘의 당번은 ???
print('===Q7===')
dict_groups = T4IR_5th['members']['1304']['groups']['4조']
ran = random.choice(dict_groups)
print(f'오늘의 당번은? {ran}')