# Question 1

# def question1():
#     name = input("Enter your name : ")
#     name = name.strip().title()
#     billamnt = float(input("Enter bill price : "))
#     person = int(input("Enter the total person"))
#     eachquantry = billamnt/person
#     print(f"Hello {name} ! your bill amnt is {billamnt:.2f}Rs and each person get {eachquantry:.2f}Rs Quantry")

# question1()


# Question 2

# def questions2():
#     price = float(input("Enter Billing Price : "))
#     if price >= 1000:
#         member_input = input("Enter True if you are member Other wise enter false : ").strip().lower()
#         coupon_input = input("Enter True if you have coupon Other wise enter false : ").strip().lower()

#         member = (member_input == 'true')
#         coupon = (coupon_input == 'true')

#         if member and coupon:
#             price = round((price * 0.80) - 50, 2)
#             print(f"your total bill is {price} because you are member and you have coupon")
#         elif member or coupon:
#             price = round((price * 0.90) - 20, 2)
#             print(f"your total bill is {price} because you are either member or you have coupon")
#         else:
#             price = round(price * 0.90, 2)
#             print(f"your total bill is {price} because you are not member and you have not coupon")
#     elif 1 <= price <= 999:
#         price = round(price * 0.90, 2)
#         print(f"Your total bill is {price} (10% discount applied).")
#     elif price <= 0:
#             print("You entered 0 or a negative number, which is not acceptable.")
#     else:
#         return

# questions2()

# question 3


# def question3():
#     # 1. Get Inputs safely (use .lower() on the 3D check so "true" or "True" both work)
#     age = int(input("Enter your Age : "))
#     time_of_day = input("Enter time of day afternoon or evening : ").strip().lower()
#     view_input = input("Enter True if you go with 3D wise enter false : ").strip().lower()
    
#     is_3d = (view_input == 'true')
    
#     # 2. STARTING STATE
#     price = 12
    
#     # 3. STEP 1: Apply Age Rules (Overrides the starting price)
#     if age < 12:
#         price = 8
#     elif age >= 65:
#         price = 9
        
#     # 4. STEP 2: Apply Time Rules (Modifies the current price)
#     if time_of_day == "afternoon":
#         price -= 2
        
#     # 5. STEP 3: Apply 3D Rules (Modifies the current price)
#     if is_3d: # This is the same as writing 'if is_3d == True:'
#         price += 3
        
#     # 6. Print EXACTLY ONCE at the very end
#     print(f"Your ticket price is {price} RS")

# # Run the function
# question3()


# question 4

# def question4():
#     # 1. get inputs
#     distance = float(input("Enter the distance : "))
#     weather = input("Enter the current weather : ").strip().lower()
#     rush = input("Enter True id its rush hour otherwise enter False : ").strip().lower()

#     # variables
#     is_rushHour = (rush == 'true')
#     base_far = 5
#     total_fare = float(5 + (distance * 2))

#     # apply distance rules
#     if weather == "rainy":
#         total_fare += 3
#     elif weather == "snowy":
#         total_fare *=  1.2
#     else:
#         total_fare += 0

#     # apply rush hour rules
#     if is_rushHour:
#         total_fare *= 1.5

#     print(f"your ride cost is {total_fare:.2f} rs because you travel {distance} km \n and the surrent wather is {weather} and there is rush hour {is_rushHour}")
    

# question4()



# question 5

# def question5():
#     # variables
#     current_position = 0
#     jump_count = 0
    
#     target_distance = float(input("Enter the target distance : "))
#     jump_length = float(input("Enter the jump length : "))

#     # counting
#     while current_position < target_distance:
#         current_position += jump_length
#         jump_count += 1 

#     # conditions
#     if jump_count in range (1,6):
#         print("you won gold medal")
#     elif jump_count in range(6 , 11):
#         print("you won silver medal")
#     else:
#         print("you won bronze medal")

# question5()

# question 6

# def question6():

#     # varibales
#     turns = 0
#     current_heat = int(input("Enter the current heat : "))
#     target_heat = int(input("Enter the target heat : "))

#     # loop with conditions adn addition
#     while current_heat < target_heat:
#         if(current_heat % 2 == 0):
#             current_heat += 2
#         else:
#             current_heat += 3

