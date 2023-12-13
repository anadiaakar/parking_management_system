import time
from collections import OrderedDict
 

def get_spot(i):
    """This funtion return a dictioinary of parking spot"""
    reqd_dict = {}
    reqd_dict['level'] = i.split(',')[0]
    reqd_dict['spot'] = i.split(',')[1]
    return reqd_dict

def confirm_car_reg():
    """This function displays prompt for entering car registeration"""
    val = 0
    while True:
        car_reg = input("Please enter car registeration no. :")
        print("Car registeration number is "+car_reg)
        try:
            val = int(input("Press 1 to confirm : ").strip())
        except ValueError as e:
            print("Please Enter valid Input ")
        if val == 1:
            return car_reg

def display_prompt():
    """This Function displays a prompt for using various features of 
    parking management system"""

    print("Choose an option from below: ")
    print('1. Park a Car')
    print('2. Find a car')
    print('3. Unpark a Car')
    try:
        val = int(input("Please enter you input : "))
    except ValueError as e:
        print("Please Enter valid Input ")
        return
    if val > 3 or val <1:
        print("Please Enter valid Input")
    else:
        return val


def park_car():
    """This finctions assigns closest parking spot to a car"""
    global parking_dict
    car_reg = confirm_car_reg()
    if car_reg.upper() in parking_dict.values():
        print('*********************************')
        print('Car already in Parking lot')
        print('*********************************')
    else:
        for i,j in parking_dict.items():
            if j == '':
                parking_dict[i] = car_reg.upper()
                print('*********************************')
                print("You car is parked at :")
                print(get_spot(i))
                print('*********************************')
                return
        

def find_car():

    """This function finds the parking spot of a parked car"""
    global parking_dict
    car_reg = confirm_car_reg()
    for i,j in parking_dict.items():
        if j == car_reg.upper():
            print('*********************************')
            print("You car is parked at : ")
            print(get_spot(i))
            print('*********************************')
            return
    print('*********************************')
    print("Unable to find car. Please recheck car registration")
    print('*********************************')

def unpark_car():

    """This function unlinks the car from parking spot"""
    global parking_dict
    car_reg = confirm_car_reg()
    for i,j in parking_dict.items():
        if j == car_reg.upper():
            parking_dict[i]=''
            print('*********************************')
            print("You car is unparked from ")
            print(get_spot(i))
            print('*********************************')
            return
    print('*********************************')
    print("Unable to find car. Please recheck car registration")
    print('*********************************')

if __name__ == "__main__":
    global parking_dict
    #Global variable is used to share memory among all the functions of code
    parking_dict = OrderedDict()
    #Order dict is used, So as to get closest parking spot each time
    for i in range(1,21):
        parking_dict['A,'+str(i)] = ''
    for i in range(1,21):
        parking_dict['B,'+str(i)] = ''
    
    while True:
        val = display_prompt()
        if val:
            if val == 1:
                park_car()
            elif val ==2:
                find_car()
            elif val==3:
                unpark_car()
        time.sleep(1)
        # print('*********************************')
        # print(parking_dict)
        # print('*********************************')