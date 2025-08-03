def make_sandwich(bread_type, filling, cheese="none", toasted=False):
    # Building the sandwich description
    description = f"You are making a {bread_type} sandwich filled with {filling}."

    # Add cheese detail if it's not 'none'
    if cheese.lower() != "none":
        description += f" It includes {cheese} cheese."

    # Add toast detail
    if toasted:
        description += " The sandwich will be toasted."
    else:
        description += " The sandwich will not be toasted."

    return description
print(make_sandwich("sourdough", "grilled chicken"))
# You are making a sourdough sandwich filled with grilled chicken. The sandwich will not be toasted.

print(make_sandwich("whole grain", "tuna", "swiss", True))
# You are making a whole grain sandwich filled with tuna. It includes swiss cheese. The sandwich will be toasted.
