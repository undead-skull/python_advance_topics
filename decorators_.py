""" Decorators"""

def func_dec(f):
    def wrapper(x):
        print("started func1")
        f(x)
        print("Func1 Ended")
    
    return wrapper

@func_dec
def func1(x):
    print(x)

@func_dec
def func2(x):
    print(x)

func1(5)
func2(2)
    
 
 
"""execution time decorator """



import datetime



def timer_fun(f):
    def timer_wrapper(x):
        start = datetime.datetime.now()
        f(x)
        end = datetime.datetime.now()
        print(start,end)
        print(f"total execution time :{end-start}")

    return timer_wrapper

@timer_fun
def func1(x):
    for _ in range(x):
        pass 

func1(10000000)