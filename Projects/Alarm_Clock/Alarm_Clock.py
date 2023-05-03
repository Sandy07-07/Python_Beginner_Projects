from playsound import playsound
from datetime import datetime


# To validate the time entered by user
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"


while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

# To extract the hour,minute,seconds from the time entered
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()  # To get the  present time we create a datetime object

    current_hour = now.strftime("%I")  # It retrieves the hour in 12-hour format with leading zeros
    current_min = now.strftime("%M")  # It retrieves the minute with leading zeros
    current_sec = now.strftime("%S")  # It retrieves the second with leading zeros
    current_period = now.strftime("%p")  # It retrieves whether it is am or pm in lowercase

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    playsound("alarm_sound.mp3")  # Plays the sound which is in mp3 format
                    break
