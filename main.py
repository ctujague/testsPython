"""
print("Tutu rules")
print(" ")
"""
# Variables Globales
x = 12
name_of_unit = "pieds"

# je fais mon calcul
result = x * 5


# This is a function


def days_to_units(nb_of_days):
    sortie = ""
    sortie = f"Calcul pour {nb_of_days} jours: {nb_of_days*result} {name_of_unit}"
    return sortie


def validate_and_execute(num_of_days):
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_string = days_to_units(user_input_number)
            print(calculated_string)
        elif user_input_number == 0:
            print("T as mis zero")
        else:
            print("T'as mis un negatif")
    except ValueError:
        print("T as merdé, on veut un nombre entier positif non nul")

"""
user_input = ""

while user_input != "exit":
    # Demande une valeur au clavier
    user_input = input("Enter number or list: \n")
    print(type(user_input))
    print(user_input.split(", "))
    for num_of_days_elements in user_input.split(", "):
        # Execute traitement
        validate_and_execute(num_of_days_elements)


print(" ")
print("Tutu leaves")
"""