#         turns += 1

#     # output conditions
#     if turns == 0:
#         print("Already at to the target heat !")
#     elif turns in range(1 , 6):
#         print("fast brew !")
#     elif turns in range(6 , 11):
#         print("normal brew !")
#     else:
#         print("slow brew")

# question6()



# question 7

# def question7():
#     while True:
#         command = input("Enter the command (Scan or Exit) : ").strip().lower()
#         if command == "scan":
#             number = int(input("How many lockers do you want to scan ? : "))
#             for i in range(1 , number+1):
#                 if(i % 3 == 0):
#                     continue
#                 else:
#                     print(f"Scanning locker {i}")
#         elif command == "exit":
#             print("Shutting Down...! ")
#             break
#         else:
#             print("invalid command , try again....!")


# question7()



# question 8
# def question8():
#     # variables
#     packaged = 0
#     defects = 0
#     item_number = int(input("How many items are on the belt ? : "))

#     # loop
#     for i in range(1 , item_number+1):
#         if(i % 8 == 0):
#             print(f"power failure at item {i} ! line stopped")
#             break
#         elif(i % 4 == 0):
#             print(f"Item {i} is defective")
#             defects += 1
#             continue
#         else:
#             print(f"Item {i} is packaged")
#             packaged += 1

#     print(f"total number of packaged : {packaged} \ntotal number of defects : {defects}")

# question8()



# # question 9

# def question9():
#     # variables
#     cargo_weight = 0
#     max_capacity = 100

#     # main menu loop
#     while True:
#         # command input
#         command = input("Enter the command (load , check , launch) : ").strip().lower()

#         # conditions
#         if(command == "load"):
#             crates_to_load = int(input("How many crates to load ? : "))
#             for i in range(1 , crates_to_load+1):
#                 if(cargo_weight + 25 > max_capacity):
#                     print("capacity reached! cannot load more...")
#                     break
#                 elif(i % 3 == 0):
#                     print(f"Crate {i} is fragile. Skipping...")
#                     continue
#                 elif(cargo_weight != max_capacity and i % 3 != 0):
#                     cargo_weight += 25
#                     print(f"Loaded crate : {i}.\ntotal weight : {cargo_weight}")
#         elif(command == "check"):
#             print(f"current carrgo weight is : {cargo_weight}")
#             continue
#         elif(command == "launch"):
#             if(cargo_weight == 0):
#                 print("Cannot launch an empty ship! Load cargo first.")
#                 continue
#             else:
#                 print(f"your ship is launching and your cargo weight is : {cargo_weight}...")
#                 break
#         elif(command == "exit"):
#             break
#         else:
#             print("enter the valid command")
#             continue

# question9()


# question 10
# def question10():
#     spy_data = {
#     "Agent 007": "Active",
#     "Agent 009": "Captured",
#     "Agent 042": "Active",
#     "Agent 088": "Retired"
# }

#     for i in spy_data:
#         if(spy_data[i] == "Active"):
#             print(f"{i} is currently on a mission")
#         elif(spy_data[i] == "Captured"):
#             print(f"ALERT : {i} needs rescue...!")
#         else:
#             print(f"{i} is enjoying a vacation")

# question10()


# question 11
# def question11():
#     racers = ["Mario", "Luigi", "Bowser", "Yoshi", "Toad"]

#     for i in range(len(racers)):
#         if(i == 0):
#             print(f"1st Place : {racers[i]} wins the GOLD medal!")
#         elif(i == 1):
#             print(f"2nd Place : {racers[i]} wins the SILVER medal!")
#         elif(i == 2):
#             print(f"3rd Place : {racers[i]} wins the BRONZE medal!")
#         else:
#             print(f"{i+1}th place : {racers[i]} gets a participation trophy")


# question11()


# # question 12
# def question12():

#     health = 100
#     gold = 0
#     # The player's journey
#     path_taken = ["Hallway", "Armory", "Dungeon", "Vault", "Garden"]
#     maze_rooms = {
#         "Hallway": "Empty",
#         "Armory": "Weapon",
#         "Dungeon": "Monster",
#         "Vault": "Gold",
#         "Garden": "Monster"
#         }

#     for i in range(len(path_taken)):
        

