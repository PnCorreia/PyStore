# As a final project of Intro to Programming of my Computer Science course at CodeCadmy I've created this store model for small producers to sell directly to his clients online.
# This can reduce the price of essencial goods bringigng fresh produts to all.


class Store:
  # When creating an object store the name and type of products it sells must be defined
  def __init__(self, name, type):

    self.name = name
    self.type = type
    self.inventory = []
        
  def __repr__(self):
    greeting = "Welcome to {name} store. In our store we sell {type}\n".format(name = self.name, type = self.type)
    return greeting

  # To add products to the inventory a list must be passed as argument containing: product name, it's quantity and the product price
  def add_product(self, product):
    self.inventory.append(product)
    return self.inventory

  # with the today_special method all the products in the inventory are listed and the client is requested to put an order 
  def today_specials(self):
    print("Today we have fresh:")
    for list in self.inventory:
      print(list[0] + " at $" + str(list[2]) + "/kg")
    print("What's your order today?\n")

class Client:
  #To create a new client his details are required: name, surname, address and payment method.
  def __init__(self, name, surname, address, payment_method, order = ""):

    self.name = name
    self.surname = surname
    self.address = address
    self.payment_method = payment_method
    self.order = order
  
  # Printing __repr__ for the instance client will print it's details
  def __repr__(self):
    return "Client: {name} {surname}\nDelivery Address: {address}\n".format(name = self.name, surname = self.surname, address = self.address)

  # In order to allow the instance client to put an order, a list of products needs to be passed as argument  
  def place_order(self, inventory_list):
    self.order = input("List the products to add to cart: ")
    
    # Next the order string is transformed in a list of products
    order_split = self.order.split(",")

    # All the spaces before and after each string are removed
    order_strip = []
    for str in order_split:
      order_strip.append(str.strip())

    # If the products picked by the client match the ones in the store inventory a final order_list is created with the prices of each product
    order_list = []
    for str in order_strip:
      for list in inventory_list:
        if str == list[0]:
          order_list.append(list[2])
    
    # Total is the adition of all values of order_list
    total = round(sum(order_list), 2)
    
    return "\nProducts in your cart: {order}\nTotal in cart: ${total}".format(order = self.order, total = total)

  def check_out(self):

    details_confirmation = input("""Please confirm your details:
    \nFull Name: {name} {surname}
    Address: {address}
    Payment method: {payment_method}
    \nConfirm? (y/n) """.format(name = self.name, surname = self.surname, address = self.address, payment_method = self.payment_method))

    if "yes" in details_confirmation:
      print("\nYour order is going to be prepared and will be by your door step tomorrow. Thank you for your order")
    else:
      print("\nUps, something is wrong. Please check your details in the private area.")
    

# Tests   

# instance store
store_test = Store("Panda", "fresh fruits and vegetables")

print(store_test)

# adding products to the store inventory
store_test.add_product(["bananas", 10, 1.0]) 
store_test.add_product(["apples", 10, 0.89]) 
store_test.add_product(["oranges", 10, 0.99])
store_test.add_product(["lemons", 10, 0.89]) 
store_test.add_product(["strawberries", 50, 3.50]) 
store_test.add_product(["pinaple", 5, 4.99])
store_test.add_product(["pears", 10, 0.99]) 

# printing the products available 
store_test.today_specials()

# variable with the list of products available to use by the instance client in the method place_order
inventory = store_test.inventory

# instance client
client_test = Client("Patricia", "Correia", "Rua Dr Moreira Pinto, n 31, Fao", "Card n 2424242424")

# placing an order
first_order = client_test.place_order(inventory)

print(first_order)

# Check out
client_test.check_out()

