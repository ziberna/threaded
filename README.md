@threaded
=========

__@threaded__ is a Python decorator for easy threading. It comes in handy when
you have a function that you want to run in a separate thread.

There are four decorators, actually...

### threaded.inherit

Inherits daemon property from the current thread.

### threaded.daemon

The resulting thread is a daemon thread.

### threaded.nondaemon

The resulting thread is a non-daemon thread.

### threaded.opposite

The thread's daemon property is opposite than that of the current thread.


Example
-------

```python
import threaded
import time


# Replace with threaded.daemon and run again. Notice any changes?
@threaded.inherit
def print_odd_numbers(limit, interval):
    number = 1
    while number < limit:
        print('\t', number)
        number += 2
        time.sleep(interval)

def print_even_numbers(limit, interval):
    number = 0
    while number < limit:
        print(number)
        number += 2
        time.sleep(interval)

print('MAIN\t', '2ND THREAD')
print_odd_numbers(30, 0.5)  # will be run in 2ND thread
print_even_numbers(30, 0.25)  # will be run in MAIN thread
```
