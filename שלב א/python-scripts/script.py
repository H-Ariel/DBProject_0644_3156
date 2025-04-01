import random
from faker import Faker

fake = Faker()

# פתיחת קובץ לכתיבה
with open('insert_data.sql', 'w') as file:

    # פקודות INSERT עבור טבלת Colony
    for i in range(1, 401):
        name = fake.company()
        established_date = fake.date_this_century()
        file.write(f"INSERT INTO Colony (colony_id, name, established_date) VALUES ({i}, '{name}', '{established_date}');\n")

    # פקודות INSERT עבור טבלת Crew
    for i in range(1, 401):
        name = fake.name()
        role = random.choice(['Commander', 'Engineer', 'Scientist', 'Technician'])
        joined_date = fake.date_this_century()
        colony_id = random.randint(1, 400)
        file.write(f"INSERT INTO Crew (crew_id, name, role, joined_date, colony_id) VALUES ({i}, '{name}', '{role}', '{joined_date}', {colony_id});\n")

    # פקודות INSERT עבור טבלת Researcher
    for i in range(1, 401):
        name = fake.name()
        research_field = random.choice(['AI Research', 'Radiation Studies', 'Astrobiology', 'Geology'])
        crew_id = random.randint(1, 400)
        file.write(f"INSERT INTO Researcher (researcher_id, name, research_field, crew_id) VALUES ({i}, '{name}', '{research_field}', {crew_id});\n")

    # פקודות INSERT עבור טבלת Mission
    for i in range(1, 401):
        name = fake.bs()
        description = fake.sentence()
        start_date = fake.date_this_century()
        colony_id = random.randint(1, 400)
        file.write(f"INSERT INTO Mission (mission_id, name, description, start_date, colony_id) VALUES ({i}, '{name}', '{description}', '{start_date}', {colony_id});\n")

    # פקודות INSERT עבור טבלת Equipment
    for i in range(1, 401):
        name = fake.word()
        purchase_date = fake.date_this_century()
        file.write(f"INSERT INTO Equipment (equipment_id, name, purchase_date) VALUES ({i}, '{name}', '{purchase_date}');\n")

    # פקודות INSERT עבור טבלת Infrastructure
    for i in range(1, 401):
        capacity = random.randint(10, 100)
        infrastructure_type = random.choice(['Habitat', 'Power Station', 'Greenhouse', 'Research Lab'])
        status = random.choice([1, 2, 3])  # 1=Active, 2=Inactive, 3=Under Construction
        colony_id = random.randint(1, 400)
        file.write(f"INSERT INTO Infrastructure (infrastructure_id, capacity, infrastructure_type, status, colony_id) VALUES ({i}, {capacity}, '{infrastructure_type}', {status}, {colony_id});\n")

    # פקודות INSERT עבור טבלת Uses
    for i in range(1, 401):
        mission_id = random.randint(1, 400)
        equipment_id = random.randint(1, 400)
        file.write(f"INSERT INTO Uses (mission_id, equipment_id) VALUES ({mission_id}, {equipment_id});\n")
