### Task 1

# import time
#
# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970
#
#
# # Write your code below 👇
# def speed_calc_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} run speed: {end_time - start_time}s")
#         return result
#
#     return wrapper
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i
#
#
# fast_function()
# slow_function()


### Task 2
#
# def respect(maybe):
#     def congrats():
#         return "Congrats bro"
#     def insult():
#         return "You're silly!"
#     if maybe == "yes":
#         return congrats()
#     else:
#         return insult
#
# respect = respect("maybe")
# print(respect)

### Task 3
#
# def startstop(func):
#     def wrapper():
#         print("Starting")
#         func()
#         print("Finished")
#     return wrapper
# #@startstop #or just use this decorator
# def roll():
#     print("Rolling on the floor laughing")
# roll = startstop(roll)
#
# roll() # this is another way to do it

# Task 4 Czas wykonania

# import time
#
#
# def measuretime(func):
#     def wrapper(*args, **kwargs):  # Handle arbitrary arguments
#         starttime = time.perf_counter()
#         result = func(*args, **kwargs)
#         endtime = time.perf_counter()
#         print(f"time needed: {endtime - starttime} seconds")
#         return result
#     return wrapper
#
# @measuretime
# def wastetime():
#     sum([i ** 2 for i in range(1000000)])
#
# result = wastetime()
# print(result)


# Task 5
# slowing down the code

# import time
#
# def sleep(func):
#     def wrapper():
#         time.sleep(10)
#         return func()
#     return wrapper
#
# @sleep
# def wakeup():
#     print("Get up ducker!")
# wakeup()


# Task 6 - Testowanie i debugowanie

def debug(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        return func() #without it i only print ""
    return wrapper

@debug
def scare():
    print("Boo!")

scare()