import csv

class Country:
    def __init__(self, name, gdp, life_expectancy, population_density, population):
        
        # Country 객체의 속성을 초기화
        self.name = name
        # GDP에서 $ 기호와 콤마를 제거한 후 float로 변환
        self.gdp = float(gdp.replace('$', '').replace(',', '')) if gdp else 0.0
        self.life_expectancy = float(life_expectancy) if life_expectancy else 0.0
        # 인구 밀도에서 콤마를 제거한 후 int로 변환
        self.population_density = int(population_density.replace(',', '')) if population_density else 0
        # 인구에서도 콤마를 제거한 후 int로 변환
        self.population = int(population.replace(',', '')) if population else 0

class CountryStatistics:
    def __init__(self, csv_file):
        # CountryStatistics 객체를 초기화하고 데이터를 로드
        self.countries = []
        self.load_data(csv_file)
    
    def load_data(self, csv_file):
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                country = Country(
                    row['Country'],
                    row['GDP'],  # GDP에서 $와 , 제거는 Country 클래스에서 처리됨
                    row['Life expectancy'],
                    row['Density (P/Km2)'],  # 인구 밀도에서 콤마 제거는 Country 클래스에서 처리됨
                    row['Population']
                )
                self.countries.append(country)
    
    def top_5_gdp(self):
        # GDP 기준으로 상위 5개 국가를 반환
        sorted_countries = sorted(self.countries, key=lambda x: x.gdp, reverse=True)[:5]
        return [(c.name, f"{c.gdp:,.0f}") for c in sorted_countries]
    
    def top_5_life_expectancy(self):
        # 기대수명 기준으로 상위 5개 국가를 반환
        sorted_countries = sorted(self.countries, key=lambda x: x.life_expectancy, reverse=True)[:5]
        return [(c.name, c.life_expectancy) for c in sorted_countries]
    
    def countries_by_density(self):
        # 인구 밀도 기준으로 상위 5개 국가를 반환
        sorted_countries = sorted(self.countries, key=lambda x: x.population_density, reverse=True)[:5]
        return [(c.name, c.population_density) for c in sorted_countries]
    
    def average_population(self):
        # 모든 국가의 평균 인구를 계산
        total_population = sum(c.population for c in self.countries)
        average = total_population / len(self.countries) if self.countries else 0
        return f"{average:,.0f}"
    
# try except