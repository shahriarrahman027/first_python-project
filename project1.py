name_color = "\033[35m"
bold="\033[1m"
reset ="\033[0m"
error_color = "\033[31m"
correct_color= "\033[32m"
print(bold+name_color+"                Welcome To Daffodil Smart City"+reset)
print("             -----------------------------------")
print("Please enter your information:")
name = input("What is your Name: ")
if len(name)>20 or any(c.islower() for c in name):
    print(bold+error_color+"Your usernamae has more than 12 characters or lowercase "+reset)
    print(bold+correct_color+"Make a username contains less than 12 characters and don't have any lowercase! "+reset)
else:
    age = int(input("What is your Age: "))
    school = input("What is the name of your School: ")
    college = input("What is the name of your College: ")
    University = input("What is the name of your University: ")
    department = input("What is the name of your Department: ")
    id =input("Please Enter Your Student ID Number(e.g : xxx-xx-xxx):")
    parts = id.split("-")
    if len(parts) == 3:
       if parts[1] !="15":
           print(bold+error_color+"Sorry!Your not a Student of CSE"+reset)
           print(bold+correct_color+"This is only for CSE student!😊"+reset)
       else:
            print("  ")
            Bold = "\033[1m"
            Reset = "\033[0m"
            Color = "\033[32m"
            print(Bold+Color+"        🧑🏻‍🎓Daffodil Smart City👩🏻‍🎓       "+Reset)
            print("  ")
            lebel_color = "\033[33m"
            value_color = "\033[36m"
            tag_color = "\033[31m"
            print(Bold + lebel_color + "Name       : " + value_color+name+Reset)
            print(Bold + lebel_color + "Age        : " + value_color+str(age)+Reset)
            print(Bold + lebel_color + "School     : " + value_color+school+Reset)
            print(Bold + lebel_color + "College    : " + value_color+college+Reset)
            print(Bold + lebel_color + "University : " + value_color+University+Reset)
            print(Bold + lebel_color + "Department : " + value_color+department+Reset)
            print("           ")
            print(Bold+tag_color+"             Stay Safe,Stay Happy!             "+Reset)
            print("            ")
    else: 
        print("Invalid Id format")


