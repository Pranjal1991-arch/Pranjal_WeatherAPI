import time

print("Program started")
start_time = time.time()
for i in range(1, 1000001, 1):
    print(i)
# i = 1
# while i <= 1000000:
#    print(i)
#    i = i + 1

print((time.time() - start_time))
