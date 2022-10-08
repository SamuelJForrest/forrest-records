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
| /profile/order/history/<order_number> | | [Report](/docs/readme/testing/past-order-html-report.png) |

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

The following files were tested using [PEP8Online](http://pep8online.com/)



## Testing User Stories

| # | User story | Implementation | Test | Result |
| ---- | ---- | -------------- | ---- | ------ |
| #1 | As a user, I want the site's navigation to be simple and intuitive. | I created a simple navigation by only using six possible links for the general areas of the site: home, shop, blog, contact, login/logout, basket - for the links that have more complexity (e.g. the different products within the shop) I added submenus to the main nav items. | I will ask a test user (my partner) to navigate to three areas within the site - contact, the basket, and merchandise within the store - to see if she can easily navigate to all of these areas on her first try. | My partner was able to navigate to all three areas of the site, and described the process as 'simple and intuitive'. I have determined this test to be successful. |
| #2 | As a user, I want to be able to be able to checkout without an account. | When creating the logic/templates for checking out, I included a checkout path that allows a user to checkout without logging in. | I will create my own test account, and attempt to complete the entire checkout process without logging in. | Result text |
| #3 | As a user, I want to be able to search for products, to reduce the amount of time it takes to locate a particular product. | On the product pages, I included a search bar that allows the user to search within the shop for a specific item. | I will search for three specific items | Result text |
| #4 | As a user, I want to be able to sort/filter products based on the following criteria: price, alaphabetically, rating, item type, artist | I have added a select dropdown to the product pages to allow the user to filter by the criteria set in this user story. | I will attempt to use this select to filter the products page by each criteria, and observe whether it filters appropriately for each one. | Result text |
| #5 | As a user, I would like to be able to create an account to save/update my delivery information. | I will implement an authorisation system - using allauth - to allow users to login, and to save their data within the User/Userprofile database tables | I will create a test account, and add details for said account - once done, I will logout and attempt to login in again and check that the information has saved and displays properly. | Result text |
| #6 | As a user, I would like to be directed to an error page that is inkeeping with the sites design/aesthetic if there is any error. | I have added a redirect for any unrecognised URL or other error to the appropriate 404, 500, etc pages. | I will add three unused URLs to the end of the site's URL: /news, /gigs, /forum and observe whether I am redirected to the appropriate error page. | Result text |
| #7 | As a user, I would like to be able to add products to a 'wishlist' to view them later. | I have added a button on each product page that adds the product in question to the user's wishlist within the database. | Using a test account, I will choose four products at random and add them to my wishlist - I will then check to see whether the same items display on the profile page for this account. | Result text |
| #8 | As a user, I want clear feedback on what is in my shopping bag, including when it is empty. | Within the basket icon - in the main navigation - I have added a number that displays the amount of items in the user's bag. Also, I have added a toast that displays when an item is added, updated, or removed from the basket. | I will add three random products to my basket to test whether the appropriate toasts and number of items display. | Result text |
| #9 | As a user, I want to be able to easily update my shopping bag, including removing items from it. | I have added functionality that allows the user to change the quantity of each item in their basket, as well as removing it (either by clicking 'remove' or changing the quantity to 0). | I will select two items that have been added to my basket. One of these items I will update the quantity of, the other I will delete. I will observe whether both of these items have updated correctly. | Result text |
| #10 | As a user, I want clear confirmation when an order has been completed. | I have included a template that displays a success message, which the user is redirected to upon successfully completing their order. | Using a test account, I will complete three orders, to see if I am directed to the appropriate template each time. | Result text |
| #11 | As a user, I want feedback that my order is being processed. | I have added functionality that emails the user once a transaction has been completed and is being processed | Upon completing three test transactions from the previous user story, I will check that - for each of these transactions - a confirmation email has been sent. | Result text |
| #12 | As a user, I would like a page that shows a list of all the artists, so I am able to find relevant products easily. | I have added an 'artists' page, which is accessible through the shop submenu (or through the /artists url) - this template lists all of the artists in alphabetical order. | I will ask a test user (my partner) to locate and visit the page of three random artists, and observe if she is able to find them all simply. | My partner was able to locate all three artists (Float, Async and Event Handlers) and described the process of finding them as 'easy' - I have determined this test to be a success. |
| #13 | As a user, I want to be able to reset my passowrd if I forget it. | Implementation text | Test text | Result text |
| #14 | As a user, I want the ability to easily log out of my account. | Implementation text | Test text | Result text |
| #15 | As a store owner, I want the ability to add products to the store. | Implementation text | Test text | Result text |
| #16 | As a store owner, I want the ability to edit products easily. | Implementation text | Test text | Result text |
| #17 | As a store owner, I want the ability to delete products from the store. | Implementation text | Test text | Result text |
| #18 | As a store owner, I want the ability to add new artists to the store. | Implementation text | Test text | Result text |
| #19 | As a store owner, I want the ability to edit information about artists. | Implementation text | Test text | Result text |
| #20 | As a store owner, I want the ability to delete artists from the store. | Implementation text | Test text | Result text |
| #21 | As a store owner, I want to see orders that have been placed. | Implementation text | Test text | Result text |
| #22 | As a store owner, I want to be able to edit orders when a customer informs us of any mistakes made. | Implementation text | Test text | Result text |
| #23 | As a store owner, I want to see a list of users to determine how popular the site is. | Implementation text | Test text | Result text |
| #24 | As a store owner, I would like to be able to manage the accounts of users: changing their permissions, deleting accounts, etc. | Implementation text | Test text | Result text |
| #25 | As a store owner, I want to be able to see which products have sold the most units, to guage the popularity of different products. | Implementation text | Test text | Result text |
| #26 | As a store owner, I want a list of email addresses for each user, so that I can create a mailing list of all customers, if permission is given by users. | Implementation text | Test text | Result text |