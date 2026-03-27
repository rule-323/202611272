mode=int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 :"))

if mode==1 :
    expression=input("*** 수식을 입력하세요 :")
    answer=eval(expression)
    print(f"{expression}의 결과는 {answer}입니다.")

elif mode==2 :
    num1=int(input("첫 번째 숫자를 입력하세요 :"))
    num2=int(input("두 번째 숫자를 입력하세요 :"))
    result=sum(range(num1,num2+1))
    print(f"{num1}+...+{num2}는 {result}입니다.")

else :
    print("1 또는 2만 입력해야 합니다.")