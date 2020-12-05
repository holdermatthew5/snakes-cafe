intro = [
    "**************************************",
    "**    Welcome to the Snakes Cafe!   **",
    "**    Please see our menu below.    **",
    "**",
    "** To quit at any time, type 'quit' **",
    "**************************************",
]

prompt = [
  "***********************************",
  "** What would you like to order? **",
  "***********************************",
]

appetizers = {
  "name": "Appetizers",
  "dash": "----------",
  "one": "Wings",
  "two": "Cookies",
  "three": "Spring Rolls",
}

entrees = {
  "name": "Entrees",
  "dash": "-------",
  "one": "Salmon",
  "two": "Steak",
  "three": "Meat Tornado",
  "four": "A Literal Garden",
}

desserts = {
  "name": "Desserts",
  "dash": "--------",
  "one": "Ice Cream",
  "two": "Cake",
  "three": "Pie",
}

drinks = {
  "name": "drinks",
  "dash": "------",
  "one": "Coffee",
  "two": "Tea",
  "three": "Unicorn Tears",
}

orders = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}

j = 0

for i in intro:
    print(i)
print("")

for i in appetizers:
    print(appetizers[i])
print("")

for i in entrees:
    print(entrees[i])
print("")

for i in desserts:
    print(desserts[i])
print("")

for i in drinks:
    print(drinks[i])
print("")

while (j < 1):
    for i in prompt:
        print(i)
    print("")

    user_input = input(">")
    print("")

    if (user_input == "quit"):
        break

    if (orders[user_input] == 0):
        count = orders[user_input] + 1

        print(str(count) + " order of " + user_input + " has been added.")
        print("")
    else:
        count = orders[user_input] + 1

        print(str(count) + " orders of " + user_input + "have been added.")
        print("")

    orders[user_input] += 1

print("Your order:")
for i in orders:
    if (orders[i] > 0):
      print(i + ": " + str(orders[i]))