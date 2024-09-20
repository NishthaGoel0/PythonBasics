# Lambda Expression - Function accepting function as parameter/argument
def get_full_name (first_name, last_name, formatter):
    return formatter(first_name, last_name)

first_name = input("First Name:")
last_name = input("Last Name:")

full_name = get_full_name(first_name,last_name,lambda first_name, last_name: f"{first_name} {last_name}")
print(full_name)

full_name = get_full_name(first_name,last_name,lambda first_name, last_name: f"{last_name} {first_name}")
print(full_name)