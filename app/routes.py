from flask import Flask, request
from app.database import car

app = Flask(__name__)

# @app.get("/")
@app.get("/cars")
def get_all_cars():
    out = {
        "cars": car.scan()

    }
    return out

@app.get("/cars/<int:pk>")
def get_car_by_id(pk):
    single_car = car.select_by_id(pk)
    out = { "ok": True }
    if single_car:
        out["car"] = single_car
        return out
    out["ok"] = False
    out['message'] = "Car not found"
    return out, 404

@app.post("/cars")
def create_car():
    raw_data = request.json
    car.insert(raw_data)
    return "", 204

@app.put("/cars/<int:pk>")
def update_car(pk):
    car.detele_by_id(pk)
    return "", 204
