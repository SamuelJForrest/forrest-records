$(document).ready(function() {

    // header menu dropdowns (desktop)
    const windowWidth = $(window).width();

    $('.nav-list-item').each(function() {
        const subMenu = $(this).find('ul');

        if (windowWidth > 992) {
            const subMenuHeight = subMenu.outerHeight();
            const basket = $(this).find('.__basket');
            const scrollBtn = '<span class="scroll"><i class="fa-solid fa-chevron-down"></i></span>';
        
            if (subMenu.length) {
                $(this).hover(function() {
                    basket.scrollTop(0);
                    if (subMenuHeight >= 400) {
                        basket.append(scrollBtn);
                    }
                }, function() {
                    $('.scroll').remove();
                });
            }

            basket.scroll(function() {
                if (basket.scrollTop() > 1) {
                    $('.scroll').fadeOut(300);
                }
            });
        } else {
            $(this).click(function() {
                subMenu.slideToggle();
            });
        }
    });

    $('.burger').click(function() {
        const body = $('body');

        if (!body.hasClass('__mobile')) {
            body.addClass('__mobile');
        } else {
            body.removeClass('__mobile');
        }
    });

    $('.nav-overlay').click(function() {
        const body = $('body');

        body.removeClass('__mobile');
    })
});
