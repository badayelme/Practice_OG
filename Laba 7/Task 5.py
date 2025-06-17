class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

fitness_centers = [
    FitnessCenter("001", 2022, 1, 13),
    FitnessCenter("002", 2022, 2, 43),
    FitnessCenter("003", 2022, 3, 72),
    FitnessCenter("004", 2023, 4, 36),
    FitnessCenter("005", 2023, 5, 94),
    FitnessCenter("006", 2023, 6, 57),
    FitnessCenter("007", 2024, 7, 82),
    FitnessCenter("008", 2024, 8, 67),
    FitnessCenter("009", 2024, 9, 74),
    FitnessCenter("010", 2025, 10, 99)
]

yearly_durations = {}
for i in fitness_centers:
    if i.year in yearly_durations:
        yearly_durations[i.year] += i.duration
    else:
        yearly_durations[i.year] = i.duration

max_duration = 0
max_year = 0

for year, duration in yearly_durations.items():
    if duration > max_duration:
        max_duration = duration
        max_year = year

print(f"Год с наибольшей суммарной продолжительностью: {max_year}, Продолжительность: {max_duration}")