# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")


def print_message():
  return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def get_size():
  res = input("What size drink would you like?")
  if(res == 'a'):
   return 'small'
  if(res == 'b'):
    return 'medium'
  if(res == 'c'):
    return 'large'
  else:
    print_message()
    return get_size()

# Call coffee_bot()!
coffee_bot()

final = "Alright, that's a {size} {drink_type}!".format(size = get_size(), drink_type = get_drink_type())

print(final)

print("Thanks, {name}! Your drink will be ready shortly.".format(name = input("Can I get your name please?")))