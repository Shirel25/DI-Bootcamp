import random

def get_season(month):
    if month in [12, 1, 2]:   # December, January, February
        return "winter"
    elif month in [3, 4, 5]:  # March, April, May
        return "spring"
    elif month in [6, 7, 8]:  # June, July, August
        return "summer"
    else:  # September, October, November
        return "fall"


def get_random_temp(season):
    if season == 'winter':
        # temp = random.randint(-10, 16)
        temp = round(random.uniform(-10, 16), 1)
    elif season == 'spring':
        # temp = random.randint(11, 24)
        temp = round(random.uniform(11, 24), 1)
    elif season == 'fall':
        # temp = random.randint(6, 20)
        temp = round(random.uniform(6, 20), 1)
    else: # Summer
        # temp = random.randint(20, 40)
        temp = round(random.uniform(20, 40), 1)
    return temp


def main():
    # season = input("Enter the season (winter, spring, summer, fall): ").lower().strip()

    while True:
        try:
            month = int(input("Enter the number of the month (1 = January, 12 = December): "))
            if 1 <= month <= 12:
                break  # Valid input
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    season = get_season(month)
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("Mild weather! A light jacket should be enough.")
    elif 23 <= temp < 32:
        print("It's warm outside! Enjoy the nice weather.")
    else:
        print("It's really hot! Stay hydrated and wear sunscreen.")
        


if __name__ == '__main__':
    main()