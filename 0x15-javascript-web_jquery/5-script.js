const element = $('<li></li>').text('Item');

$('div#add_item').on('click', function () {
  $('ul.my_list').append(element);
});
