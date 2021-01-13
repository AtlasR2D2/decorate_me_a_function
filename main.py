import time


def speed_calc_decorator(function):
    start_time = time.time()
    function()
    end_time = time.time()
    def time_taken():
        return end_time - start_time
    print(f"{function.__name__} run speed: {time_taken()}s")
    return time_taken
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


#-------------------------------------
# Compare the times

print(f"fast_function is {slow_function()/fast_function()} times faster than slow_function")