#         current_room = path_taken[i]
#         hidden_item = maze_rooms[current_room]
        
#         if(hidden_item == "Empty"):
#             print(f"step {i+1} : room is empty")
#         elif(hidden_item == "Weapon"):
#             print(f"step {i+1} : found a sword ! you health add +50")
#             health += 50
#         elif(hidden_item == "Gold"):
#             print(f"step {i+1} : jackpot ! you gained 1000 gold")
#             gold += 1000
#         else:
#             print(f"step {i+1} : Attacked by monster ! health decreased by 80")
#             health -= 80

#         if(health <= 0):
#             print(f"Game Over! You died in the {current_room}.")
#             break

#     if(health > 0):
#         print(f"you survived with {health} HP and {gold} GOLD")

# question12()    


# question 13
# def question13():
#     budget = int(input("Enter you budget : "))
#     total_spent = 0

#     wish_list = ["Keyboard" , "Mouse" , "Monitor" , "Headphones" , "USB Drive"]
#     prices = {
#     "Keyboard": 30,
#     "Mouse": 15,
#     "Monitor": 150,
#     "Headphones": 40,
#     "USB Drive": 5
#     }

#     for i in range(len(wish_list)):
#         current_item = wish_list[i]
#         item_price = prices[current_item]

#         if(item_price > budget):
#             print(f"Item {i+1} : can't afford {current_item}. Skipping...")
#             continue
#         else:
#             budget -= item_price
#             total_spent += item_price
#             print(f"Item {i+1} : bought {current_item} for {item_price}. Remaining budget is {budget} RS")

#         if(budget == 0):
#             print("Wallet is empty! Stopping shopping.")
#             break

#     print(f"Shopping complete...! You spent {total_spent} RS and have {budget} RS left over")

# question13()



# # question 14
# def question14():
#     employees = [
#         {"name": "Alice", "role": "Manager", "salary": 80000},
#         {"name": "Bob", "role": "Developer", "salary": 60000},
#         {"name": "Charlie", "role": "Intern", "salary": 20000},
#         {"name": "Diana", "role": "Developer", "salary": 65000}
#     ]

#     for i in employees:
#         if(i['role'] == "Intern"):
#             print(f"* Assign a mentor to this employee. whose name is {i['name']} and work as  {i['role']} and makes ${i['salary']} *")
#         else:
#             print(f"{i['name']} works as a {i['role']} and makes ${i['salary']}")

# question14()



# # question 15
# def question15():
#     for floor in range(1,4):
#         for room in range(1,5):
#             print(f"Cleaning room {floor}0{room} at {floor}")
#     print()

# question15()  


# qeustion 16
# def question16():
#     total_bots_built = 0

#     orders = [
#         {"client": "Stark Industries", "qty": 3},
#         {"client": "Wayne Enterprises", "qty": 5},
#         {"client": "Oscorp", "qty": 2}
#     ]

#     for i in orders:
#         print(f"\nProcessing order for client : {i['client']}")
#         for j in range(i['qty']):
#             print(f"Assembling bot {j+1} for {i['client']} client...")
#             total_bots_built += 1
#     print()

#     print(f"\nFactory shutdown. Total robots built today: {total_bots_built}")

# question16()


# question 17
# def question17():
#     beans_stock = int(input("Enter the Beans stock : "))
#     total_revenue = 0

#     table_orders = [
#         {"table": 12, "drink": "Espresso", "qty": 3, "price": 4},
#         {"table": 5, "drink": "Americano", "qty": 5, "price": 3},
#         {"table": 8, "drink": "Mocha", "qty": 2, "price": 5}
#     ]

#     for i in table_orders:
#         print(f"\nProcessing Table : {i['table']}")
#         for j in range(i['qty']):
#             if(beans_stock > 0):
#                 print(f"Brewing {i['drink']} cup {j+1}")
#                 beans_stock -= 1
#                 total_revenue += i['price']
#             else:
#                 print(f"Out of beans! Cannot brew {i['drink']} cup {j+1}.")

#     print(f"\nShift over. Total revenue : ${total_revenue}. Beans remaining : {beans_stock}")

# question17()

"""problem solving day 10 question in just one day"""

