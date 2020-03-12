import random
from list_of_countries import COUNTRIES

def main():
     countries = list(COUNTRIES.keys())
     guess = random.choice(countries)
     capital = input('What is the capital of '+ guess +'?')

     if capital.lower() == COUNTRIES[guess]:
         print('well done')
     else:
         print('wrong! it is '+COUNTRIES[guess] )

main()