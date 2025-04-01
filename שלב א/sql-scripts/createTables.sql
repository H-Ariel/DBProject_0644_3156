CREATE TABLE Colony
(
  colony_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  established_date DATE NOT NULL,
  PRIMARY KEY (colony_id)
);

CREATE TABLE Crew
(
  crew_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL,
  joined_date DATE NOT NULL,
  colony_id INT NOT NULL,
  PRIMARY KEY (crew_id),
  FOREIGN KEY (colony_id) REFERENCES Colony(colony_id)
);

CREATE TABLE Researcher
(
  researcher_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  research_field VARCHAR(255) NOT NULL,
  crew_id INT NOT NULL,
  PRIMARY KEY (researcher_id),
  FOREIGN KEY (crew_id) REFERENCES Crew(crew_id)
);

CREATE TABLE Mission
(
  mission_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  colony_id INT NOT NULL,
  PRIMARY KEY (mission_id),
  FOREIGN KEY (colony_id) REFERENCES Colony(colony_id)
);

CREATE TABLE Equipment
(
  equipment_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  purchase_date DATE NOT NULL,
  PRIMARY KEY (equipment_id)
);

CREATE TABLE Infrastructure
(
  infrastructure_id INT NOT NULL,
  capacity INT NOT NULL,
  infrastructure_type VARCHAR(255) NOT NULL,
  status INT NOT NULL,
  colony_id INT NOT NULL,
  PRIMARY KEY (infrastructure_id),
  FOREIGN KEY (colony_id) REFERENCES Colony(colony_id)
);

CREATE TABLE Uses
(
  mission_id INT NOT NULL,
  equipment_id INT NOT NULL,
  PRIMARY KEY (mission_id, equipment_id),
  FOREIGN KEY (mission_id) REFERENCES Mission(mission_id),
  FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id)
);