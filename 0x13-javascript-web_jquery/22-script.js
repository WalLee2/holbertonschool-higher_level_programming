$.getJSON('http://swapi.co/api/films?format=json', function (data) {
  $.each(data.results, function (key, value) {
    $('#list_movies').append($('<LI></LI>')).text(value.title);
  });
});
