import random

def main():
    hangul = list("최강박이김오홍신류장고")
    hanguls2 = list("가나다라마바사아자차카타파하길하동원시병강방동정궁군정현태원연우운호이도")

    for _ in range(50):
        random_hangul = random.choice(hangul) + str().join(random.choices(hanguls2, k=2))
        print(random_hangul)

if __name__ == "__main__":
    main()  
