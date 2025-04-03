# Python script to connect to PostgreSQL database and insert initial data

import random
from faker import Faker
import psycopg2

fake = Faker()

# init connection
print('connect...')
conn = psycopg2.connect(
    host='host.docker.internal', #"172.17.0.2",
    port="5432",
    database="postgres",
    user="myuser",
    password="mypassword"
)
cursor = conn.cursor()

# Run command on SQL Server
def insert_data(query, values=()):
    cursor.execute(query, values)
    conn.commit()


print('insert data')

# INSERT Colony
print('Colony')
for i in range(1, 401):
    name = fake.company()
    established_date = fake.date_this_century()
    insert_data(f"INSERT INTO Colony (colony_id, name, established_date) VALUES ({i}, '{name}', '{established_date}');\n")

# INSERT Crew
print('Crew')
for i in range(1, 401):
    name = fake.name()
    role = random.choice(['Commander', 'Engineer', 'Scientist', 'Technician'])
    joined_date = fake.date_this_century()
    colony_id = random.randint(1, 400)
    insert_data(f"INSERT INTO Crew (crew_id, name, role, joined_date, colony_id) VALUES ({i}, '{name}', '{role}', '{joined_date}', {colony_id});\n")

# INSERT Researcher
# NOTE: load from CSV
#print('Researcher')
#for i in range(1, 401):
#    name = fake.name()
#    research_field = random.choice(['AI Research', 'Radiation Studies', 'Astrobiology', 'Geology'])
#    crew_id = random.randint(1, 400)
#    insert_data(f"INSERT INTO Researcher (researcher_id, name, research_field, crew_id) VALUES ({i}, '{name}', '{research_field}', {crew_id});\n")

# INSERT Mission
print('Mission')
for i in range(1, 401):
    name = fake.bs()
    description = fake.sentence()
    start_date = fake.date_this_century()
    colony_id = random.randint(1, 400)
    insert_data(f"INSERT INTO Mission (mission_id, name, description, start_date, colony_id) VALUES ({i}, '{name}', '{description}', '{start_date}', {colony_id});\n")

# INSERT Equipment
print('Equipment')
for i in range(1, 401):
    name = fake.word()
    purchase_date = fake.date_this_century()
    insert_data(f"INSERT INTO Equipment (equipment_id, name, purchase_date) VALUES ({i}, '{name}', '{purchase_date}');\n")

# INSERT Infrastructure
print('Infrastructure')
for i in range(1, 401):
    capacity = random.randint(10, 100)
    infrastructure_type = random.choice(['Habitat', 'Power Station', 'Greenhouse', 'Research Lab'])
    status = random.choice([1, 2, 3])  # 1=Active, 2=Inactive, 3=Under Construction
    colony_id = random.randint(1, 400)
    insert_data(f"INSERT INTO Infrastructure (infrastructure_id, capacity, infrastructure_type, status, colony_id) VALUES ({i}, {capacity}, '{infrastructure_type}', {status}, {colony_id});\n")

# INSERT Uses
print('Uses')
uses = set()
while len(uses) < 400:
    mission_id = random.randint(1, 400)
    equipment_id = random.randint(1, 400)
    uses.add((mission_id,equipment_id))

for mission_id, equipment_id in uses:
    insert_data(f'INSERT INTO Uses (mission_id, equipment_id) VALUES ({mission_id},{equipment_id});\n')


print('END')
