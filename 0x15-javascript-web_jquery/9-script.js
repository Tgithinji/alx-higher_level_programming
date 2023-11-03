$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    succcess: function (data) {
      $('div#hello').value(data.hello);
    }
  });
});
