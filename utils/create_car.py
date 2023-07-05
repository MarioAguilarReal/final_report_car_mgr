import requests

BASE_URL = "http://127.0.0.1:5000/cars"

def create_car(type_car, color, license, owner_last_name, owner_first_name):
    car_data = {
        "type_car": type_car,
        "color": color,
        "license": license,
        "owner_last_name": owner_last_name,
        "owner_first_name": owner_first_name
    }
    response = requests.post(BASE_URL, json = car_data)
    if response.status_code == 204:
        print("Creation Successfull")
    else:
        print("Creation Failed")

if __name__ == "__main__":
    print("Create a Task by filling out the propmts below:")
    type_car = input("Type_car: ")
    color = input("Color: ")
    license = input("LLicense plate: ")
    owner_last_name = input("Last Name: ")
    owner_first_name = input("First Name: ")
    create_car(type_car, color, license, owner_last_name, owner_first_name)
