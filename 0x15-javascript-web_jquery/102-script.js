$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const langCode = $('input#language_code').value();
    const baseUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + langCode;
    $.getJSON(baseUrl, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
