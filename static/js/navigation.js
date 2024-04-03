/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!***********************************!*\
  !*** ./frontend/js/navigation.js ***!
  \***********************************/
$(document).ready(function () {
  // header menu dropdowns (desktop)
  var windowWidth = $(window).width();
  $('.nav-list-item').each(function () {
    var subMenu = $(this).find('ul');
    if (windowWidth > 992) {
      var subMenuHeight = subMenu.outerHeight();
      var basket = $(this).find('.__basket');
      var scrollBtn = '<span class="scroll"><i class="fa-solid fa-chevron-down"></i></span>';
      if (subMenu.length) {
        $(this).hover(function () {
          basket.scrollTop(0);
          if (subMenuHeight >= 400) {
            basket.append(scrollBtn);
          }
        }, function () {
          $('.scroll').remove();
        });
      }
      basket.scroll(function () {
        if (basket.scrollTop() > 1) {
          $('.scroll').fadeOut(300);
        }
      });
    } else {
      $(this).click(function () {
        subMenu.slideToggle();
      });
    }
  });
  $('.burger').click(function () {
    var body = $('body');
    if (!body.hasClass('__mobile')) {
      body.addClass('__mobile');
    } else {
      body.removeClass('__mobile');
    }
  });
  $('.nav-overlay').click(function () {
    var body = $('body');
    body.removeClass('__mobile');
  });
});
/******/ })()
;