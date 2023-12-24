import phonenumbers

#kodu çalıştırmak için phonenumbers kütüphanesi indirilmeli

number1 = '+905533684788'

from phonenumbers import geocoder
number = phonenumbers.parse(number1)
print(geocoder.description_for_number(number,'tr'))

from phonenumbers import carrier
number = phonenumbers.parse(number1)
print(carrier.name_for_number(number,'tr'))

