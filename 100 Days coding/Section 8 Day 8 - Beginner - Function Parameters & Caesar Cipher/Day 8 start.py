# def greet():
#     print("Hello, Hosam")
#     print("How do you do?")
#     print("isn't the weather nice today?")
# greet()

#function with input
# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print("How do you do?")
#     print("isn't the weather nice today?")

# greet_with_name("Hosam")

#functi with 2 inputs
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

#positional arguments
greet_with("Hosam", "Fayoum")
#keyword arguments
greet_with(location = "Fayoum", name = "Hosam")