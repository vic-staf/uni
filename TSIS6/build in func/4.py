import time
import math

num = int(input("Sample input: "))
ms = int(input("ms: "))
time.sleep(ms / 1000)
print(f"Square root of {num} after {ms} milliseconds is {math.sqrt(num)}")