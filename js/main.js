$(document).ready(function () {
  $('.btnIcon').on('click', function () {
    $('nav ul').toggleClass('show');
  });

  $('nav li').on('click', function () {
    $('header nav ul').removeClass('show');
  });
});


