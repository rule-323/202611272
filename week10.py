# 넘파이 배열
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

# 인덱싱, 슬라이싱
print(arr[1]) #인덱싱
print(arr[1:4]) #슬라이싱

# array 외...
arr1=np.arange(1,8,1) #마치 range
print(arr1) # [1 2 3 4 5 6 7]

arr2=np.linspace(1,9,5) #1부터 9까지 5개의 숫자를, 요소 간격이 일정하도록 생성
print(arr2) # [1. 3. 5. 7. 9.]

arr3=np.zeros(10)
print(arr3) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

arr4=np.ones(10)
print(arr4) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

arr5=np.full(10,5) #지정한 수로 이루어진 배열 (개수, 값)
print(arr5) # [5 5 5 5 5 5 5 5 5 5]


# 원하는 차원의 배열 생성하기
arr=np.array([[1,2,3],[4,5,6]]) #2행 3열인 2차원 배열
print(arr)

# 배열이름[행 인덱스, 열 인덱스]
print(arr[0,1]) # 2
print(arr[1,2]) # 6
print(arr[0,1],arr[1,2]) # 2 6

# shape : 배열에 대한 각 차원의 크기를 알려주는 속성
print(arr.shape) # (2, 3) : 2행 3열

# reshape : 배열을 데이터 변경 없이 새로운 모양으로 변경하는 속성
arr1=np.array([1,2,3,4,5,6])
arr2=arr1.reshape(3,2) # 3행 2열로 변경
print(arr1)
print(arr2)


# 리스트 각 항목에 2를 곱하기
# for문.ver
lst=[2,3,4]
result=[]
for i in range(0,len(lst),1):
    result.append(lst[i]*2)
print(result) # [4, 6, 8]

# 리스트 내포.ver
lst=[2,3,4]
result=[x*2 for x in lst] # x에 lst의 각 항목이 순서대로 대입됨
print(result) # [4, 6, 8]

# 배열의 연산.ver
# 숫자와 배열의 연산
arr=np.array([2,3,4])
result=arr*2
print(result) # [4 6 8]

# 배열과 배열의 연산
arr1=np.array([2,3,4])
arr2=np.array([5,6,7])
result=arr1+arr2
print(result) # [7 9 11]


# 이차함수 y=x^2
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,100) # -1부터 1까지 100개의 숫자를 생성
y=x**2

plt.figure(figsize=(5,3)) # 그래프의 크기 설정
plt.plot(x,y,label='y=x^2')
plt.legend() # 범례 표시
plt.show() # 그래프 출력

score=np.array([71,80,60,90,65])
result=np.where(score>=90,'A',
                np.where(score>=80,'B',
                         np.where(score>=70,'C','D')))
print(result) # ['C' 'B' 'D' 'A' 'D']