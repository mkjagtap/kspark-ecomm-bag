from fastapi import FastAPI
from bag import Bag

app = FastAPI()
bag_list = []

@app.get("/")
def home():
    print(f"inside home function")
    return {"message": "Welcome to the Mukesh's bag shop!"}

@app.post("/new-bag")
def add_new_bag(bag: Bag):
    print(f"inside add new bag method")
    bag_list.append(bag.dict())
    return bag_list

@app.get("/bags")
def get_bags():
    print(f"inside get bag")
    return {"availble_bags": bag_list}