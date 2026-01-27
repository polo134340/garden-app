ALLOWED_SEASONS = {"summer", "winter"}
ALLOWED_PLANT_TYPES = {"flower", "vegetable"}


def prompt_choice(label: str, allowed: set[str]) -> str:
    allowed_display = ", ".join(sorted(allowed))
    while True:
        value = input(f"Enter {label} ({allowed_display}): ").strip().lower()
        if value in allowed:
            return value
        print(f"Sorry, '{value}' isn't supported. Please choose: {allowed_display}")


# Prompt user for the season and plant type
season = prompt_choice("season", ALLOWED_SEASONS)
plant_type = prompt_choice("plant type", ALLOWED_PLANT_TYPES)

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
