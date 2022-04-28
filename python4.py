market={}
while(True):
    key=input("Enter a fruit type (q to quit): ")
    if(key=="q"):
        print(market)
        break
    value = input("Enter the weight in kg: ")
    market[key]=value