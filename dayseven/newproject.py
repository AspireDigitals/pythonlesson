country = input("Enter country: ")

if  country.lower() != "ghana":
    print("not a Ghanaian")
else:
    name = input("Enter fullname: ")
    age = int(input("Enter age: "))
    if age >= 18 and age <= 60:
        print(f"{name} is eligible to work in government company")
    else:
        print(f"{name} is not eligible to work in government company")



