const $ = window.$;
$(function () {
  $('#add_item').click(function () {
    $('header').toggleClass('red green');
  });
});