# # question 18 = The Batch Name Cleaner
# def question18():
#     messy_names = ["   kRuTiKa   ", "  ", "rAhul  ", ""]
#     for i in messy_names:
#         messy_names = i.strip().lower()
#         if(messy_names == ""):
#             print("Error! blank name detected")
#         else:
#             print(f"Welcome {messy_names} !")

# question18()


# qeustion 19 = The Inventory Counter from string to list. and skip sugar as a count
# def question19():
#     delivery_string = "Milk Sugar Coffee Syrups Cups Lids"
#     delivery_string = delivery_string.split()

#     # a = len(delivery_string)
#     valid_items = 0
#     for i in delivery_string:
#         if(i == "Sugar"):
#             continue
#         else:
#             valid_items += 1

#     print(f"you have total {valid_items} valid items")


# question19()


# question 20 : The Rolling tax and discount.
# def question20():
#     total = float(input("Enter the total of your bill : "))
#     while True:
#         if(total == 0):
#             break
#         else:
#             total += total*0.18

#             if(total > 100):
#                 total -= 5
#                 total = round(total , 2)
#             break

#     print(f"your total bill amount is : {total}Rs")
# question20()



# question 21 : the VIP filter by using set and convert it to list
# def question21():
#     friday = {"Alice", "Bob", "Charlie"}
#     saturday = {"Charlie", "Bob", "Eve"}
#     loyal_guests = list(friday & saturday)

#     for i in loyal_guests:
#         if(i == "Charlie"):
#             print("Charlie gets the Ultimate VIP Pass.")
#         else:
#             print(f"{i} gets a STANDARD VIP pass")

# question21()


# question 22 : The Bulk Discount Engine
    
# def question22(guest_bills):

#     for table_name , details in guest_bills.items():
#         if(details['total'] > 50) and (details['member'] == True):
#             details['total'] *= 0.85

#     return guest_bills

# tonights_bills = {
#     "Table 1": {"total": 120, "member": True},
#     "Table 2": {"total": 45, "member": True},
#     "Table 3": {"total": 80, "member": False}
# }

# updated_bills = question22(tonights_bills)
# print(tonights_bills)



#uqestion 23 :  The Security Lockout

# def question23():

#     error_count = 0
#     daily_total = 0
#     while True:
#         item_price = int(input("Enter the item price : "))

#         if(item_price < 0):
#             error_count += 1
#         else:
#             error_count = 0
#             daily_total += item_price

#         if(error_count == 3):
#             print("System Locked....!")
#             break

# question23()


# question 24 : the shift formatter

# def question24():
#     staff = [{"name": "Krutika", "role": "Manager", "shift": "Day"},
#              {"name": "Rahul", "role": "Barista", "shift": "Night"}]

#     for i in staff:
#         if(i['shift'] == "Day"):
#             print(f"{i['name']} - {i['role']}")
#         else:
#             print(f"Alert : \n \t {i['name']} is on night shift")

# question24()


# question 25 : The revenu drop detector

# def question25():
#     revenue = [300 , 310 , 290 , 150 , 400]

#     for i in range(1 , len(revenue)):
#         if(revenue[i] < revenue[i-1]):
#             print(f"drop detected on day {i+1} ! Lost $ {revenue[i-1] - revenue[i]}")

# question25()


# question 26 : Unique digital menu

# def question26():
#     raw_menu = "latte, tea, espresso, tea, cake, latte"
#     split_menu = raw_menu.split(",")
#     clean_menu = []
#     for i in split_menu:
#         cleaned_item = i.strip()
#         if cleaned_item not in clean_menu:
#             clean_menu.append(cleaned_item)
        
#     for i in clean_menu:
#         print(i.upper())

# question26()     

# question 27 : The Live Kitchen Ticket System

# def question27():
#     orders = [
#                 {"table": 1, "items": ["Burger", "Fries"]},
#                 {"table": 2, "items": ["Salad"]}
#             ]
#     stock = {
#             "Burger": 1,
#             "Fries": 5,
#             "Salad": 0
#             }

#     for order in orders:
#         print(f"Table {order['table']}:")
#         for item in order['items']:
#             if(stock[item] > 0):
#                 stock[item] -= 1
#                 print(f"coocking {item}")
#             else:
#                 print(f"86 {item} ! Order cancelled for Table : {order['table']}.")
#                 break
# question27()


