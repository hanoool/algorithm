array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count(array[i]) += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)):
    for j in range(count[i]): 
        print(i, end=" ") # 인덱스에 해당하는 array 숫자가 몇번 나왔는지에 따라 print
# 예시
# i = 0 일 때, count[0] = 2
# 따라서 0, 0 프린트 함