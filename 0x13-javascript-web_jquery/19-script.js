$('#add_item').click(function () {
  let item1 = $('<LI></LI>').text('Item');
  $('UL.my_list').append(item1);
});
