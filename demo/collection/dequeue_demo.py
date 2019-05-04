import collections
import threading
import time

rotate_deque = collections.deque(range(10))
print(rotate_deque)
rotate_deque.rotate(2)
print(rotate_deque)
rotate_deque.rotate(-4)
print(rotate_deque)

number_deque = collections.deque(range(7))


def consumer(direction: str, number_source):
    while True:
        try:
            next_number = number_source()
        except IndexError as e:
            print(e)
            break
        else:
            print('direction: {:>10}, next:{}'.format(direction, next_number))
            time.sleep(1)

    print('direction: {:>10} down.'.format(direction))
    return


left_consumer = threading.Thread(target=consumer, args=('Left', number_deque.popleft))
right_consumer = threading.Thread(target=consumer, args=('Right', number_deque.pop))

left_consumer.start()
right_consumer.start()

left_consumer.join()
right_consumer.join()
