students = [
    {"name": "John Smith", "birth_year": 2005, "address": "12 Green St",
     "grades": {"Math": 85, "English": 90, "Physics": 78}},
    {"name": "Emily Johnson", "birth_year": 2006, "address": "34 Blue Rd",
     "grades": {"Math": 92, "English": 88, "Physics": 95}},
    {"name": "Michael Brown", "birth_year": 2004, "address": "56 Red Ave",
     "grades": {"Math": 70, "English": 65, "Physics": 72}}
]

student_name=input("Choose a Student's Name: ")

def information(name):
    for s in students:
        if name in s["name"].lower()  :
            print(
                f"Student {s['name']} was born in year {s['birth_year']}, "
                f"lives at {s['address']}, and his grades are: "
                f"Math {s['grades']['Math']}, English {s['grades']['English']} "
                f"and Physics {s['grades']['Physics']}."
            )

            return
    print(f"Student with name '{name}' was not found.")

information(student_name)
