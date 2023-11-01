$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'Get',
  success: function (data) {
    const movies = data.results;
    $.each(movies, function (i, movie) {
      const element = $('<li></li>').text(movie.title);
      $('ul#list_movies').append(element);
    });
  }
});
