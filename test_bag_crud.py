from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app=app)

def test_home():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the Mukesh's bag shop!"}
        
        
        
# def test_add_new_bag():
#     with TestClient(app) as client:
#         response = client.post("/bag/", json={"id": 2, "brand": "VIP", "capacity": 25, "colour": "Black"})
#         assert response.status_code == 201
        
#         body = response.json()
#         assert body.get("id") == 2
#         assert body.get("brand") == "VIP"
#         assert body.get("capacity") == 25
#         assert body.get("colour") == "Black"