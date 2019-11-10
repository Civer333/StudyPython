"""
实现斐波那契
"""
#for 循环
def Fibonacci_for(num):
    #初始化前两个值
    a,b=1,1
    result=[a,b]
    #从第三个开始，每个数为前两个数之和
    if num >=3 :
        for i in range(num-2):
            temp = a+b
            result.append(temp)
            a = b
            b = temp
    #截止到第num个数的序列有
    print(result)
    #第num个数为
    print(result[num-1])

Fibonacci_for(5)