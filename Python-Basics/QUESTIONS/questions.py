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