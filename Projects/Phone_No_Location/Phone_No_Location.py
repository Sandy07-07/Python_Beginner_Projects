import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# To get the phone number from the user with the country code
number = input("Enter the phone number whose location you want to know with country code at first :- ")

# To parse the phone number
phone = phonenumbers.parse(number)

# To get the time zone of the phone number
time = timezone.time_zones_for_number(phone)

# To get the service provider of the number
car = carrier.name_for_number(phone, "en")

# To get the country name of the number
reg = geocoder.description_for_number(phone, "en")

print("Country in which the number is present :- " + reg)
print("Time Zone under which the number falls :- " + str(time))
print("The Service Provider of the number is :- " + car)
