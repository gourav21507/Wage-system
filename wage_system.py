#Introduction code for wage system:

print("Entering into the wage system...")

intro = input("Enter Y/N if you want an intro about the Key wards of the program ")

if intro.lower() == "y":
    print("OK !! There is some information about the key wards in this program")
    print("In this program \n CIT = Check In Time \n COT = Check Out Time")
else:
    pass

name = input("Enter the name of labour : ")

#Creating time variables : 

cith = int(input("Enter CIT in hrs : "))

#Putting cunditions for right input :

while cith > 12 :
    print("your input is wrong please enter it again it should be less than 12 hrs : ")
    cith = int(input("Enter CIT in hrs again : "))

citm = int(input("Enter CIT in min : "))

while citm > 60 :
    print("your input is wrong please enter it again it should be less than 60 min : ")
    citm = int(input("Enter CIT in min again : "))

cits = int(input("Enter CIT in sec : "))

while cits > 60 :
    print("your input is wrong please enter it again it should be less than 60 sec : ")
    cits = int(input("Enter CIT in sec again : "))

#Creating am/pm variable for CIT :

citap = input("Enter AM or PM for CIT : ")

#Putting condition to enter right am/pm for CIT:

while citap not in ["am", "pm", "Am", "Pm", "AM", "PM"] : 
    print("Your AM PM Entry is worng : ")
    citap = input("Enter AM/PM again : ")

#Creating COT time variables : 

coth = int(input("Enter COT in hrs : "))

while coth > 12 :
    print("your input is wrong please enter it again it should be less than 12 hrs : ")
    coth = int(input("Enter COT in hrs again : "))

cotm = int(input("Enter COT in min : "))

while cotm > 60 :
    print("your input is wrong please enter it again it should be less than 60 min : ")
    cotm = int(input("Enter COT in min again : "))

cots = int(input("Enter COT in sec : "))

while cots > 60 :
    print("your input is wrong please enter it again it should be less than 60 sec : ")
    cots = int(input("Enter COT in sec again : "))


#Creating am/pm variable for COT :

cotap = input("Enter AM or PM for COT : ")

#Putting condition to enter right am/pm for COT:

while cotap not in ["am", "pm", "Am", "Pm", "AM", "PM"] :
    print("Your AM PM Entry is worng : ")
    cotap = input("Enter AM/PM again : ")


#Adding logics on negetive time bug :

if citap == "pm" and cotap == "am":
    print("Invalid operation your am pm values are not valid (CIT = PM and COT = AM) put them again ")

    # Condition for CIT :
    print("Enter your CIT value again :")
    citap = input("Enter AM/PM again : ")
    while citap not in ["am", "pm", "Am", "Pm", "AM", "PM"] :
        citap = input("Enter AM/PM again : ")
    
    print("Enter your COT value again :")

    # Condition for COT :
    cotap = input("Enter AM/PM again : ")
    while cotap not in ["am", "pm", "Am", "Pm", "AM", "PM"] :
        cotap = input("Enter AM/PM again : ")
else :
    pass

if citap == "am" and cotap == "am":
    while coth < cith :
        print("Invalid Operation your COTH value is smaller than CITH ")
        print("Enter CITH anf COTH value again")
        cith = int(input("Enter CITH value again : "))
        coth = int(input("Enter COTH value again : "))
elif citap == "pm" and cotap == "pm":
    while coth < cith :
        print("Invalid Operation your COTH value is smaller than CITH ")
        print("Enter CITH anf COTH value again")
        cith = int(input("Enter CITH value again : "))
        coth = int(input("Enter COTH value again : "))

else:
    pass


#Putting condition to create sence of am pm logic for CIT :

if citap.lower() == "pm":
    cith += 12
else:
    pass

#Putting condition to create sence of am pm logic for COT :

if cotap.lower() == "pm":
    coth += 12
else:
    pass

# Asking for rate :

rate = int(input("Enter rate for per hour work : "))

# Putting logic : 

work_Time = int((coth*(60**2) + cotm*60 + cots) - (cith*(60**2) + citm*60 + cits))

# Printing details :

print("Name of the labour is : ", name)
print("Your work time is ", (work_Time/60**2), " Hrs")
print("Your wage is : Rs", int((work_Time/60**2)*rate))

