-- List all cities contained in the database
SELECT DISTINCT cities.id, cities.name, states.name FROM states JOIN cities WHERE cities.state_id = state_id ORDER BY cities.id ASC;
