import pandas as pd
import matplotlib.pyplot as plt
import os

print("---------------------------WELCOME TO LUXURY CAR RENTALS---------------------------")

# File paths (update if needed)
USER_FILE = r"C:\Users\deshm\OneDrive\Desktop\EXCEL\Users.csv"
CAR_FILE = r"C:\Users\deshm\OneDrive\Desktop\EXCEL\Cars.csv"
MEMBER_FILE = r"C:\Users\deshm\OneDrive\Desktop\EXCEL\Members.csv"
BOOKED_CAR_FILE = r"C:\Users\deshm\OneDrive\Desktop\EXCEL\Cars Booked.csv"

# Function to add a new user
def addUser():
    uid = input("Enter User ID: ")
    uname = input("Enter User Name: ")
    pwd = input("Enter Password: ")
    udf = pd.read_csv(USER_FILE)
    n = udf["User ID"].count()
    udf.loc[n] = [uid, uname, pwd]
    udf.to_csv(USER_FILE, index=False)
    print("User added successfully!")
    print(udf)

# Function to delete a user
def deleteUser():
    uid = input("Enter a User ID to delete: ")
    udf = pd.read_csv(USER_FILE)
    if uid in udf["User ID"].values:
        udf = udf.drop(udf[udf["User ID"] == uid].index)
        udf.to_csv(USER_FILE, index=False)
        print("User deleted successfully!")
        print(udf)
    else:
        print("User ID not found!")

# Function to add a new car
def addNewCar():
    carno = input("Enter a Car Number: ")
    carname = input("Enter Name of the Car: ")
    brand = input("Enter brand of the Car: ")
    branch = input("Enter branch: ")
    fueltype = input("Enter fuel type of the car: ")
    cost = input("Enter cost of rent per day: ")
    category = input("Enter category of the car: ")
    cdf = pd.read_csv(CAR_FILE)
    n = cdf["Car No."].count()
    cdf.loc[n] = [carno, carname, brand, branch, fueltype, cost, category]
    cdf.to_csv(CAR_FILE, index=False)
    print("Car added successfully!")
    print(cdf)

# Function to search for a car
def searchCar():
    carname = input("Enter a Car name to search: ")
    cdf = pd.read_csv(CAR_FILE)
    df = cdf.loc[cdf["Car Name"] == carname]
    if df.empty:
        print("No cars found with the given name.")
    else:
        print("Car details:")
        print(df)

# Function to delete a car
def deleteCar():
    carno = input("Enter a Car Number to delete: ")
    cdf = pd.read_csv(CAR_FILE)
    if carno in cdf["Car No."].astype(str).values:
        cdf = cdf.drop(cdf[cdf["Car No."].astype(str) == carno].index)
        cdf.to_csv(CAR_FILE, index=False)
        print("Car deleted successfully!")
        print(cdf)
    else:
        print("Car Number not found!")

# Function to display all cars
def showCars():
    cdf = pd.read_csv(CAR_FILE)
    print("List of all cars:")
    print(cdf)

# Function to add a new member
def addNewMember():
    mid = input("Enter Member ID: ")
    mname = input("Enter Member Name: ")
    phoneno = input("Enter Phone Number: ")
    numberofcarsbooked = 0
    mdf = pd.read_csv(MEMBER_FILE)
    n = mdf["MID"].count()
    mdf.loc[n] = [mid, mname, phoneno, numberofcarsbooked]
    mdf.to_csv(MEMBER_FILE, index=False)
    print("Member added successfully!")
    print(mdf)

# Function to search for a member
def searchMember():
    mname = input("Enter a Member Name to search: ")
    mdf = pd.read_csv(MEMBER_FILE)
    df = mdf.loc[mdf["M Name"] == mname]
    if df.empty:
        print("No members found with the given name.")
    else:
        print("Member details:")
        print(df)

