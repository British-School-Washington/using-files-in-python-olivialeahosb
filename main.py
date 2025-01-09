# Open the text file containing the list of countries
with open('countries.txt', 'r') as file:
    # Read all lines from the file and store them in a list
    countries = file.readlines()
 
# Remove any extra whitespace (like newline characters) from each line
countries = [country.strip() for country in countries]
 
# Get the count of countries
country_count = len(countries)
 
# Output the number of countries
print(f"There are {country_count} countries listed.")
 
print(countries[6])
 
print(countries[75])
 
over5 = 0
 
less5 = 0
 
over10 = 0
 
for country in countries:
    if len(country) > 5:
        over5 = over5+1
 
print(over5)
 
for country in countries:
    if len(country) < 5:
        less5 = less5+1
 
print(less5)
 
for country in countries:
    if len(country) > 10:
        over10 = over10+1
 
print(less5)