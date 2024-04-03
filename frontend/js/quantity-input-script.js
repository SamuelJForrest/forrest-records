function handleDisableEnable(element) {
    const thisElement = element;
    const quantity = element.closest('.product-quantity').find('input[type="number"]');
    const minusBtn = element.closest('.product-quantity').find('.minus-btn');
    const currentValue = parseInt(quantity.val());
    
    const minusDisabled = currentValue < 2;
    minusBtn.prop('disabled', minusDisabled);
}

function checkInitialValue() {
    let quantities = $('.product-quantity');

    quantities.each(function() {
        const thisElement = $(this);
        const quantityInput = thisElement.closest('.product-quantity').find('input[type="number"]');
        const closestMinusButton = thisElement.closest('.product-quantity').find('.minus-btn');
        const currentValue = quantityInput.val();

        if (currentValue == 1) {
            closestMinusButton.prop('disabled', true);
        }
    });
}
checkInitialValue();

function updateQuantityValue(element, direction) {
    const thisElement = element;
    const quantity = element.closest('.product-quantity').find('input[type="number"]');
    const currentValue = parseInt(quantity.val());

    if (direction == 'increment') {
        quantity.val(currentValue + 1);
    } else {
        quantity.val(currentValue - 1);
    }
}

$('.qty-btn').each(function() {
    const thisElement = $(this);

    thisElement.click(function(e) {
        e.preventDefault();

        if (thisElement.hasClass('plus-btn')) {
            updateQuantityValue(thisElement, 'increment');
        } else {
            updateQuantityValue(thisElement, 'decrement');
        }

        handleDisableEnable(thisElement);
    });
});
