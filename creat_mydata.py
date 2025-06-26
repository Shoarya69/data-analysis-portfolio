import pandas as pd
import random as rd
import numpy as np
import string as st
from datetime import datetime

now = datetime.now()
    # Create a DataFrame with random data
def generate_id():
    letters = ''.join(rd.choices(st.ascii_uppercase + st.digits + st.ascii_uppercase, k=6))
    return letters

def generate_name():
    names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hannah','KO','PI']
    return rd.choice(names)

def generate_city(n = 10):
    city = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
    return rd.choice(city[0:10])

def generate_product(n = 10):
    products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Scanner', 'Webcam', 'Headphones']
    return rd.choice(products[0:n])

def generate_Department(n = 10):
    departments = ['IT', 'HR', 'Finance', 'Sales', 'Markting','Legal', 'Operations', 'Customer Service', 'Research and Development', 'Administration']
    return rd.choice(departments[0:n])

def generate_Gender(name = None):
    male_names =['Ko','Pi','Bob', 'Charlie', 'Frank']
    female_names = ['Alice', 'Diana', 'Eve', 'Grace', 'Hannah']
    if name in male_names:
        return 'Male'
    elif name in female_names:
        return 'Female'
    else:
        return rd.choice(['Male','Female'])
    
def generate_age():
    return rd.randint(20, 60)

def generate_experience(age = None):
    
    if age is None:
        age = generate_age()   
    if age < 25:
        return rd.randint(0, 2)
    elif age < 30:
        return rd.randint(2, 5)
    elif age < 40:
            return rd.randint(5, 7)
    elif age < 50:
        return rd.randint(7, 20)
    else:
        return rd.randint(20, 30)


def generate_Status(Experience = None):
    if Experience is None:
        Experience = generate_experience()
    if Experience < 2: 
        status = ['Intern', 'Junior']
    elif Experience < 5:
        status = ['Junior', 'Mid-level']
    elif Experience < 10:
        status = ['Mid-level', 'Senior','Expert']
    else:
        status = ['Senior', 'Lead', 'Manager']
    return rd.choice(status)
    

def generate_salary(experience = None,depertament= None):
    if experience is None:
        experience = generate_experience()
    if depertament is None:
        depertament = generate_Department()
    if depertament == 'IT':
        return rd.randint(50000 + experience * 2000, 120000 + experience * 5000)
    elif depertament == 'HR':
        return rd.randint(40000 + experience * 1500, 100000 + experience * 4000)
    elif depertament == 'Finance':
        return rd.randint(60000 + experience * 2500, 150000 + experience * 6000)
    elif depertament == 'Sales':
        return rd.randint(30000 + experience * 1000, 90000 + experience * 3000)
    elif depertament == 'Markting':
        return rd.randint(35000 + experience * 1200, 95000 + experience * 3500)
    else:
        return rd.randint(30000 + experience * 800, 80000 + experience * 2500)

def generate_Subject(n = 3):
    return rd.sample(['Math', 'Science', 'History', 'English', 'Art', 'Music', 'Physical Education', 'Computer Science', 'Biology', 'Chemistry'], k=n)

def generate_score():
    return rd.randint(20,100)


def generat_Attendance():
     return np.random.choice(['Present', 'Absent'], p=[0.8, 0.2])

def generate_date():
    year = rd.randint(2020, 2023)
    month = rd.randint(1, 12)
    day = rd.randint(1, 28)  # To avoid issues with February
    return f"{day:02d}/{month:02d}/{year}"

