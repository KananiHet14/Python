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