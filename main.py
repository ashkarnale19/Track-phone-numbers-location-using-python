import phonenumbers
from phonenumbers import geocoder
number="" #enter the number 

country=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(country,"en"))

from phonenumbers import carrier
service_no=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_no,"en"))

