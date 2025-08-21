import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+916363825966")
phone_number2 = phonenumbers.parse("+916361860351")
phone_number3 = phonenumbers.parse("+917618765910")
phone_number4 = phonenumbers.parse("+917892388211")

print("\nphone number location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))