# question 28 : the stock audit

# def question28():
#     starting_stock = 15
#     adjustments = [10, -5, -8, -15, 20, -5]
#     for i in adjustments:
#         starting_stock += i
#         if(starting_stock >= 0):
#             print(f"Stock updated. Current level: {starting_stock}")
#         else:
#             print(f"CRITICAL ERROR: Stock cannot be negative. Halting audit!")
#             break

#     print(f"final audited stock : {starting_stock}")

# question28()


# question 29 : The Hotel Room Service Router

# def question29():
#     room_requests = [
#     {"room": 101, "items": ["Towels", "Soap"]},
#     {"room": 205, "items": ["Pillows", "Towels", "Shampoo"]}
#     ]

#     cart_inventory = {
#         "Towels": 2,
#         "Soap": 5,
#         "Pillows": 0,
#         "Shampoo": 3
#     }

#     for outerlp in room_requests:
#         print(f"\n- Processing Room {outerlp['room']} -")
#         for specific_item in outerlp['items']:
#             if(cart_inventory[specific_item] > 0):
#                 cart_inventory[specific_item] -= 1
#                 print(f"Delivering {specific_item}")
#             else:
#                 print(f"Out of stock on {specific_item} ! halting delivery for room {outerlp['room']}")
#                 break
# question29()


# question 30 = the safe divider
# def devide(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("cant devide with zero")

# devide(20 , 0)


# question 31 = The silent crash
# def question31():
#     try:
#         bad_data = int("glitch")
#     except ValueError:
#         pass

# question31()


# question 32 = the forgotten variable
# def question32():
#     try:
#         print(mystry_user)
#     except NameError:
#         print("Error : that variable name is not defined")

# question32()


# question 33
# def question33():
#     while True:
#         try:
#             user_num = int(input("enter a whole number : "))
#         except ValueError:
#             print("wrong input please try again")
#         else:
#             print("Thanks you !")
#             break

# question33()

# question 34
# def question34():
#     menu = ["Coffee", "Tea", "Water"]
#     index = int(input("Enter a index number : "))
#     try:
#         print(menu[index])
#     except IndexError:
#         print("That item number is not on menu")
#     finally:
#         print("Closing menu interface")

# question34()


# question 35
# def question35():
#     sensor_data = [70, 75, "Glitch", 80, "Error"]
#     for item in sensor_data:
#         try:
#             print(item + 10)
#         except TypeError:
#             print("Skipping corrupted data.")

# question35()


# questiop 36
# def question36():
#     data = {
#                 "Alice": "50000.50" ,
#                 "Bob": "Not Provided" ,
#                 "Charlie": "60000.00"
#                 }

#     for i in data.values():
#         try:
#             update = float(i)
#         except ValueError:
#             pass
#         else:
#             update += 1000
#             print(update)


# question36()


# question 37
# def question37():
#     box_weights = [100, 50, 0, 200]
#     index_input = int(input("Enter a number for index access : "))
#     try:
#         a = 1000/box_weights[index_input]
#         print(a)
#     except IndexError:
#         print("invalid box selection")
#     except ZeroDivisionError:
#         print("cant devide a container by 0 weight")

# question37()

# question 38

# def question38(user_list , user_id):
#     try:
#         user_id = user_id + 0
#         print(user_list[user_id])
#     except TypeError:
#         print("ID must be a number")
#     except IndexError:
#         print("profile is missing")
#     finally:
#         print("System check complete")
# question38(["Alice", "Bob", "Charlie", "Diana"] , "TWo")



# question 39
# def question39():
#     batches = [
#         [100, 5],        # 100 total items, 5 defects
#         [0, 10],         # 0 total items, 10 defects
#         [50, "Five"],    # 50 total items, "Five" defects
#         [40]             # Missing the defect data entirely
#         ]

#     for batchesiterate in batches:
#         try:
#             rate = batchesiterate[1] / batchesiterate[0]
#         except IndexError:
#             print("Audit Failed: Batch missing defect data.")
#         except TypeError:
#             print("Audit Failed: Batch contains text instead of numbers.")
#         except ZeroDivisionError:
#             print("Audit Failed: Total items cannot be zero.")
#         else:
#             print(f"Batch audited successfully. Defect rate : {rate}")
#         finally:
#             print("--- Moving to next batch ---")
# question39()



