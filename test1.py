name = "sergio"
print(name)

def say_hello():
    print("hello")
    print("I'm inside")


# call the fn
say_hello()
say_hello()

# data structures -> 114

# array js -> list python
prices = [1,2,3,4,5]

# add
prices.append(9)

print(prices)

# sum all the prices
total = 0
for price in prices:
    total += price

print(total)

# dictionary
me = {
    "name": "Sergio",
    "age": 37,
    "hobbies": [],
    "address": {
        "Street": "evergreen",
        "city": "springfield"
    }
}

print(me)

# read
print(me['name'])

# warning: reading a key that does not exist
if "last" in me:
    print(me["last"])

me["age"] = 99

#add keys
me["last"] = "Inzunza"


print("THE END")
