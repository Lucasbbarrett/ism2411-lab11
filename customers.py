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
