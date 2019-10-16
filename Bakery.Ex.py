#Tyler Vasquez
#Oct 14, 2019
#Hartwick bakery list

months = int(input("Number of months the bakery was open:"))#Input number of months
candy_sold = []
cookies_sold = []

def lists():
    total=0
#creates list of candy and cookies
    for i in range(0, months):
        cookies = input(f"Amount of cookies sold each month {i+1}: ")
        cookies_sold.append(cookies)
        total = total + int(cookies)

    for x in range(0, months):
        candy = input(f"Amount of candy sold each month {x+1}: ")
        candy_sold.append(candy)
        total = total + int(candy)


lists()


def average():
    total_cookies = 0
    for cookies in cookies_sold:
        total_cookies = int(total_cookies) + int(cookies)
    cookies_avg = int(total_cookies) / int(months)

    total_candy = 0
    for candy in candy_sold:
        total_candy = int(total_candy) + int(candy)
    candy_avg = int(total_candy) / int(months)

    print(f"The average cookies sold each month is {cookies_avg}.")
    print(f"The average candy sold each month is {candy_avg}.")

average()

def minimum():
    cookies_sold.sort()
    candy_sold.sort()
    print(f"The lowest number of cookies sold was {cookies_sold[0]}")
    print(f"The lowest number of candy sold was {candy_sold[0]}")

minimum()

def maximum():
    cookies_sold.sort()
    candy_sold.sort()
    print(f"The highest number of cookies sold was {cookies_sold[months - 1]}")
    print(f"The highest number of candy sold was {candy_sold[months - 1]}")

maximum()

total_cookies = 0
total_candy = 0

for cookies in cookies_sold:
    total_cookies = int(total_cookies) + int(cookies)

for candy in candy_sold:
    total_candy = int(total_candy) + int(candy)

if total_candy > total_cookies:
    print("Candy was more popular than cookies.")

else:
    print("Cookies was more popular than candy.")
