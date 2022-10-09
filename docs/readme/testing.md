# Testing

## Table of contents

## Code validation

### HTML Validation

The following pages were validated using the [Markup Validation Service](https://validator.w3.org/)

| File | Result | Report |
| ---- | --- | ---- |
| / (home) | 0 errors, 0 warnings | [Report](/docs/readme/testing/homepage-html-report.png) |
| /accounts/login | 0 errors, 0 warnings | [Report](/docs/readme/testing/login-html-report.png) |
| /accounts/logout | 0 errors, 0 warnings | [Report](/docs/readme/testing/logout-html-report.png) |
| /accounts/signup | 0 errors, 0 warnings | [Report](/docs/readme/testing/register-html-report.png) |
| /artists | 0 errors, 0 warnings | [Report](/docs/readme/testing/artists-html-report.png) |
| /artists/add/artists | 0 warnings, 0 errors | [Report](/docs/readme/testing/add-artist-html-report.png) |
| /artists/edit/artists/<id> | 0 warnings, 0 errors | [Report](/docs/readme/testing/edit-artist-html-report.png) |
| /artists/artists/warning/<id> | 0 warnings, 0 errors | [Report](/docs/readme/testing/delete-artist-html-report.png) |
| /bag | 0 errors, 0 warnings | [Report](/docs/readme/testing/bag-html-report.png) |
| /blog | 0 errors, 0 warnings | [Report](/docs/readme/testing/blog-html-report.png) |
| /blog/<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/blog-single-html-report.png) |
| /blog/add/blog | 0 errors, 0 warnings | [Report](/docs/readme/testing/add-blog-html-report.png) |
| /blog/edit/blog/<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/edit-blog-html-report.png) |
| /blog/blog/warning/<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/delete-blog-html-report.png) |
| /checkout | 0 errors, 0 warnings | [Report](/docs/readme/testing/checkout-html-report.png) |
| /checkout/checkout/success/<order_number> | 0 errors, 0 warnings | [Report](/docs/readme/testing/checkout-success-html-report.png) |
| /checkout/orders/all | 0 errors, 0 warnings | [Report](/docs/readme/testing/checkout-orders-all-html-report.png) |
| /contact | 0 errors, 0 warnings | [Report](/docs/readme/testing/contact-html-report.png) |
| /contact/inbox | 0 errors, 0 warnings | [Report](/docs/readme/testing/contact-inbox-html-reports.png) |
| /products | 0 errors, 0 warnings | [Report](/docs/readme/testing/products-html-report.png) |
| /products/? (query) | 0 errors, 0 warnings | [Report](/docs/readme/testing/product-query-html-report.png) |
| /products/<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/product-single-html-report.png) |
| /products/add/album | 0 errors, 0 warnings | [Report](/docs/readme/testing/add-album-html-report.png) |
| /products/edit/album/<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/edit-album-html-report.png) |
| /products/album/warning<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/delete-album-html-report.png) |
| /products/add/merch | 0 errors, 0 warnings | [Report](/docs/readme/testing/add-merch-html-report.png) |
| /products/edit/merch<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/edit-merch-html-report.png) |
| /products/merch/warning<id> | 0 errors, 0 warnings | [Report](/docs/readme/testing/delete-merch-html-report.png) |
| /profile | 0 errors, 0 warnings | [Report](/docs/readme/testing/profile-html-report.png) |
| /profile/all | 0 errors, 0 warnings | [Report](/docs/readme/testing/profile-all-html-report.png) |
| /profile/order/history/<order_number> |0 errors, 0 warnings | [Report](/docs/readme/testing/past-order-html-report.png) |

### CSS Validation

The following files were tested using [CSS Validation Service](https://jigsaw.w3.org/css-validator/)

| File | Result | Report |
| ---- | --- | ---- |
| /static/css/base.css | 0 warnings, 0 errors | [Report](/docs/readme/testing/base-css-report.png) |
| /checkout/static/checkout/css/checkout.css | 0 warnings, 0 errors | [Report](/docs/readme/testing/checkout-css-report.png) |
| /profiles/static/profiles/css/profiles.css | 0 warnings, 0 errors | [Report](/docs/readme/testing/profiles-css-report.png) |

### JSHints

The following files were tested using [JSHint](https://jshint.com/)

| File | Result | Report |
| ---- | --- | ---- |
| /static/js/bootstrap.js | 0 warnings, 0 errors | [Report](/docs/readme/testing/bootstrap-js-report.png) |
| /static/js/navigation.js | 0 warnings, 0 errors | [Report](/docs/readme/testing/navigation-js-report.png) |
| /static/js/quantity-input-script.js | 0 warnings, 0 errors | [Report](/docs/readme/testing/quantity-input-script-js-report.png) |
| /bag/static/bag/js/basket-buttons.js | 0 warnings, 0 errors | [Report](/docs/readme/testing/basket-buttons-js-report.png) |
| /checkout/static/checkout/js/stripe_elements.js | 0 warnings, 0 errors | [Report](/docs/readme/testing/stripe-js-report.png) |
| /products/static/products/js/shop-and-filter-search.js | 0 warnings, 0 errors | [Report](/docs/readme/testing/shop-and-filter-search-js.png) |
| /profiles/static/profiles/js/countryfield.js | 0 warnings, 0 errors | [Report](/docs/readme/testing/countryfield-report.png) |

### Python

Due to time constraints, I was unable to run unit tests for all apps. With this in mind, I decided to first target what I considered the two most important apps: Checkout and Products. With my remaining time, I also managed to run unit tests for Artists and the Blog.

| App | Tests | Report | Coverage |
| --- | ----- | ------ | -------- | 
| Artists | 10 tests: 10 successful, 0 failed | [Report](/docs/readme/testing/artist-unit-tests.png) | [Coverage](/docs/readme/testing/artist-coverage-report.png) |
| Blog | 10 tests: 10 successful, 0 failed | [Report](/docs/readme/testing/blog-unit-tests.png) | [Coverage](/docs/readme/testing/blog-coverage-report.png) |
| Checkout | 4 tests: 4 successful, 0 failed | [Report](/docs/readme/testing/checkout-unit-tests.png) | [Coverage](/docs/readme/testing/checkout-coverage-report.png) |
| Products | 17 tests: 17 successful, 0 failed | [Report](/docs/readme/testing/products-unit-tests.png) | [Coverage](/docs/readme/testing/products-coverage-report.png) |

## Browser testing

This project has been tested in the following browsers
- Google Chrome
- Firefox
- Microsoft Edge
- Brave