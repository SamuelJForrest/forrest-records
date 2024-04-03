/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!**********************************************!*\
  !*** ./frontend/js/quantity-input-script.js ***!
  \**********************************************/
function handleDisableEnable(element) {
  var thisElement = element;
  var quantity = element.closest('.product-quantity').find('input[type="number"]');
  var minusBtn = element.closest('.product-quantity').find('.minus-btn');
  var currentValue = parseInt(quantity.val());
  var minusDisabled = currentValue < 2;
  minusBtn.prop('disabled', minusDisabled);
}
function checkInitialValue() {
  var quantities = $('.product-quantity');
  quantities.each(function () {
    var thisElement = $(this);
    var quantityInput = thisElement.closest('.product-quantity').find('input[type="number"]');
    var closestMinusButton = thisElement.closest('.product-quantity').find('.minus-btn');
    var currentValue = quantityInput.val();
    if (currentValue == 1) {
      closestMinusButton.prop('disabled', true);
    }
  });
}
checkInitialValue();
function updateQuantityValue(element, direction) {
  var thisElement = element;
  var quantity = element.closest('.product-quantity').find('input[type="number"]');
  var currentValue = parseInt(quantity.val());
  if (direction == 'increment') {
    quantity.val(currentValue + 1);
  } else {
    quantity.val(currentValue - 1);
  }
}
$('.qty-btn').each(function () {
  var thisElement = $(this);
  thisElement.click(function (e) {
    e.preventDefault();
    if (thisElement.hasClass('plus-btn')) {
      updateQuantityValue(thisElement, 'increment');
    } else {
      updateQuantityValue(thisElement, 'decrement');
    }
    handleDisableEnable(thisElement);
  });
});
/******/ })()
;