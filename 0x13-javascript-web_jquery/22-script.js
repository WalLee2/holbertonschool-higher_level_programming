$.get('http://swapi.co/api/films?format=json', function(data) {
    $.each(data.results, function(key, value) {
	$('#list_movies').append($('<li></li>')).text(value.title);
};
