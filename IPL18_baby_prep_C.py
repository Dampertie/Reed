

ounces_per_pound = 16

#-- defines
def poop(current_weight):
    current_weight -= 5
    print("The baby pooped! -5 oz")
    return current_weight


def pee(current_weight):
    current_weight -= 4
    print("The baby peed! -4 oz")
    return current_weight


def eat(current_weight, eat_count):
    current_weight += 11
    eat_count += 1
    print("The baby ate! +11 oz")

    if eat_count % 3 == 0:
        current_weight = poop(current_weight)

    return current_weight, eat_count


def drink(current_weight, drink_count):
    current_weight += 8
    drink_count += 1
    print("The baby drank! +8 oz")

    if drink_count % 3 == 0:
        current_weight = pee(current_weight)

    return current_weight, drink_count


def cry():
    print("The baby is crying!")
    return "Sad"


def sleep():
    print("The baby is sleeping!")
    return "Sleeping"


def display_status(baby_name, current_weight, mood, eat_count, drink_count):
    weight_in_pounds = current_weight / ounces_per_pound

    print("\nYour Baby stats!!!")
    print("Name:", baby_name)
    print("Current weight:", current_weight, "ounces")
    print("Weight in pounds:", weight_in_pounds)
    print("Mood:", mood)
    print("Times eaten:", eat_count)
    print("Times drank:", drink_count)
    print()



action = "none"

baby_name = input("What is your baby's name? ")
baby_birthdate = input("What is your baby's birthdate? (MM/DD/YYYY) ")
current_weight = int(input("What is your baby's weight in ounces? "))
baby_height = float(input("What is your baby's height in inches? "))

eat_count = 0
drink_count = 0
mood = "DEFAULT_MOOD"

while action != "home":
    action = input(
        "What would you like to do with your baby? "
        "(feed, drink, sleep, cry, status, home) "
    ).lower()

    if action == "cry":
        mood = cry()

    elif action == "sleep":
        mood = sleep()

    elif action == "feed":
        current_weight, eat_count = eat(current_weight, eat_count)
        mood = "Happy"

    elif action == "drink":
        current_weight, drink_count = drink(current_weight, drink_count)
        mood = "Chill"

    elif action == "status":
        display_status(
            baby_name, current_weight, mood, eat_count, drink_count
        )
   
    else:
        print("Invalid action. Please choose feed, drink, sleep, cry, status, or home.")

# Final status
display_status(baby_name, current_weight, mood, eat_count, drink_count)
