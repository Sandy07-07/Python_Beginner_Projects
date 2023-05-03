import os
import time

# to take inout the time after which shutdown will occur
set_time = input("Shutdown after how many minutes :- ")
set_time = int(set_time)

print("Computer will shut down in " + str(set_time) + " Minutes")
time.sleep(set_time*60)  # To convert minutes into seconds for the sleep function
print("\n")

# To print the last message before shutdown
print("Computer will shutdown")
time.sleep(3)  # To wait 3 seconds before shutdown
os.system("shutdown /s /t 1")  # Shutdown the system
