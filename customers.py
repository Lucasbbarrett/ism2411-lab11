# Exercise 1
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 850,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2
customer["phone"] = "202-555-0146"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError: {error}")

# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

# .items() gives me both the key and its value. A plain loop gives me just the key.
for key in customer:
    print(key)

# Exercise 5
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
tier = customer["tier"]
rate = tier_discounts.get(tier, 0)
purchase = 200
final_price = purchase * (1 - rate)
print(f"{tier} | {rate:.0%} discount | final price ${final_price:.2f}")

# Exercise 6
customers = [
    customer,
    {"name": "Mateo", "email": "mateo@example.com", "tier": "silver", "ytd_spend": 420},
    {"name": "Nina", "email": "nina@example.com", "tier": "bronze", "ytd_spend": 90},
]
purchase = 300
for record in customers:
    tier = record["tier"]
    discount = purchase * tier_discounts.get(tier, 0)
    print(f"{record['name']} | {tier} | ${discount:.2f} off")
