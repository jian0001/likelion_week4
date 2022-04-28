import random
import time

dinner=[]
i =0

print("5 개의 메뉴를 추천해주세요! 5 개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요! \n")

while(len(dinner)!=5): #리스트 길이가 5가 되기 전까지 반복
    a=input("메뉴 추가: ")
    for i in range (len(dinner)): 
        if(dinner[i]==a): #같은 요소가 있는 경우
            print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
            dinner.remove(dinner[i])
            break
    dinner.append(a)
    print("현재 메뉴 수 = "+str(len(dinner))+"\n")

for i in range (3,0,-1):
    time.sleep(1)
    print(i)

print()
print(dinner)
print("과연 오늘의 메뉴는? \n")

for i in range (3,0,-1):
    time.sleep(1)
    print(i)
print("")

today=random.randint(1,5)
print("오늘의 메뉴는 "+str(i)+"번째 메뉴, "+dinner[i-1]+"입니다!")