from country_statistics import CountryStatistics

stats = CountryStatistics('PA3 006 - Country Statistics/world-data-2023.csv')

print(stats.top_5_gdp())
print(stats.top_5_life_expectancy())
print(stats.countries_by_density())
print(f'{stats.average_population()} people')