def generate_country():
    countries = ['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'India', 'China', 'Japan', 'Brazil']
    return rd.choice(countries)

def generate_phone():
    return f"+91-{rd.randint(6,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}"

def generate_email(name = None):
    if name is None:
        name = generate_name()
    domains = ['example.com', 'test.com', 'demo.com', 'sample.com']
    return f"{name.lower()}{rd.randint(0,100)}@{rd.choice(domains)}"

def generat_rating():
    return rd.randint(1,10)


def generate_sales(product = None):
    # products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Scanner', 'Webcam', 'Headphones']
    
    if product == 'Laptop':
        return rd.randint(500,2000)
    elif product == 'Smartphone':   
        return rd.randint(1000,3000)
    elif product == 'Tablet':
        return rd.randint(200,1000)
    elif product == 'Monitor' or product == 'Keyboard' or product == 'Mouse' or product == 'Headphone':
        return rd.randint(100,500)
    elif product == 'Scanner' or product == 'Scanner' or product == 'Webcam':
        return rd.randint(100,300)
    else:
        return rd.randint(100,500)



def generate_Money(Sales = None,product= None):
    if product == 'Laptop' and Sales>0 :
        z = [i for i in range(30,200,5)]
        return Sales *rd.choice(z)*1000
    elif product == 'Smartphone':   
        z = [i for i in range(30,100,4)]
        return Sales *rd.choice(z)*1000
    elif product == 'Tablet' and Sales>0:
        z = [i for i in range(30,100,4)]
        return Sales *rd.choice(z)*1000        
    elif (product == 'Monitor' or product == 'Keyboard' or product == 'Mouse' or product == 'Headphone') and Sales>0:
        z = [i for i in range(5,100,20)]
        return Sales *rd.choice(z)*100
    elif (product == 'Scanner' or product == 'Scanner' or product == 'Webcam' ) and Sales>0:
        z = [i for i in range(10,60,15)]
        return Sales *rd.choice(z)*100

    elif Sales>0:
        z = [i for i in range(10,300,40)]
        return Sales *rd.choice(z)*100
 

while True:
    try:
        a = int(input("Enter how much lines of data you want to generate: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


v = []

while True:
    print("Select the type of data you want to generate:")
    print("1. ID")
    print("2. Name")
    print("3. City")
    print("4. Product")
    print("5. Department")
    print("6. Age")
    print("7.gender")
    print("8. Experience")
    print("9. Status")
    print("10. Salary")
    print("11. Attendance")
    print("12. Date")
    print("13. Country")
    print("14. Phone")
    print("15. Email")
    print("16. Subject")
    print("17 . For rating")
    print("0. Exit")
    c = input("Select:- ")
    if c == '0':
        print("Exiting the selection.")
        break
    elif c in [str(i) for i in range(1,17)]:
        v.append(c)
    else:
        print("you enter wrong option try again")

v = [int(x) for x in v]
if 16 in v:
    while True:
        try:
            d = int(input("How many subject in num(<10):- "))
            break
        except Exception:
            print("invalid try again")

f = input("Name of file(without extension and without spacing):- ")

data = {}
df = pd.DataFrame(data)

if 1 in v:
    id = []
    for i in range(a):
        id.append(generate_id())
    g = input("Name the id fileld = ")
    df[g] = id

if 2 in v:
    name = []
    for i in range(a):
        name.append(generate_name())
    g = input("Name the 'name' filed = ")
    df[g] = name

if 3 in v:
    city = []
    for i in range(a):
        city.append(generate_city())
    
    df['City'] = city

if 4 in v:
    
    product = []
    for i in range(a):
        product.append(generate_product())
    df['Product'] = product
    q = input("if you want to make product sale data also press y other wise any other key:- ")
    if q == 'y':
        pop = input("do you want to generate also how much money maked if want press y and not then any key:-")
        Sales = []
        for i in range(a):  
            Sales.append(generate_sales(product[i]))
        df['Sales'] = Sales
        if pop == 'y':
            profit = []
            Money = []
            for i in range(a):
                Money.append(generate_Money(Sales[i],product[i]))
                profit.append(Money[i]*0.4)
            df['Sales Generat'] = Money
            df['Profit'] = profit   
        
if 5 in v:
    Department = []
    for i in range(a):
        Department.append(generate_Department())
    df['Dedartment'] = Department

if 6 in v:
    age = []
    for _ in range(a):
        age.append(generate_age())
    
    df['Age'] = age

if 7 in v:
    gender = []
    if 2 in v:
        for i in range(a):
            gender.append(generate_Gender(name[i]))
    else:
        for i in range(a):
            gender.append(generate_Gender())
    df["Gender"] = gender

if 8 in v:
    Experience = []
    if 6 in v:
        for i in range(a):
            Experience.append(generate_experience(age[i]))
    else:
        for i in range(a):
            Experience.append(generate_experience())
    df['Exprience'] = Experience

if 9 in v:
    status = []
    if 8 in v:
        for i in range(a):
            status.append(generate_Status(Experience[i]))
    elif 6 in v:
        for i in range(a):
            temp = generate_experience(age[i])
            status.append(generate_Status(temp))
    else:
        for i in range(a):
            status.append(generate_Status())
    df['Status'] = status

if 10 in v:
    salary = []
    if 5 in v and 8 in v:
        for i in range(a):
            salary.append(generate_salary(Experience[i], Department[i]))
    elif 5 in v and 6 in v:
        for i in range(a):
            temp = generate_experience(age[i])
            salary.append(generate_salary(temp,Department[i]))
    elif 5 in v:
        for i in range(a):
            salary.append(generate_salary(None,Department[i]))
    elif 8 in v:
        for i in range(a):
            salary.append(generate_salary(Experience[i]))
    else:
        for i in range(a):
            salary.append(generate_salary())
    df['Salary'] = salary

if 11 in v:
    Attendndence = []
    for i in range(a):
        Attendndence.append(generat_Attendance())
    df['Attendence'] = Attendndence

if 12 in v:
    date = []
    while True:
        try:
            l = int(input("if you want same date the press 1 other wise 2 and 3 for current data:- "))
            break
        except Exception:
            print("invalid do it again")
    if l == 1:
        dat = generate_date()
        for i in range(a):
            date.append(dat)
    elif l == 2:
        for i in range(a):
            date.append(generate_date())
    elif  l == 3:
        dat = now.date
        for i in range(a):
            date.append(dat)
    else:
        print("you choce wrong choice that's why we are going to set some randome but same date")
        dat = generate_date()
        for i in range(a):
            date.append(dat)    
    df['Date'] = date

if 13 in v:
    Country = []
    for i in range(a):
        Country.append(generate_country())
    df['Country'] = Country

if 14 in v:
    phone = []
    for i in range(a):
        phone.append(generate_phone())
    df['Mobile Number'] = phone

if 15 in v:
    email = []
    if 2 in v:
        for i in range(a):
            email.append(generate_email(name[i]))
    else:
        for i in range(a):
            email.append(generate_email())
    df['eMAIL'] = email

if 16 in v:
    selected_subjects = generate_Subject(d)
    for subject in selected_subjects:
        df[subject] = [generate_score() for _ in range(a)]

if 17 in v:
    rating = []
    for i in range(a):
        rating.append(generat_rating())
    df['Rating']
    
df.to_excel(f"{f}.xlsx",index = False)
print(f"{f}.xlsx file is ready")