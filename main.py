from praktikum import exercise_one, exercise_two, exercise_three
from database import DatabaseConnection
# Create an instance of DatabaseConnection
db = DatabaseConnection()
print("Latihan 1 dan praktikum")
exercise_one(db)
print("\n Latihan 2")
exercise_two(db)
print("\n Latihan 3")
exercise_three()

# Close the database connection
db.close_connection()
