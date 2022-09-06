#Functions with output
def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return
    return f"{first_name.title()} {last_name.title()}"

print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))