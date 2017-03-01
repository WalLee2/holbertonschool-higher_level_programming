-- Importing database dump and listing all shows contained in the dump file
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;
