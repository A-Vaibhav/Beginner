import datetime

today = datetime.datetime.now()
today_year = today.year

def guess_age():
    dob = input("Enter Date of Birth (21-05-1996): ")
    age = today_year - int(dob[-4:])

    return age

            
result = guess_age()
print(result)