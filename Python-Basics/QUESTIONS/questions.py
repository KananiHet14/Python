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


