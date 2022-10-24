# -*- coding: utf-8 -*-
# @Time : 2022/10/21 12:34
# @Author : Xu Bai
# @Email : 1373953675@qq.com
# @File : p1.py
# @Desc : ...
'''
请使用Python多进程实现10个生产者进程和10个消费者进程相互通信、协作完成一个计算1000000个位于[1, 100]区间内的随机整数之和的任务。
要求使用生产者和消费者设计模式，包含进程通信；
写文档说明设计、原理、思路和细节；
'''
import random
from multiprocessing import Process, JoinableQueue, Manager
import time
from functools import reduce
manager = Manager()
return_list = manager.list()



def add(x, y):  # 两数相加
    return x + y


num = [random.randint(1, 100) for i in range(1000000)]
sum1 = reduce(add, num)  # 计算列表和：1+2+3+4+5


# 生产者方法
def producer(q, name, food):
    print("进程%s 生产了 %s" % (name, food))
    # 把生产的任务放入到队列中
    q.put(food)
    q.join()  # 等消费者把自己放入队列的所有元素取完之后才结束


# 消费者方法
def consumer(q, name):
    while True:
        res = q.get()
        if res is None: break
        sum1 = reduce(add, res)
        print("%s 计算结果 %s" % (name, sum1))
        q.task_done()  # 发送信号给q.join(),表示已经从队列中取走一个值并处理完毕了
        return sum1


if __name__ == "__main__":
    # q = Queue()
    q = JoinableQueue()
    # 创建生产者
    p1 = Process(target=producer, args=(q, "p1", [1, 2, 3]))
    p2 = Process(target=producer, args=(q, "p2", [4, 5, 6]))
    # 创建消费者
    c1 = Process(target=consumer, args=(q, "c1",return_list),)
    c2 = Process(target=consumer, args=(q, "c2",return_list))
    c3 = Process(target=consumer, args=(q, "c3",return_list))

    c1.daemon = True
    c2.daemon = True
    c3.daemon = True

    p_l = [p1, p2, c1, c2, c3]
    for p in p_l:
        p.start()

    p1.join()
    p2.join()
    # 1.主进程等待p1,p2进程结束才继续执行
    # 2.由于q.join()的存在,生产者只有等队列中的元素被消费完才会结束
    # 3.生产者结束了,就代表消费者已经消费完了,也可以结束了,所以可以把消费者设置为守护进程(随着主进程的退出而退出)

    print("主进程")