# Function to delete a member
def deleteMember():
    mid = input("Enter a Member ID to delete: ")
    mdf = pd.read_csv(MEMBER_FILE)
    if mid in mdf["MID"].astype(str).values:
        mdf = mdf.drop(mdf[mdf["MID"].astype(str) == mid].index)
        mdf.to_csv(MEMBER_FILE, index=False)
        print("Member deleted successfully!")
        print(mdf)
    else:
        print("Member ID not found!")

# Function to display all members
def showMembers():
    mdf = pd.read_csv(MEMBER_FILE)
    print("List of all members:")
    print(mdf)

# Function to book a car
def bookCar():
    carname = input("Enter Car Name to book: ")
    cdf = pd.read_csv(CAR_FILE)
    car = cdf.loc[cdf["Car Name"] == carname]
    if car.empty:
        print("No car found with the given name.")
        return

    mname = input("Enter Member Name: ")
    mdf = pd.read_csv(MEMBER_FILE)
    member = mdf.loc[mdf["M Name"] == mname]
    if member.empty:
        print("No member found with the given name.")
        return

    dateofbooking = input("Enter Date of Booking (YYYY-MM-DD): ")
    numberofdays = int(input("Enter the Number of Days: "))
    cost_per_day = int(car.iloc[0]["Cost"])
    total_cost = cost_per_day * numberofdays

    print("^" * 40)
    print("BILL GENERATED")
    print("^" * 40)
    print(f"Car Rented: {carname}")
    print(f"Name of Member: {mname}")
    print(f"Cost per Day: {cost_per_day}")
    print(f"Total Rental Cost: {total_cost}")
    print("^" * 40)

    bdf = pd.read_csv(BOOKED_CAR_FILE)
    n = bdf["Car Name"].count()
    bdf.loc[n] = [carname, mname, dateofbooking, numberofdays, total_cost]
    bdf.to_csv(BOOKED_CAR_FILE, index=False)
    print("Car booked successfully!")
    print(bdf)

# Function to handle login
def login():
    if not os.path.exists(USER_FILE):
        print(f"{USER_FILE} not found. Creating a new file...")
        pd.DataFrame(columns=["User ID", "User Name", "Password"]).to_csv(USER_FILE, index=False)

    uid = input("Enter User ID: ")
    uname = input("Enter User Name: ")
    pwd = input("Enter Password: ")

    df = pd.read_csv(USER_FILE)
    user = df[(df["User ID"] == uid) & (df["User Name"] == uname) & (df["Password"] == pwd)]
    if user.empty:
        print("Invalid credentials! Please try again.")
        return False
    else:
        print("Login successful!")
        return True

# Menu options
def showMenu():
    print("----------------------------------------------------------------------------------------")
    print("                               LUXURY CAR RENTALS                                       ")
    print("----------------------------------------------------------------------------------------")
    print("Press 1 - Add a User")
    print("Press 2 - Delete a User")
    print("Press 3 - Add a New Car")
    print("Press 4 - Search for a Car")
    print("Press 5 - Delete a Car")
    print("Press 6 - Show all Cars")
    print("Press 7 - Add a New Member")
    print("Press 8 - Search for a Member")
    print("Press 9 - Delete a Member")
    print("Press 10 - Show all Members")
    print("Press 11 - Book a Car")
    print("Press 12 - Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Main program logic
if login():
    while True:
        ch = showMenu()
        if ch == 1:
            addUser()
        elif ch == 2:
            deleteUser()
        elif ch == 3:
            addNewCar()
        elif ch == 4:
            searchCar()
        elif ch == 5:
            deleteCar()
        elif ch == 6:
            showCars()
        elif ch == 7:
            addNewMember()
        elif ch == 8:
            searchMember()
        elif ch == 9:
            deleteMember()
        elif ch == 10:
            showMembers()
        elif ch == 11:
            bookCar()
        elif ch == 12:
            break
        else:
            print("Invalid option selected!")
print("THANK YOU FOR VISITING LUXURY CAR RENTALS")
