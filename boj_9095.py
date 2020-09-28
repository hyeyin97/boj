test_case=int(input())
ans_lst=[0,1,2,4]
input_lst =[]

for _ in range(test_case):
    input_lst.append(int(int(input())))
max_num=max(input_lst)

if max_num>=4:
    for i in range(4,max_num+1):
        ans_lst.append(ans_lst[i-1]+ans_lst[i-2]+ans_lst[i-3])

for num in input_lst:
    print(ans_lst[num])