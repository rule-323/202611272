#입력할 진수 결정
base=int(input("입력 진수 결정(16/10/8/2):"))

#값 입력
value=input("값 입력:")

#입력한 값 10진수로 변환
number=int(value,base)

print("16진수 ==> ",hex(number))
print("10진수 ==> ",number)
print("8진수 ==> ",oct(number))
print("2진수 ==> ",bin(number))