import sys
import statistics
import random
import cs50

# question 40 project : The Command-Line Data Auditor

# def question40():
#     arguments = sys.argv[1:]
#     valid_scores = []

#     for i in arguments:
#         try:
#            scr = float(i)
#            valid_scores.append(scr)
#         except ValueError:
#             pass

#     try:
#         average = statistics.mean(valid_scores)
#         print(average)
#     except statistics.StatisticsError:
#         print("ERROR : No valid number is provided")

# question40()


# question 41 project : The Secure Authentication Router
# def question41():
#     database = {
#         "admin": 1, 
#         "editor": 2, 
#         "viewer": 3
#         }
#     while True:
#         role = input("Enter a role : ").strip().lower()

#         match role:
#             case "admin" | "editor" | "viewer":
#                 level = database[role]
#                 print(f"access granted. your level is {level}")
#                 try:
#                     print(secure_key)
#                 except NameError:
#                     print("SECURITY ALERT : missing variable detected")
#             case "exit":
#                 print("Shutting down the system")
#                 break
#             case _:
#                 print("Unknown role")

# question41()

# question 42 : The Casino Shuffler & Payout Engine

# def question42():
#     bet = get_int()

# def get_int():
#         deck = ["Ace", "King", "Queen", "Jack", "10", "9"]
#         sfl = random.shuffle(deck)
#         while True:
#             try:
#                 bet = int(input("Enter the bet amount : "))
#             except ValueError:
#                 print("ERROR : enter the invalid bet amount type...!")
#                 break
#             card = random.choice(deck)
#             multiplier = 5 if card == "Ace" else 0
#             print(bet*multiplier)

# question42()


# question 43 : The Corrupted Inventory Matrix

# def question43():
#     warehouse = [
#                     ["Laptops", 50, 2],    # [Item, Total Stock, Daily Usage]
#                     ["Keyboards", 100],    # Missing usage data
#                     ["Monitors", "Ten", 5], # String instead of int
#                     ["Mice", 200, 0]       # Zero usage
#                 ]
#     fail_audit = 0
#     for item in warehouse:
#         try:
#             days = item[1]/item[2]
#         except IndexError:
#             print(f"{item[0]} is missing data.")
#             fail_audit += 1
#         except TypeError:
#             print(f"{item[0]} contains invalid text")
#             fail_audit += 1
#         except ZeroDivisionError:
#             print(f"{item[0]} has zero usage.")
#             fail_audit += 1
#         else:
#             print(f"{item[0]}: {round(days)} days remaining.")

#     print(f"total failed audits : {fail_audit}")
        
# question43()


# question 44 : The Master Terminal
# import statistics
# import random

# def question44():
#     system_memory = []
    
#     while True:
#         print("\nSelect command: \n1: add \n2: average \n3: random \n4: clear \n5: exit")
#         cmd = input("Enter the command: ").strip().lower()
        
#         try:
#             match cmd:
#                 case "add" | "1":
#                     try:
#                         num = int(input("Enter a number: "))
#                         system_memory.append(num)
#                     except ValueError:
#                         print("You entered the wrong value type, make sure it is an integer.")
                        
#                 case "average" | "2":
#                     try:
#                         print(f"The average is: {statistics.mean(system_memory)}")
#                     except statistics.StatisticsError:
#                         print("Can't calculate average: no memory data found.")
                        
#                 case "random" | "3":
#                     try:
#                         random_index = random.randint(0, len(system_memory))
#                         print(f"Random item: {system_memory[random_index]}")
#                     except IndexError:
#                         print("Cannot pick a random item: The list is empty or index is out of bounds.")
                        
#                 case "clear" | "4":
#                     system_memory.clear()
#                     print("Memory cleared.")
                    
#                 case "exit" | "5":
#                     break
#         finally:
#             # This will now trigger after EVERY command, even if you clear the list or exit!
#             print(f"Current Memory Size: {len(system_memory)}")

# question44()

# question 45 : Project 1: The Command-Line Sensor Calibrator

