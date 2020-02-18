
# coding=utf-8

import time

#if __name__ == '__main__':
#   print "hello world"

#写个程序,可以访问网页,并且把数据包存下来

def test():
    now_time = time.time()
    print "fsdfsdf ,this is my house"
    a=1000;
    a += 1;
    b = 'test string'
    print b

def foo(x=10):
    "This is a doc string"
    x += 1
    print 'call foo(): a=', x
    return x

if __name__ == '__main__':
    print("hello, python!")
    print "hello lion, you are danger"

    #test()

    #foo()

    a = 1
    #while a < 10:
    #    print(a)
    #    a += 1

    word = 'word'
    sentence = "这是一个句子"
    paragraph = """这个一个段落
    包含了多个语句"""

    word = 'lion'
    #打印

    word = 'hello'

    print word  # 1

    #raw_input("按下 enter 退出，其他任意键显示....\n")  #\n 实现换行

    import sys; x = 'runoob'; #sys.stdout.write(x)
    sys.stdout.write(x + '\n')

    x = "a"
    y = "b"
    print x
    print y
    print '-----------'
    print x,
    print y,

    print x,y

    a = 3

    if a == 1:
        print "1"
    elif a == 2:
        print "2"
    else :
        print "3"

    a = 1
    while True:
        print(a)
        a += 1
        if a == 3:
            break;
    print "while is break"

    for letter in 'Python':
        if letter == 'h':
            break
        print '当前字母 ：', letter
    print "good bye"