file = open("K_or_M survey.txt", "w+")


print("Test yourself! Are you team Ketchup or team Mustard?\n")

print("Coca-Colla [A] or Pepsi [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("K")

if choice == 'b':
    file.write("M")

print("Pastries [A] or Bread [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("K")

if choice == 'b':
    file.write("M")

print("Pizza [A] or Pasta [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("M")

if choice == 'b':
    file.write("K")

print("Potatoes [A] or Rice [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("K")

if choice == 'b':
    file.write("M")

print("Vegetables [A] or Fruit [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("M")

if choice == 'b':
    file.write("K")

print("Bacon [A] or Cheese [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("M")

if choice == 'b':
    file.write("K")

print("Sweet [A] or Sour [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("M")

if choice == 'b':
    file.write("K")

print("Sweet [A] or Salty [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("K")

if choice == 'b':
    file.write("M")

print("Meat [A] or Tofu [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("K")

if choice == 'b':
    file.write("M")

print("Pancakes [A] or Waffles [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("M")

if choice == 'b':
    file.write("K")

print("Milk [A] or Juice [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("M")

if choice == 'b':
    file.write("K")

print("Tea [A] or Water [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("M")

if choice == 'b':
    file.write("K")

print("Hot-Dog [A] or Burger [B]?")
choice = input("Choose an option: \n")
if choice == 'a':
    file.write("K")

if choice == 'b':
    file.write("M")

try:
    file = open("K_or_M survey.txt", "r+")
    content = file.read()

    if content.count('K') > content.count('M'):
        file.write("\nYour result is KETCHUP!")
        print("\nThank you for completed survey! Check your results in created file.")

    if content.count('K') < content.count('M'):
        file.write("\nYour result is MUSTARD!")
        print("\nThank you for completed survey! Check your results in created file.")

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("You do not have permissions for this activity.")
