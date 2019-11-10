"""
实现print函数
"""


def print_string(*arg, sep=' ', end=''):
    v_result = ''
    for i in range(len(arg)):
        # 如果为最后一个元素，那么接结束符
        if i == len(arg) - 1:
            v_result += arg[i] + end
        # 如果不为最后一个元素，那么接连接符
        else:
            v_result += arg[i] + sep
    print(v_result, '\n')


print_string('This is a test')
print_string('This', 'is', 'a', 'test')
print_string('This', 'is', 'a', 'test', sep='-')
print_string('This', 'is', 'a', 'test', ',', 'Yes', sep='_', end='.')
