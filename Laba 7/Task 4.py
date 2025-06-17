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
    FitnessCenter("001", 2025, 1, 30),
    FitnessCenter("002", 2025, 2, 15),
    FitnessCenter("003", 2025, 3, 34),
    FitnessCenter("004", 2025, 4, 50),
    FitnessCenter("005", 2025, 5, 70)
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