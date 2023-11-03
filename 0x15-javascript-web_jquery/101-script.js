$(document).ready(function () {
  const item = $('<li></li>').text('Item');
  $('div#add_item').on('click', function () {
    $('ul.my_list').append(item);
  });
  $('div#remove_item').on('click', function () {
    $('ul.my_list li:last-child').remove();
  });
  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
