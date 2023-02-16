import requests
import csv

URL_TEMPLATE = "https://www.carlist.my/ajax/newreviews?make=Perodua&model=MyVi&page={}"

headers = {
    'authority': 'www.carlist.my',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ms;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/json',
    'dnt': '1',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

reviews = []

for page in range(1, 19):
    url = URL_TEMPLATE.format(page)
    r = requests.get(url, headers=headers)
    data = r.json()["data"]
    reviews.extend(data)

filename = "response.csv"

# Open the CSV file in write mode
with open(filename, "w", newline="") as file:

    # Create a writer object
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["id", "created_at", "updated_at", "deleted_at", "model_year_id", "country_id", "make", "model", "year", "name", "phone", "email", "overal_rating", "performance", "interior_design", "safety", "exterior_design", "title", "details", "uuid", "status", "helpful_count", "user_ip", "user_agent", "created_at_readable"])

    # Write the data rows
    for review in reviews:
        writer.writerow([review["id"], review["created_at"], review["updated_at"], review["deleted_at"], review["model_year_id"], review["country_id"], review["make"], review["model"], review["year"], review["name"], review["phone"], review["email"], review["overal_rating"], review["performance"], review["interior_design"], review["safety"], review["exterior_design"], review["title"], review["details"], review["uuid"], review["status"], review["helpful_count"], review["user_ip"], review["user_agent"], review["created_at_readable"]])
