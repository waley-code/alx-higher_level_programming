$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json',
    success: function(data) {
      $.each(data.results, function(i, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });