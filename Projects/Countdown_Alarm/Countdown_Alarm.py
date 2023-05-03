from playsound import playsound
import time


def alarm(total_seconds):
    time_elapsed = 0

    while time_elapsed < total_seconds:
        time.sleep(1)  # To wait for 1 second when the function is called
        time_elapsed += 1

        time_left = total_seconds - time_elapsed
        minutes_left = time_left // 60  # Calculate the total minutes left
        seconds_left = time_left % 60  # To calculate the total seconds left

        print(f"Alarm will sound in {minutes_left:02d}:{seconds_left:02d}")  # To display the left time

    playsound("alarm_sound.mp3")  # To play the alarm sound


minutes = int(input("Enter the minutes to wait for alarm :- "))
seconds = int(input("Enter the seconds to wait for alarm :- "))
total_seconds = minutes*60 + seconds  # To convert the total time into seconds
alarm(total_seconds)
