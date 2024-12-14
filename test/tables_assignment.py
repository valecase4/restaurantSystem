# Tables Assignment Test 

tables = [
    {
        "ID": 20,
        "Capacity": 4,
    },
    {
        "ID": 22,
        "Capacity": 2
    },
    {
        "ID": 24,
        "Capacity": 4
    },
    {
        "ID": 25,
        "Capacity": 6
    },
    {
        "ID": 26,
        "Capacity": 2
    },
    {
        "ID": 27,
        "Capacity": 2
    },
    {
        "ID": 33,
        "Capacity": 4
    },
    {
        "ID": 34,
        "Capacity": 7
    },
    {
        "ID": 37,
        "Capacity": 7
    },
    {
        "ID": 28,
        "Capacity": 6
    }, 
    {
        "ID": 30,
        "Capacity": 4
    }, 
    {
        "ID": 32,
        "Capacity": 4
    }
]

###################


people = [5, 4, 2, 6, 3, 3, 7, 4, 3, 6]

people = sorted(people, reverse=True)

print(people)

total_places_left = sum([table["Capacity"] for table in tables])

print(total_places_left)

assignments = {}

for group in people:
    for available_table in tables:
        if available_table["Capacity"] >= group:
            assignments[f"{available_table["ID"]}"] = group
            tables.remove(available_table)
            total_places_left = total_places_left - group
            break
        else:
            continue

print("Assegnazione completata: ")
print("\n")
print("Tavoli assegnati: ")

for key, value in assignments.items():
    print(f"Tavolo nr. {key} --> Nr. Persone {value}")

print("\n")
print("Posti liberi: \n")
print(total_places_left)



