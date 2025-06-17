class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def view_client(self):
        return (f"client_code={self.client_code}, year={self.year}, "
                f"month={self.month}, duration={self.duration})\n")

fitness_centers = [
    FitnessCenter(client_code="001", year=2025, month=1, duration=30),
    FitnessCenter(client_code="002", year=2025, month=2, duration=15),
    FitnessCenter(client_code="003", year=2025, month=3, duration=34),
    FitnessCenter(client_code="004", year=2025, month=4, duration=50),
    FitnessCenter(client_code="005", year=2025, month=5, duration=70)
]

longest_session = fitness_centers[0]
shortest_session = fitness_centers[0]

for session in fitness_centers:
    if session.duration > longest_session.duration:
        longest_session = session
    if session.duration < shortest_session.duration:
        shortest_session = session

print("Longest session:")
print(longest_session.view_client())

print("Shortest session:")
print(shortest_session.view_client())