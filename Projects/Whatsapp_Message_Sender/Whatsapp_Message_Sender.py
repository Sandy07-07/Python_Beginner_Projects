import pywhatkit

# To send Whatsapp message to a specific number
receiver = input("Enter the number of the receiver with +91 :- ")
msg = input("Enter the message tobe send to the receiver :- ")
hr_time = int(input("Enter the Hour time to send the message in 24 hr format :- "))
min_time = int(input("Enter the Minute time to send the message :- "))
pywhatkit.sendwhatmsg(receiver, msg, hr_time, min_time)

# To send Whatsapp message to a specific number but close the tab after that
close_time = int(input("Enter the time after which tab will be closed :- "))
pywhatkit.sendwhatmsg(receiver, msg, hr_time, min_time, 15, True, close_time)

# To send a Whatsapp message of image to a specific number
caption = input("Enter the caption to include with the image :- ")
pywhatkit.sendwhats_image(receiver, "sending_image.jpg", caption)

# To send a Whatsapp message of image with caption to a specific number
pywhatkit.sendwhats_image(receiver, "sending_image.jpg", )

# To send a Whatsapp message to a specified group
group_name = input("Enter the name of the group to send the message :- ")
pywhatkit.sendwhatmsg_to_group(group_name, msg, hr_time, min_time)

# To play a YouTube video on the topic specified
topic = input("Enter the Topic to play on Youtube :- ")
pywhatkit.playonyt(topic)

# To search on Google the specified topic
search = input("Enter the Topic to search on Google :- ")
pywhatkit.search(search)
