from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Used Cars Marketplace API", version="1.0.0")

APP_ENV = os.getenv("APP_ENV", "development")
STUDENT_ID = int(os.getenv("STUDENT_ID", "11"))
SERVICE_NAME = os.getenv("SERVICE_NAME", "used-cars-marketplace")
DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "UAH")


class TestDriveRequest(BaseModel):
    car_id: int
    buyer_name: str
    preferred_date: str


cars = [
    {
        "id": 1101,
        "title": "Volkswagen Golf 2017",
        "seller": "Auto Seller 11",
        "price": 8900,
        "currency": DEFAULT_CURRENCY,
        "status": "active"
    },
    {
        "id": 1102,
        "title": "Toyota Corolla 2018",
        "seller": "Auto Seller 11",
        "price": 10500,
        "currency": DEFAULT_CURRENCY,
        "status": "active"
    },
    {
        "id": 1103,
        "title": "Skoda Octavia 2016",
        "seller": "Auto Seller 11",
        "price": 8200,
        "currency": DEFAULT_CURRENCY,
        "status": "reserved"
    }
]


@app.get("/")
def root():
    return {
        "service": SERVICE_NAME,
        "student_id": STUDENT_ID,
        "environment": APP_ENV,
        "status": "running"
    }


@app.get("/cars")
def get_cars():
    return {
        "student_id": STUDENT_ID,
        "count": len(cars),
        "cars": cars
    }


@app.get("/cars/{car_id}")
def get_car(car_id: int):
    for car in cars:
        if car["id"] == car_id:
            return {
                "student_id": STUDENT_ID,
                "car": car
            }
    return {
        "student_id": STUDENT_ID,
        "error": "Car listing not found"
    }


@app.post("/test-drives")
def create_test_drive(request: TestDriveRequest):
    return {
        "student_id": STUDENT_ID,
        "status": "created",
        "test_drive": {
            "car_id": request.car_id,
            "buyer_name": request.buyer_name,
            "preferred_date": request.preferred_date,
            "seller_confirmation": "pending"
        }
    }
