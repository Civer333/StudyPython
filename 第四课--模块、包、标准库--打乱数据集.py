import random
# you may need import some package
x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']

def shuffle(a,b):
    # your code here
    #把x,y压缩，形成字典形成对应关系
    c = list(zip(a,b))
    #把数据打乱
    random.shuffle(c)
    #把压缩后的c解压重新赋值到a,b
    a[:],b[:]=zip(*c)
    return a,b

if __name__ == '__main__':
    # print result for certify
    shuffle(x,y)

    for i,j in zip(x,y):
        print(i,':',j)