from datetime import datetime
from random import choice

contractor_data = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "123-456-7890",
        "address": "123 Main St, City, State",
        "service_provided": "Harvesting Services",
    },
    {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "phone_number": "555-555-5555",
        "address": "456 Elm Ave, Town, State",
        "service_provided": "Irrigation Systems",
    },
    {
        "name": "Mark Williams",
        "email": "mark@example.com",
        "phone_number": "111-222-3333",
        "address": "789 Oak St, County, State",
        "service_provided": "Pest Control",
    },
]

farmer_data = [
    {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "phone_number": "987-654-3210",
        "address": "456 Farm Rd, Village, State",
    },
    {
        "name": "Michael Brown",
        "email": "michael@example.com",
        "phone_number": "222-333-4444",
        "address": "789 Orchard Ln, Countryside, State",
    },
    {
        "name": "Sarah Green",
        "email": "sarah@example.com",
        "phone_number": "444-555-6666",
        "address": "1234 Vine St, Rural, State",
    },
]

farm_data = [
    {
        "name": "Green Acres Farm",
        "farmer_id": 1,
        "size": 100.0,
        "city": "Springfield",
        "state": "Illinois",
        "zip_code": "62701",
    },
    {
        "name": "Harvest Moon Ranch",
        "farmer_id": 2,
        "size": 75.0,
        "city": "Fargo",
        "state": "North Dakota",
        "zip_code": "58102",
    },
    {
        "name": "Sunrise Fields",
        "farmer_id": 1,
        "size": 120.0,
        "city": "Boise",
        "state": "Idaho",
        "zip_code": "83702",
    },
    {
        "name": "Golden Grain Farm",
        "farmer_id": 3,
        "size": 50.0,
        "city": "Sacramento",
        "state": "California",
        "zip_code": "95814",
    },
    {
        "name": "Sweet Meadows",
        "farmer_id": 4,
        "size": 200.0,
        "city": "Austin",
        "state": "Texas",
        "zip_code": "78701",
    },
    {
        "name": "Oak Valley Ranch",
        "farmer_id": 5,
        "size": 80.0,
        "city": "Atlanta",
        "state": "Georgia",
        "zip_code": "30303",
    },
    {
        "name": "Harmony Acres",
        "farmer_id": 6,
        "size": 150.0,
        "city": "Denver",
        "state": "Colorado",
        "zip_code": "80202",
    },
    {
        "name": "Evergreen Pastures",
        "farmer_id": 7,
        "size": 90.0,
        "city": "Seattle",
        "state": "Washington",
        "zip_code": "98101",
    },
    {
        "name": "Blue Sky Farm",
        "farmer_id": 8,
        "size": 180.0,
        "city": "Portland",
        "state": "Oregon",
        "zip_code": "97201",
    },
    {
        "name": "Golden Wheat Fields",
        "farmer_id": 9,
        "size": 120.0,
        "city": "Kansas City",
        "state": "Missouri",
        "zip_code": "64101",
    },
]

crop_data = [
    {
        "name": "Corn",
        "variety": "Yellow",
        "planting_season": "summer",
        "harvest_season": "autumn",
    },
    {
        "name": "Wheat",
        "variety": "Hard Red Winter",
        "planting_season": "fall",
        "harvest_season": "spring",
    },
    {
        "name": "Tomatoes",
        "variety": "Roma",
        "planting_season": "spring",
        "harvest_season": "summer",
    },
    {
        "name": "Apples",
        "variety": "Gala",
        "planting_season": "spring",
        "harvest_season": "fall",
    },
    {
        "name": "Soybeans",
        "variety": "Roundup Ready",
        "planting_season": "summer",
        "harvest_season": "autumn",
    },
    {
        "name": "Cotton",
        "variety": "Pima",
        "planting_season": "spring",
        "harvest_season": "fall",
    },
    {
        "name": "Potatoes",
        "variety": "Russet",
        "planting_season": "spring",
        "harvest_season": "summer",
    },
    {
        "name": "Oranges",
        "variety": "Valencia",
        "planting_season": "winter",
        "harvest_season": "spring",
    },
    {
        "name": "Peppers",
        "variety": "Bell",
        "planting_season": "summer",
        "harvest_season": "autumn",
    },
    {
        "name": "Grapes",
        "variety": "Thompson Seedless",
        "planting_season": "spring",
        "harvest_season": "summer",
    },
]

activity_data = []

for _ in range(50):
    activity = {
        "activity_type": choice(["planting", "watering", "fertilizing", "harvesting"]),
        "crop_id": choice(range(1, len(crop_data) + 1)),
        "farmer_id": choice(range(1, len(farmer_data) + 1)),
        "farm_id": choice(range(1, len(farm_data) + 1)),
        "contractor_id": choice(range(1, len(contractor_data) + 1)),
        "date_time": datetime(2023, 7, choice(range(1, 31)), choice(range(0, 24)), choice(range(0, 60))),
        "notes": "Random activity notes.",
    }
    activity_data.append(activity)

fixtures_data = {
    "Contractor": contractor_data,
    "Farmer": farmer_data,
    "Farm": farm_data,
    "Crop": crop_data,
    "Activity": activity_data,
}
