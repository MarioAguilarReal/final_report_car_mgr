import requests

BASE_URL = "http://127.0.0.1:5000/cars"

def update_car(id, type_car, color, license, owner_last_name, owner_first_name):
    car_data = {
        "type_car": type_car,
        "color": color,
        "license": license,
        "owner_last_name": owner_last_name,
        "owner_first_name": owner_first_name
    }

    url = "%s/%s" % (BASE_URL, id)

    response = requests.put(url, json = car_data)
    if response.status_code == 204:
        print("Updated Successful")
    else:
        print("Updated failed")

    if __name__ == "__main__":
        print("Update a car by filling out the prompts below: ")
        id = input("ID: ")
        type_car = input("Type_car: ")
        color = input("Color: ")
        license = input("License plate: ")
        owner_last_name = input("Last name: ")
        owner_first_name = input("First Name: ")
        update_car(id, type_car, color, license, owner_last_name, owner_first_name)
