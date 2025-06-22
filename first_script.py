print("Hello from my first Python script!")
name = "Khoa"
print(f"Nice to meet you, {name}!")
print(len(str(304023)))
lottery = [34, 56, 21, 66, 234]
print(lottery)
len(lottery)
lottery.sort()
print(lottery)
lottery.sort(reverse=True)
print(lottery)
print(lottery[0])
print(lottery[-1])
lottery.pop(-1)
print(lottery)
participant = {"name": "Ola", "country": "Poland", "favorite_numbers": [7, 42, 92]}
print(participant["name"])
participant["country"] = "Germany"
print(participant["country"])


def hello(name):
    print(f"Hello, {name}!")


hello(name)

boys = ["Khoa", "tom", "john"]
for boy in boys:
    hello(boy)
    print("Next")
