const $ = window.$;

$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (jsonData, requestStatus) {
    if (requestStatus === 'success') {
      const movies = jsonData.results;
      for (const i in movies) {
        $('#list_movies').append('<li>' + movies[i].title + '<li/>');
      }
    }
  });
});
