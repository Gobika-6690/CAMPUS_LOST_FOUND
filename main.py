from fastapi import FastAPI

app = FastAPI(title="Campus Lost & Found Matcher API")

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Campus Lost & Found Matcher API"
    }

# Add lost item
@app.post("/lost-item")
def add_lost_item(item_name: str, location: str):
    return {
        "status": "success",
        "item": item_name,
        "location": location,
        "type": "Lost"
    }

# Add found items
@app.post("/found-item")
def add_found_item(item_name: str, location: str):
    return {
        "status": "success",
        "item": item_name,
        "location": location,
        "type": "Found"
    }

# Match lost and found items
@app.get("/match")
def match_items(lost_item: str, found_item: str):
    if lost_item.lower() == found_item.lower():
        return {"message": "Possible Match Founded!"}
    else:
        return {"message": "No Match Founded"}