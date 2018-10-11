"""
세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a
< b < c ).
예를 들면 3**2 + 4**2 = 9 + 16 = 25 = 5**2이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?


Date: 2018/03/20
"""


diff = 1
while True:
    a, b = 1, 1 + diff
    while a + b < 1000:
        c = (a**2 + b**2) ** (1/2)
        if a + b + c == 1000:
            print(a * b * c)
        else:
            a += 1
            b += 1
    diff += 1