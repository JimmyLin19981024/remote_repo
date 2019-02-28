import dis
import time
import math


def timeit(func):
    def timed(*arg, **kwarg):
        start = time.time()
        result = func(*arg, **kwarg)
        end = time.time()
        print(f'function "{func.__name__}" takes {end - start} to run.')
        return result
    return timed


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


head = Node(4)
nodeB = Node(3)
nodeC = Node(2)
nodeD = Node(1)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD


def countNodes(head):
    count = 1
    while head.next != None:
        count += 1
        head = head.next
    return count


print(countNodes(head))


def test2():
    print("testing!")

def test3():
    print("change 2!")
