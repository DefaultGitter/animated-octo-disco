from threading import Thread
import time


def t_func1():
    for i in range(10):
        print('#', end=' | ')
        time.sleep(0.5)
    # print()


def t_func2():
    for i in range(10):
        print('*', end=' | ')
        time.sleep(0.5)


# Thread(target=t_func2).start()
th1 = Thread(target=t_func2)
th1.start()
th1.join()

t_func1()
# t_func2()
