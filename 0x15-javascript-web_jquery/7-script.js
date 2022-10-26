const $ = window.$;

$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (jsonData, requestStatus) {
    if (requestStatus === 'success') {
      $('#character').text(jsonData.name);
    }
  });
});
