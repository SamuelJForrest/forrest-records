// update button
$('.basket-item-update').click(function(e) {
    e.preventDefault();
    let form = $(this).closest('.basket-item-form');
    form.submit();
});

// remove button
$('.basket-item-remove').click(function(e) {
    e.preventDefault();

    let itemId = $(this).attr('id').split('remove_')[1];
    let size = $(this).data('product_size');
    let url = `/bag/remove/${itemId}`;
    let data = {'csrfmiddlewaretoken': csrfToken, 'product_size': size};
    
    $.post(url, data)
    .done(function() {
        location.reload();
    });
});