def first_digit(num):
    num=abs(num)
    if num>=1:
        while num//10>0:
            num //=10
    else:
        while num*10<1:
            num *=10
        num = round(num*10)
    return num

def scientific_notation(num,trunc=16):
    sign = "-" if num < 0 else ""
    exp=0
    if num>=1:
        while num/10>1:
            num /=10
            exp += 1
    elif num>0:
        while num*10<10:
            num *=10
            exp -=1
        num = num
    if trunc == 0: trunc-=1 # To delete the floating point from next string
    return sign+str(num)[:trunc+2]+f"*10^{exp}"
print(scientific_notation(234.76574,1))