INSERT INTO Colony (colony_id, name, established_date) VALUES
(1, 'Mars Alpha', '2030-05-14'),
(2, 'Lunar Base', '2028-11-23'),
(3, 'Titan Outpost', '2042-07-01');

INSERT INTO Crew (crew_id, name, role, joined_date, colony_id) VALUES
(1, 'John Smith', 'Commander', '2030-06-01', 1),
(2, 'Alice Brown', 'Engineer', '2028-12-01', 2),
(3, 'Eve Carter', 'Biologist', '2042-08-01', 3);

INSERT INTO Researcher (researcher_id, name, research_field, crew_id) VALUES
(1, 'Dr. Alan Turing', 'AI Research', 1),
(2, 'Dr. Marie Curie', 'Radiation Studies', 2),
(3, 'Dr. Carl Sagan', 'Astrobiology', 3);

INSERT INTO Mission (mission_id, name, description, start_date, colony_id) VALUES
(1, 'Mars Exploration', 'Geological survey', '2031-03-10', 1),
(2, 'Lunar Mining', 'Helium-3 extraction', '2029-05-20', 2),
(3, 'Titan Research', 'Atmospheric study', '2043-01-15', 3);

INSERT INTO Equipment (equipment_id, name, purchase_date) VALUES
(1, 'Rover X1', '2030-02-01'),
(2, 'Drill Z9', '2028-09-15'),
(3, 'Satellite Beacon', '2041-12-10');

INSERT INTO Infrastructure (infrastructure_id, capacity, infrastructure_type, status, colony_id) VALUES
(1, 50, 'Habitat Module', 1, 1),
(2, 30, 'Power Station', 1, 2),
(3, 100, 'Greenhouse', 1, 3);

INSERT INTO Uses (mission_id, equipment_id) VALUES
(1, 1),
(2, 2),
(3, 3);
