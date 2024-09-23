# Author = Gerard Keohane
# Purpose = December Assignment

# Opening title/ Creating variables

# Formatting Variables
title = "Make a Record Studios"
space = " "
band_members = ""
heading_1 = "Name"
heading_2 = "Instrument"
heading_3 = "Rate"
sentence_1 = "Daily Rate applied - studio "
sentence_2 = "Daily Rate applied - session musicians"
sentence_3 = "Total Studio Cost"
sentence_4 = "Total Session Musician Cost"
sentence_5 = "Total Payment to Studio"
sentence_6 = "Band Musician Cost "
sentence_7 = "Total Costs"
# Numbers/Accumulators
pay_options = ("1", "2", "3")
rates = 0
rate_accu = 0
max_rates = 0
max_rates_string = ""
booking_accu = ""
session_musicians = 0
day_option_1 = (2, 3, 4)
day_option_2 = (5, 6, 7, 8)
# Heading
print(f"{space:<5}{title:<25}{space:<10}")
print('-' * 31)

# Main body

# Introduction questions
band_name = str(input("What is your band's name? "))

email = str(input("What is your email address? "))
while "@" and "." not in email:
    # I use this as a validator to make sure "@" and "." were both inputted. If they aren't the question will repeat.
    email = str(input("What is your email address? "))

date = input("What start date are you looking for (dd/mm/yyyy)? ")
while "/" not in date:
    # I use this as a validator to make sure "/" are included in the answer.If it isn't the question will repeat.
    date = (input("What start date are you looking for (dd/mm/yyyy)? "))

number_of_members = int(input(f"How many members are there in {band_name}? A max of 8 is allowed. "))
while number_of_members > 8:
    # # I use this as a validator to ensure the number of members doesn't exceed 8.If it does the question will repeat.
    number_of_members = int(input(f"How many members are there in {band_name}? A max of 8 is allowed. "))

days = int(input("How many days? "))
print()

#  Band member specifics

for i in range(number_of_members):
    # This asks for each band members name, instrument and rate. It loops until the number of members is reached.
    band_members = str(input(f"Enter band member #{i+1}s name: "))
    instruments = str(input(f"Enter {band_members}'s instrument: "))
    rates = int(input(f"Enter {band_members}'s rate: "))
    output = open(f"{band_name}_{band_members}.txt", "w")
    # The output here is used to send the inputs to a text file.
    print(f"{date}", f"  {days} days", f"    €{rates * days:,.2f}", file=output)
    output.close()
    booking_accu += f"{band_members:<20}{instruments:<20}€{rates:>7,.2f}\n"
    # This variable prints the inputted values later.
    rate_accu += rates      # This accumulates all rates.
    if rates > max_rates:
        # This is used to find the highest rate.
        max_rates = rates
        max_rates_string = f"{band_members}"    # This is used to store the name with the highest rate.
    i += 1

# Session musicians/ Payment method

if number_of_members < 8:
    print(f"There is room for {8 - number_of_members} session musicians.")
    # This is used to ask the user how many session musicians they want depending on how many musicians they have.
    print()
    session_musicians = int(input("How many do you want? "))
    while session_musicians > 8:
        session_musicians = int(input("How many do you want? "))

print("Will you pay by")
print("1. Credit card (5% levy)")
print("2. Cash (5% discount)")
print("3. Online")
# This is all used to select a payment option from the three options presented.
payment_option = input("=>: ")
while payment_option not in pay_options:
    payment_option = input("=>: ")

# Booking table

print(f"Booking for: {band_name} - {date}")
print('-' * 48)
print(f"{heading_1:<20}{heading_2:<23}{heading_3}")
print('-' * 48)

print(booking_accu)

# Input facts, this section explains who's paid the most, the average rate and the number of session musicians.

print(f"The highest paid band member is {max_rates_string} on €{max_rates:,.2f}.")
print(f"The average daily rate for a band member is €{rate_accu / number_of_members}.")
print(f"There are {session_musicians} session musicians booked.")
print()

# Payment totals

if payment_option == "1":
    print("Payment is by Credit card.")
elif payment_option == "2":
    print("Payment is by Cash.")
elif payment_option == "3":
    print("Payment is made Online.")

print(f"Number of Days {days}.")
# The studios cost depends on the number of days selected, I used tuples for this.
studio_costs = 0
if days == 1:
    studio_costs += 300
elif days in day_option_1:
    studio_costs += 250
elif days in day_option_2:
    studio_costs += 220
elif days >= 9:
    studio_costs += 200
# The studio costs also depends on the payment options due to discount etc.
if studio_costs == 300 and payment_option == "1":
    studio_costs = 300 + (300 * 0.05)
if studio_costs == 300 and payment_option == "2":
    studio_costs = 300 - (300 * 0.05)
if studio_costs == 250 and payment_option == "1":
    studio_costs = 250 + (250 * 0.05)
if studio_costs == 250 and payment_option == "2":
    studio_costs = 250 - (250 * 0.05)
if studio_costs == 220 and payment_option == "1":
    studio_costs = 220 + (220 * 0.05)
if studio_costs == 220 and payment_option == "2":
    studio_costs = 220 - (220 * 0.05)
if studio_costs == 200 and payment_option == "1":
    studio_costs = 200 + (200 * 0.05)
if studio_costs == 200 and payment_option == "2":
    studio_costs = 200 - (200 * 0.05)

print(f"{sentence_1:40} €{studio_costs:>9,.2f}")

musicians_costs = session_musicians * 120
# The musician costs are also affected by what payment option is selected.
if payment_option == "1":
    musicians_costs = (session_musicians * 120 + (session_musicians * 120) * 0.05)
elif payment_option == "2":
    musicians_costs = (session_musicians * 120 - (session_musicians * 120) * 0.05)
print(f"{sentence_2:40} €{musicians_costs:>9,.2f}")
print()
# The rest of the code is used for the endgame of getting to total costs.
total_studio_costs = studio_costs * days
print(f"{sentence_3:40} €{total_studio_costs:>9,.2f}")

total_session_musician_cost = musicians_costs * session_musicians
print(f"{sentence_4:40} €{total_session_musician_cost:>9,.2f}")

print(f"{space * 41}{'=' * 10}")
print()

total_payment_to_studio = total_studio_costs + total_session_musician_cost
print(f"{sentence_5:40} €{total_payment_to_studio:>9,.2f}")

band_musician_cost = rate_accu * days
print(f"{sentence_6:40} €{band_musician_cost:>9,.2f}")

print(f"{space * 41}{'=' * 10}")
print()

total_costs = total_payment_to_studio + band_musician_cost
print(f"{sentence_7:40} €{total_costs:>9,.2f}")
print()

print("The payment details for each band member has been written to their individual files.")
