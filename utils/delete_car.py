import requests

BASE_URL = "http://127.0.0.1:5000/cars"

def delete_car(id):
    url = "%s/%s" % (BASE_URL, id)
    response = requests.delete(url)
    if response.status_code == 204:
        print("Deleted Successful")
    else:
        print("Deleted failed")

if __name__ == "__main__":
    print("Delete a car by filling out the prompts below: ")
    id = input ("ID:")
    delete_car(id)
