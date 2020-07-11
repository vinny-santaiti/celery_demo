from .tasks import add
import time


def write_output(result):
    print('Task finished? {}'.format(result.ready()))
    print('Task result: {}'.format(result.result))


if __name__ == '__main__':
    result = add.delay(1,2)
    write_output(result)
    time.sleep(6)
    write_output(result)