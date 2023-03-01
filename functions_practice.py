def hello():
    print("Hello Ben")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(lst):
    if not lst:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + lst[0])
        for i in range(1, len(lst)):
            print("Next I eat " + lst[i])

hello()

my_list = pack("water", "sandwich", "chips")
print(my_list)

my_food = ["sandwich", "chips", "cookie"]
eat_lunch(my_food)
