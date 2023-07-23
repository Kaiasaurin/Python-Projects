import time
# Counts down from x
number = int(input("Enter a number: "))
count = number

while count > 0: 
    print(count)
    # How many seconds to wait before counting every number
    time.sleep(1)
    count -= 1
             # Down by 1 number every second

print("Countdown finished!🎉")
