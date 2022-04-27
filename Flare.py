from flare.tools.alexa import Alexa
from flare.tools.umbrella import Umbrella
from flare.tools.whoisip import WhoisLookup
from flare.data_science.features import entropy

#https://majestic.com/reports/majestic-million
majestic = majesticMillion(limit=100000)
print(majestic.domain_in_majestic("google.com"))

#La lista actualizada solo esta disponible a traves de pago
alexa = Alexa(limit=1000000)

#https://umbrella.cisco.com/blog/cisco-umbrella-1-million
umbrellaCisco = Umbrella(limit=1000000)

print(umbrellaCisco.domain_in_umbrella('google.com'))

print (alexa.domain_in_alexa('google.com'))

whois = WhoisLookup()
print(whois.get_name_by_ip('8.8.8.8'))
print(whois.get_name_by_ip('13.68.205.253'))

print(entropy('abcdef.com'))
print(entropy('google.com'))
print(entropy('jshdksdhks4433.com'))

