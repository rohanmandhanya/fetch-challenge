import math
from datetime import datetime


def calculate_points(receipt):
    points = 0

    # 1. One point for every alphanumeric character in the retailer name.
    retailer_name = receipt.retailer
    alphanumeric_chars = sum(c.isalnum() for c in retailer_name)
    points += alphanumeric_chars

    # 2. 50 points if the total is a round dollar amount with no cents.
    total = float(receipt.total)
    if total.is_integer():
        points += 50

    # 3. 25 points if the total is a multiple of 0.25.
    if total % 0.25 == 0:
        points += 25

    # 4. 5 points for every two items on the receipt.
    items = receipt.items
    points += (len(items) // 2) * 5

    # 5. If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in items:
        description_length = len(item.shortDescription.strip())
        if description_length % 3 == 0:
            price = float(item.price)
            points += math.ceil(price * 0.2)

    # 6. 6 points if the day in the purchase date is odd.
    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        points += 6

    # 7. 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
    if purchase_time.hour == 14 and purchase_time.minute >= 0:
        points += 10

    return points
