import time


start_time = time.time()
print("Printed immediately.", start_time)
time.sleep(2.4)
print("Printed after 2.4 seconds.")
print("--- %s seconds ---" % (time.time() - start_time))