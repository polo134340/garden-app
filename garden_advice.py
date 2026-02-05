SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

SEASON_RECOMMENDATIONS = {
    "summer": ["tomatoes", "basil", "marigolds"],
    "winter": ["kale", "garlic", "winter pansies"],
}


def prompt_choice(label: str, allowed: set[str]) -> str:
    allowed_display = ", ".join(sorted(allowed))
    while True:
        value = input(f"Enter {label} ({allowed_display}): ").strip().lower()
        if value in allowed:
            return value
        print(f"Sorry, '{value}' isn't supported. Please choose: {allowed_display}")


def get_season_advice(season: str) -> str:
    return SEASON_ADVICE.get(season, "No advice for this season.")


def get_plant_advice(plant_type: str) -> str:
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def build_advice(season: str, plant_type: str) -> str:
    return f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"


def get_recommended_plants(season: str) -> list[str]:
    return SEASON_RECOMMENDATIONS.get(season, [])


def main() -> None:
    allowed_seasons = set(SEASON_ADVICE.keys())
    allowed_plant_types = set(PLANT_ADVICE.keys())

    season = prompt_choice("season", allowed_seasons)
    plant_type = prompt_choice("plant type", allowed_plant_types)

    print(build_advice(season, plant_type))

    recommended = get_recommended_plants(season)
    if recommended:
        print("\nRecommended plants for this season: " + ", ".join(recommended))


if __name__ == "__main__":
    main()


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