# def question45():
#     arguments = sys.argv[1:]
#     clean_temps = []
#     for i in arguments:
#         i = i.strip()
#         try:
#             str_flt = float(i)
#             clean_temps.append(str_flt)
#         except ValueError:
#             pass
#     try:
#         avg_temp = statistics.mean(clean_temps)
#     except ZeroDivisionError:
#         print("here is zero in list")
#     except statistics.StatisticsError:
#         print("zero values in the list not able to calculate average")
#         if not clean_temps:
#             sys.exit()

#     for temp in clean_temps:
#         if(temp > avg_temp):
#             print(f"WARNING: {temp} is above the {round(avg_temp, 1)} average!")

# question 46 : Project 2 :  The E-Commerce Fraud Engine

# def question46():
#     transactions = ["alice-500", "bob-50", "charlie", "diana-9000", "eve-error"]
#     for i in transactions:
#         i = i.split("-")
#         try:
#             i = int(i[1])
#         except IndexError:
#             print("Fraud Alert: Missing amount data.")
#         except ValueError:
#             print("Fraud Alert: Corrupted amount.")
#         else:
#             status = "Flagged" if i > 1000 else "Clear"
#             if(status == "Flagged"):
#                 pin = random.randint(1000, 9999)
#                 print(f"Account Locked. Verification PIN {pin} sent to user.")
# question46()


# question 47 : Project 3 : The Financial Market Routing Matrix

# def question47():
#     trades = [
#                 ["AAPL", 5000, 50],   # Ticker, Total Value, Shares
#                 ["TSLA", 0, 10],      # Zero value
#                 ["GOOG", 8000, 0],    # Zero shares
#                 ["AMZN", "Ten", 5]    # Text instead of int
#             ]
#     for trade in trades:
#         if(trade[1] == 0):
#             print("Ignoring zero-value trade.")
#             continue
#         try:
#             price_per_share = trade[1] / trade[2] 
#         except TypeError:
#             print(f"Data error for {trade[0]}.")
#         except ZeroDivisionError:
#             print(f"Trade halted for {trade[0]}: Cannot divide by zero shares.")
#         else:
#             print(f"{trade[0]} executed at ${round(price_per_share, 2)} per share.")
# question47()

# question 48 : Project 4 : The Autonomous Drone Controller
# def question48():
#     altitude_integer = get_int()
# def get_int():
#     current_altitude = 0
#     while True:
#         print("commands : \n1 : climb \n2 : descend \n3 : status \n4 : exit")
#         command = input("Enter the command : ").strip().lower()
#         try:
#             match command:
#                 case "climb" | "1":
#                     while True:
#                         try:
#                             altitude_integer = int(input("Enter the altitude : "))
#                             current_altitude += altitude_integer
#                             break
#                         except ValueError:
#                             print("Invalid input. Please enter a whole number.")
#                 case "descend" | "2":
#                     while True:
#                         try:
#                             altitude_integer = int(input("Enter the altitude : "))
#                             current_altitude -= altitude_integer
#                             if current_altitude < 0 or current_altitude == 0:
#                                 current_altitude = 0 
#                             break
#                         except ValueError:
#                             print("Invalid input. Please enter a whole number.")
#                         break
#                 case "status" | "3":
#                     try:
#                         print(drone_battery)
#                     except NameError:
#                         print("Warning: Battery sensor disconnected.")
#                 case "exit" | "4":
#                     break
#         finally:
#             print(f"Altitude locked at {current_altitude}m.")

# question48()

# question 49 : Project 5: The Master Server OS
# def question49():
#     active_users = {"admin": [50, 60, 45], "guest": []}
#     while True:
#         user_name = input("Enter the username : ").strip().lower()
#         if(user_name == "shutdown"):
#             break
#         try:
#             user_data = active_users[user_name]
#         except KeyError:
#             print("User not found.")
#             continue

#         new_ping = random.randint(0, 100)
#         user_data.append(new_ping)

#         try:
#             avg_load = statistics.mean(active_users[user_name])
#         except statistics.StatisticsError:
#             print("list is empty")
#         else:
#             print(f"User: {user_name}")
#             print(f"Loads: {active_users[user_name]}")
#             print(f"Average Load: {round(avg_load, 2)}")

# question49()