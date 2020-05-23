#Kilometer Converter
#Write a program tat asks the user to enter a distance in kilometers, then converts that distance to miles
#is as follows: Miles = Kilometers x 0.6214

def main():
    kilometers = float(input('Please enter the number in kilometers: '))
    miles = kilometers * 0.6214
    print('The distance in miles is', miles)
    
main()
