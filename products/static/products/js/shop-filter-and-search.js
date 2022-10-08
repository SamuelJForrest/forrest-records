// update shop filters
$('#shop_filter').change(function() {
    const selector = $(this);
    const currentUrl = new URL(window.location);

    let selectedVal = selector.val();
    if (selectedVal != 'reset') {
        let sort = selectedVal.split("_")[0];
        let direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set('sort', sort);
        currentUrl.searchParams.set('direction', direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');

        window.location.replace(currentUrl);
    }
});

// open search bar
$(document).click(function(e) {
    let target = $(e.target).attr('id');
    let searchInput = $('#q');
    let searchParent = $('.product-search');

    if (target == 'q') {
        searchParent.addClass('__active');
    } else {
        searchParent.removeClass('__active');
        searchInput.val('');
        searchInput.text('');
    }
});