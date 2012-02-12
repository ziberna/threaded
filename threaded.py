#=============================================================================
# threaded, a Python decorator for easy threading
# Copyright (C) 2012  Jure Ziberna
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#=============================================================================

import threading
import time


def threaded(function, daemon):
    """
    Turns given function into a threaded function.
    """
    name = '%s-%d' % (function.__name__, threading.active_count())
    def function_wrapper(*args, **kwargs):
        if '_delay' in kwargs:
            func = delayer(function, kwargs['_delay'])
            del kwargs['_delay']
        else:
            func = function
        thread = threading.Thread(target=func, name=name, args=args, kwargs=kwargs)
        thread.daemon = daemon
        thread.start()
        
    function_wrapper.__name__ = function.__name__
    return function_wrapper

def delayer(function, seconds):
    """
    Makes the actual call to the function delayed by given float number of
    seconds. Returns a wrapped function.
    """
    def delay_wrapper(*args, **kwargs):
        time.sleep(seconds)
        function(*args, **kwargs)
    
    delay_wrapper.__name__ = function.__name__
    return delay_wrapper


def inherit(function):
    """
    Turns a function into a threaded function.
    Inherits daemon property from the current thread.
    """
    daemon = threading.current_thread().daemon
    return threaded(function, daemon)

def daemon(function):
    """
    Turns a function into a threaded function.
    The thread is a daemon thread.
    """
    return threaded(function, True)

def nondaemon(function):
    """
    Turns a function into a threaded function.
    The thread is a non-daemon thread.
    """
    return threaded(function, False)

def opposite(function):
    """
    Turns a function into a threaded function.
    The thread's daemon property is opposite than that of the current thread.
    """
    daemon = not threading.current_thread().daemon
    return threaded(function, daemon)

