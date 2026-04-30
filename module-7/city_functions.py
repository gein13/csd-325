#Scott Chamberlain
#4/30/2026
#M7.2 Assignment

def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country}, - Population: {population}, {language}"
    elif population:
        return f"{city}, {country}, - Poplation: {population}"
    else:
        return f"{city}, {country}"

if __name__ == "__main__":
# Call the function at least three times
    print(city_country("Toronto", "Canada"))
    print(city_country("Gothenburg", "Sweden", 649847))
    print(city_country("Helsinki", "Finland", 600000, "Finnish"))
    print(city_country("Minneapolis", "USA", 427499, "English"))