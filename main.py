from multiprocessing import Process
from threading import Thread
import json


def printer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return inner

@printer
def numbers(s):
    with open('numbers.txt', 'w') as f:
        p = 0
        for i in s:
            if i.isdigit():
                p += int(i)
        f.write(str(p))
    return p

@printer
def uppers(s):
    with open('upper.txt', 'w') as f:
        data = []
        for i in s:
            if i.isupper():
                data.append(i)
                f.write(f'{i}\n')
    return data

@printer
def chars(s):
    with open('chars.json', 'w') as f:
        data = []
        this_dict = dict()
        for i in s:
            count_s = s.count(i)
            this_dict.update({i: count_s})
        data.append(this_dict)
        json.dump(data, f, indent=4)
    return data

if __name__ == '__main__':
    string = input('Enter a string: ')
    # p1 = Process(target=numbers, args=(string, ))
    # p2 = Process(target=uppers, args=(string, ))
    # p3 = Process(target=chars, args=(string, ))
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    th1 = Thread(target=numbers, args=(string,))
    th2 = Thread(target=uppers, args=(string,))
    th3 = Thread(target=chars, args=(string,))
    th1.start()
    th2.start()
    th3.start()
    th1.join()
    th2.join()
    th3.join()
    # print(numbers(string))
    # print(uppers(string))
    # print(chars(string))

