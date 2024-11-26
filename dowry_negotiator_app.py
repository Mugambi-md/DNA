def body_count(age):
    "Determines body count based on age"
    if 18<=age<=22:
        return 2
    elif 22<age<=25:
        return 6
    elif 25<age<30:
        return 10
    elif age < 30:
        return 15
    else:
        return 20
    

def dowry_negotiation(name, age, body_count_result, asked_dowry, single_mother, college):
    if college:
        body_count_result = body_count_result * 1.5
        
    actual_dowry = asked_dowry/(body_count_result + 1)

    if age>30 and single_mother:
        print(f"Dowry for: {name} is {actual_dowry:.2f}\nBut we recomend no dowry should be paid to single mother who is above age 30.\nShe has extra cost to raise the child and beyold age.")
    elif age>30 :
        print(f"Dowry for: {name} is {actual_dowry:.2f}\nBut we recomend no dowry should be paid to a woman above 30yrs.\nNo point to pay her.")
    elif single_mother:
        print(f"Dowry for: {name} is {actual_dowry:.2f}\nBut we recomend no dowry should be paid to single mother.\nShe has extra cost to raise the child.")
    else:
        print(f"Dowry for: {name} is {actual_dowry:.2f}")

def get_user_data():
    """Function to collect user data and pass it to the processing function."""
    name = input("Enter Brides Name: ")
    age = int(input("Enter Brides' Age: "))
    while age < 18:
        print("Too young age!. Enter age 18 and above.")
        age = int(input("Enter Brides' Age: "))
    asked_dowry =int(input("Enter the dowry requested: "))
    while asked_dowry <=0:
        print("Dowry Should Not be Less or Equal to 0.")
        asked_dowry =int(input("Enter the dowry requested: "))
    
    college_input = input("Has she gone to college? (yes/no): ").strip().lower()
    while college_input not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
        college_input = input("Has she gone to college?(yes/no): ").strip().lower()
    college = college_input=="yes"
    single_mother_input = input("Is Bride a Single Mother?(yes/no): ").strip().lower()
    while single_mother_input not in ["yes", "no"]:
        print("Please Enter 'yes' or 'no'.")
        single_mother_input = input("Is Bride a Single Mother?(yes/no): ").strip().lower()
    single_mother = single_mother_input=="yes"
    body_count_result = body_count(age)
    dowry_negotiation(name, age, body_count_result, asked_dowry, single_mother, college)

if __name__ == "__main__":
    print("Welcome to dowry negotiation program!")
    get_user_data()