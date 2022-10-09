# Forrest Records

![Forrest Records](/media/homepage-background.jpg)

All of the greatest punk/hardcore music - all under one roof. Whether you are looking for collectable, vintage vinyls, or the newest releases from your favourite artists, you are in the right place.

## Table of Contents

- [Forrest Records](#forrest-records)
  * [Table of Contents](#table-of-contents)
  * [UX/UI](#ux-ui)
    + [Target audience](#target-audience)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Visuals](#visuals)
        * [Fonts](#fonts)
      - [Wireframes (add page urls to table)](#wireframes--add-page-urls-to-table-)
      - [Database](#database)
        * [Physical model](#physical-model)
        * [Models](#models)
  * [Features](#features)
    + [Current Features](#current-features)
      - [Feature 1: Navigation Bar](#feature-1--navigation-bar)
      - [Feature 2: Homepage](#feature-2--homepage)
      - [Feature 3: Blog Pages](#feature-3--blog-pages)
        * [Individual Blog Page](#individual-blog-page)
      - [Feature 4: Shop pages](#feature-4--shop-pages)
        * [Individual Product Pages](#individual-product-pages)
      - [Feature 5: Artists Page](#feature-5--artists-page)
      - [Contact page](#contact-page)
      - [Login, Register and Logout](#login--register-and-logout)
      - [Profile pages](#profile-pages)
      - [Staff only pages](#staff-only-pages)
      - [Basket](#basket)
      - [Checkout](#checkout)
    + [Features to be Implemented](#features-to-be-implemented)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Libraries + Frameworks](#libraries---frameworks)
    + [Design](#design-1)
    + [Other tools](#other-tools)
  * [Testing](#testing)
  * [Bugs](#bugs)
  * [Deployment](#deployment)
    + [Local Development](#local-development)
    + [AWS Setup](#aws-setup)
    + [Stripe Setup](#stripe-setup)
    + [Heroku Deployment](#heroku-deployment)
  * [Credits](#credits)
    + [Code](#code)
    + [Media](#media)
    + [General Thanks](#general-thanks)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## UX/UI

### Target audience

The target audience for this site is primarily fans of punk/hardcore music, particularly:
1. People who collect vinyl albums; including rare editions.
2. Bargain hunters looking for a good deal on albums/merchandise.
3. People looking to keep up to date with the latest releases in the music scene.
4. Younger people/students looking for discounts on their favourite music.
5. People looking for both current, as well as vintage/collectable, band merchandise.

### User Stories

| No. | Bug | Link | Completed |
| ---- | -------------- | ---- | :----: |
|  | **Site users** |  |  |
| #1 | As a user, I want the site's navigation to be simple and intuitive. | [Link to issue #1](https://github.com/Samoftheforrest/forrest-records/issues/12) | :white_check_mark: |
| #2 | As a user, I want to be able to be able to checkout without an account. | [Link to issue #2](https://github.com/Samoftheforrest/forrest-records/issues/13) | :white_check_mark: |
| #3 | As a user, I want to be able to be able to checkout without an account. | [Link to issue #3](https://github.com/Samoftheforrest/forrest-records/issues/14) | :white_check_mark: |
| #4 | As a user, I want to be able to sort/filter products based on the following criteria: Price, Alphabetically, Product type, Artist. | [Link to issue #4](https://github.com/Samoftheforrest/forrest-records/issues/15) | :white_check_mark: |
| #5 | As a user, I would like to be able to create an account to save/update my delivery information. | [Link to issue #5](https://github.com/Samoftheforrest/forrest-records/issues/16) | :white_check_mark: |
| #6 | As a user, I would like to be directed to an error page that is inkeeping with the sites design/aesthetic if there is any error. | [Link to issue #6](https://github.com/Samoftheforrest/forrest-records/issues/17) | :white_check_mark: |
| #7 | As a user, I would like to be able to add products to a 'wishlist' to view them later. | [Link to issue #7](https://github.com/Samoftheforrest/forrest-records/issues/18) | :white_check_mark: |
| #8 | As a user, I want clear feedback on what is in my shopping bag, including when it is empty. | [Link to issue #8](https://github.com/Samoftheforrest/forrest-records/issues/19) | :white_check_mark: |
| #9 | As a user, I want to be able to easily update my shopping bag, including removing items from it. | [Link to issue #9](https://github.com/Samoftheforrest/forrest-records/issues/20) | :white_check_mark: |
| #10 | As a user, I want clear confirmation when an order has been completed.| [Link to issue #10](https://github.com/Samoftheforrest/forrest-records/issues/21) | :white_check_mark: |
| #11 | As a user, I want feedback that my order is being processed. | [Link to issue #11](https://github.com/Samoftheforrest/forrest-records/issues/22) | :white_check_mark: |
| #12 | As a user, I would like a page that shows a list of all the artists, so I am able to find relevant products easily. | [Link to issue #12](https://github.com/Samoftheforrest/forrest-records/issues/23) | :white_check_mark: |
| #13 | As a user, I want to be able to reset my passowrd if I forget it. | [Link to issue #13](https://github.com/Samoftheforrest/forrest-records/issues/24) | :white_check_mark: |
| #14 | As a user, I want the ability to easily log in and out of my account. | [Link to issue #14](https://github.com/Samoftheforrest/forrest-records/issues/25) | :white_check_mark: |
| #15 | As a user, I want to be able to contact the store owners to provide feedback or query an order. | [Link to issue #15](https://github.com/Samoftheforrest/forrest-records/issues/33) | :white_check_mark: |
|  | **Site owners** |  |  |
| #1 | As a user, I want the ability to add products to the store. | [Link to issue #1](https://github.com/Samoftheforrest/forrest-records/issues/26) | :white_check_mark: |
| #2 | As a user, I want the ability to edit products easily. | [Link to issue #2](https://github.com/Samoftheforrest/forrest-records/issues/27) | :white_check_mark: |
| #3 | As a user, I want the ability to delete products from the store. | [Link to issue #3](https://github.com/Samoftheforrest/forrest-records/issues/28) | :white_check_mark: |
| #4 | As a user, I want the ability to add new artists to the store. | [Link to issue #4](https://github.com/Samoftheforrest/forrest-records/issues/29) | :white_check_mark: |
| #5 | As a user, I want the ability to edit information about artists. | [Link to issue #5](https://github.com/Samoftheforrest/forrest-records/issues/30) | :white_check_mark: |
| #6 | As a user, I want the ability to delete artists from the store. | [Link to issue #6](https://github.com/Samoftheforrest/forrest-records/issues/31) | :white_check_mark: |
| #7 | As a user, I want to see orders that have been placed. | [Link to issue #7](https://github.com/Samoftheforrest/forrest-records/issues/32) | :white_check_mark: |
| #8 | As a user, I'd like to be able to see all messages sent in one place. | [Link to issue #8](https://github.com/Samoftheforrest/forrest-records/issues/34) | :white_check_mark: |

### Design

#### Visuals
For this project, I used the pre-made [Red at Night](https://colorhub.vercel.app/select-palette/enviro) colour palette from [Daniel Cranney](https://twitter.com/danielcranney)'s ['ColorHub'](https://colorhub.vercel.app/). I decided that to use this colour palette as it is largely monochromatic (using black, grey, and white), but also has a striking red; I believe this colour will attract users' attention toward any calls to action on the site.

![Devhub Colour Pallete](/docs/readme//design/color-palette.png)

The colours used were:
- `#EF4444`: This colour was used as the brand colour, used mostly on call to action buttons/links, or anything else that I wanted to focus the user's attention to.
- `#18181B`: This colour was used as the primary colour for text (on a white background), and to give a contrasting background to some sections. Also, an opaque version of this colour is used on image overlays.
- `#D4D4D8`: This colour was used sparingly either as text decoration or borders - I chose this colour as I felt it is fairly subtle/understated.
- `#F8FAFC`: This colour is used as the primary background colour, and text colour on dark backgrounds.

##### Fonts

I used two [Google fonts]() for this project: [DM Sans](https://fonts.google.com/specimen/DM+Sans) for the headings, and [Montserrat](https://fonts.google.com/specimen/Montserrat) for main body text.

#### Wireframes (add page urls to table)

| Page | Desktop | Tablet | Mobile |
| ---- | -------------- | ---- | ------ |
| Landing | [Desktop wireframe](/docs/wireframes/landing-page.png) | [Tablet wireframe](/docs/wireframes/landing-page-tablet.png) | [Mobile wireframe](/docs/wireframes/landing-page-mobile.png) |
| Artists | [Desktop wireframe](/docs/wireframes/artists.png) | [Tablet wireframe](/docs/wireframes/artists-tablet.png) | [Mobile wireframe](/docs/wireframes/artists-mobile.png) |
| Product list | [Desktop wireframe](/docs/wireframes/product-listing.png) | [Tablet wireframe](/docs/wireframes/product-listing-tablet.png) | [Mobile wireframe](/docs/wireframes/product-listing-mobile.png) |
| Product single | [Desktop wireframe](/docs/wireframes/product-single.png) | [Tablet wireframe](/docs/wireframes/product-single-tablet.png) | [Mobile wireframe](/docs/wireframes/product-single-mobile.png) |
| Add/Edit product | [Desktop wireframe](/docs/wireframes/add-edit-product.png) | [Tablet wireframe](/docs/wireframes/add-product-tablet.png) | [Mobile wireframe](/docs/wireframes/add-edit-product-mobile.png) |
| Basket | [Desktop wireframe](/docs/wireframes/basket.png) | [Tablet wireframe](/docs/wireframes/basket-tablet.png) | [Mobile wireframe](/docs/wireframes/basket-mobile.png) |
| Checkout | [Desktop wireframe](/docs/wireframes/checkout.png) | [Tablet wireframe](/docs/wireframes/checkout-tablet.png) | [Mobile wireframe](/docs/wireframes/checkout-mobile.png) |
| Checkout success | [Desktop wireframe](/docs/wireframes/checkout-success.png) | [Tablet wireframe](/docs/wireframes/checkout-success-tablet.png) | [Mobile wireframe](/docs/wireframes/checkout-success-mobile.png) |
| Profile | [Desktop wireframe](/docs/wireframes/profile.png) | [Tablet wireframe](/docs/wireframes/profile-tablet.png) | [Mobile wireframe](/docs/wireframes/profile-mobile.png) |
| Blog list | [Desktop wireframe](/docs/wireframes/blog-listing.png) | [Tablet wireframe](/docs/wireframes/blog-tablet.png) | [Mobile wireframe](/docs/wireframes/blog-mobile.png) |
| Blog single | [Desktop wireframe](/docs/wireframes/blog-single.png) | [Tablet wireframe](/docs/wireframes/blog-single-tablet.png) | [Mobile wireframe](/docs/wireframes/blog-single-mobile.png) |
| Edit blog | [Desktop wireframe](/docs/wireframes/blog-edit.png) | [Tablet wireframe](/docs/wireframes/edit-blog-tablet.png) | [Mobile wireframe](/docs/wireframes/edit-blog-mobile.png) |
| Login/Register | [Desktop wireframe](/docs/wireframes/register.png) | [Tablet wireframe](/docs/wireframes/login-register-tablet.png) | [Mobile wireframe](/docs/wireframes/login-register-mobile.png) |
| Contact | [Desktop wireframe](/docs/wireframes/contact.png) | [Tablet wireframe](/docs/wireframes/contact-tablet.png) | [Mobile wireframe](/docs/wireframes/contact-mobile.png) |
| Error pages (400, 500, etc) | [Desktop wireframe](/docs/wireframes/error-pages.png) | [Tablet wireframe](/docs/wireframes/error-pages-tablet.png) | [Mobile wireframe](/docs/wireframes/error-pages-mobile.png) |

#### Database

##### Physical model

![Database schema](/docs/readme/design/database.png)

##### Models

**NOTE**: To meet the demands of the site, more models were required since the creation of the physical model above - all models can be found below:

The individual database models can be found in [this](/docs/readme/database.md) separate markdown file.

## Features

### Current Features

#### Feature 1: Navigation Bar

![Navigation bar](/docs/readme/features/feature-nav.png)

Allows the user to navigate between the following sections:
- Home
- Shop
- Blog
- Contact
- Login/Register
- Basket

The "Shop", "Login/Register" and "Basket" also have submenus that display on hover:

**Shop submenu**
![Shop menu](/docs/readme/features/feature-nav-menu.png)

**Login submenu**
![Login menu](/docs/readme/features/feature-nav-login.png)

**Basket dropdown**
![Basket dropdown](/docs/readme/features/feature-nav-basket.png)

The basket dropdown also contains:

1. A scroll icon which displays if the dropdown is scrollable.

https://user-images.githubusercontent.com/94783808/190649667-eb4d6353-266e-42ad-bd5e-24b55e01170c.mp4

2. A small quantity icon to show how many items are current in the user's basket.

![Basket quantity](/docs/readme/features/feature-nav-basket-quantity.png)

#### Feature 2: Homepage

![Homepage](/docs/readme/features/homepage.png)

This page displays when the user visits the home directory of the site - meaning that it will be the page that most users see for the first time when visiting. It consists of:
- The navigation bar
- A title
- A lead paragraph
- Two buttons - that lead to the shop and blog

**Social icons**
The social icons, upon the page loading, have a staggered animation in which each item slides up into view - one after another. I achieved this using a SCSS for loop.

```
@for $i from 1 to 5 {
    .homepage-icons a:nth-child(#{$i}) {
        animation-delay: calc(#{$i * 0.25}s);
    }
}
```

It looks like this in the final version of the site:

https://user-images.githubusercontent.com/94783808/190912753-f9f2bdb7-b905-438e-9539-7a35bc4a3a5e.mp4

#### Feature 3: Blog Pages

![Blog page](/docs/readme/features/blog-list.png)

When the user visits the blog area of the site, they are initially directed to the blog listing page - which shows the blogs sorted in order from newest to oldest. Also, from the admin, anyone with the correct permissions can set a 'featured' blog, which will be the first blog to show on this page:

**Add blog**
When a staff member navigates to the main blog page, they are able to create a new blog by simply clicking the pencil button - which will take them to the following form:

![Add blog form](/docs/readme/features/add-blog-ft.png)

NOTE: this form also includes the ckeditor rich text field - this gives staff more flexibility to format their content.

**Featured Blog**
![Featured blog](/docs/readme/features/blog-featured.png)

Once a user clicks the blog of their choice, they are redirected to the page for that individual blog post. This page includes a breadcrumb which allows you to return to the main blog listing page.

Staff members are also able to set the featured blog via the frontend, by simply navigating to the blog they wish to feature, and clicking the star icon in the header section.

![Feature blog](/docs/readme/features/feature-blog-ft.png)

##### Individual Blog Page
![Individual blog](/docs/readme/features/blog-single.png)

I also installed an additional pip package - [ckeditor](https://django-ckeditor.readthedocs.io/en/latest/) - to allow any admin who is writing a blog to do so using a rich text field. I decided to take this approach as I found this way ensured that any formatting present in the blog post was present on the page; it also allowed for authors to include relevant links, images, tables, etc.

**Edit Blog**

When on an individual blog page, staff members are also able to edit blogs by clicking the pencil in the header section.

![Edit blog](/docs/readme/features/edit-blog-ft.png)

#### Feature 4: Shop pages

![Shop page](/docs/readme/features/shop-page.png)

When the user visits the shop area of the site, they are directed to a list of all products - although it is also possible to navigate to album/merchandise-only pages through the navigation.

**Sale tag**

![Sale tag](/docs/readme/features/shop-sale-item.png)

If an item is on sale (meaning `on_sale=True` in the backend), a red flag displays on the item to reflect this. Also, the new price is shown next to the original price to show the user the deal they are getting.

**Digital download tag**

![Digital download tag](/docs/readme/features/shop-digital-download.png)

If an album is also available for digital download, this is reflected in the products list by the 'digital download available' tag at the bottom of the item - next to the product type.

**Filter**

![Shop filter](/docs/readme/features/shop-filter.png)

On the main shop page, there are options to sort the products based upon certain criteria (e.g. price, name, etc).

Example

https://user-images.githubusercontent.com/94783808/193417101-ccf8aca8-5f3e-4402-8ae3-7c708a45f6f3.mp4

**Search**

The user is also given the ability to search for items within the shop by clicking the floating search icon in the bottom-right corner of the page. However, on mobile - to free up screen real estate - the search bar is included within the main mobile menu.

Examples

https://user-images.githubusercontent.com/94783808/193417155-2ab2ad6f-1aa0-4579-9395-8d3299d55a61.mp4

https://user-images.githubusercontent.com/94783808/193417158-3d08cf78-236e-4223-82dc-1612bfdaa797.mp4

##### Individual Product Pages

Once a user has found the product they wish to view on the main shop page, they can click through into the individual pages, which have the following features:

**Product information**

Merch version

![Merch information](/docs/readme/features/shop-merch-info.png)

Album version

![Album information](/docs/readme/features/shop-album-info.png)

This section shows the following information about the product:
- Name
- Image
- Artist
- Description
- Sizes (if product type is merch)
- Digital download (if product type is album)
- Quantity selector

This section also includes the 'Add to wishlist button'

Example of quantity buttons - including minus button being disabled when quantity reaches 1

https://user-images.githubusercontent.com/94783808/193417216-dadbc24b-03eb-4289-951e-ef7a96cd49bc.mp4

**Track listing**

![Track listing example](/docs/readme/features/shop-track-listing.png)

On the album pages, the user is also shown the track listing of the album they are currently viewing - ordered by track number. However, if there is no tracklist for this album, the following displays:

![Empty track list example](/docs/readme//features/shop-track-listing-empty.png)

**Related items**

If there are any other products available from the same artist the user is viewing, they will be shown as related products at the bottom of the page. However, this list is limited to four items.

Example

https://user-images.githubusercontent.com/94783808/193417227-3881e82b-cbb9-4a43-9eb8-1691eaaece4a.mp4

**Edit and delete products**

From these pages, staff members also have the option to edit and delete the product they are currently viewing:

Edit album

![Edit album](/docs/readme/features/edit-album-ft.png)

Edit merch

![Edit merch](/docs/readme/features/edit-merch-ft.png)

Similarly to the blog pages, the user is also warned before deleting any product

![Delete product](/docs/readme/features/delete-album-ft.png)

#### Feature 5: Artists Page

![Artists Page](/docs/readme/features/artists-page.png)

From the "Shop" menu in the navigation, the user can also navigate to the Artists page. This page shows a list of all artists on the site, arranged alphabetically. Each artist name is a link that leads the user to a filtered version of the shop page that shows products by the artists they have selected only.

**Add/Edit/Delete Artists**
From this page, the user also has the option to add, edit and or delete artists.

Add artist form:
![Add artist form](/docs/readme/features/add-artist-feature.png)

Edit artist form - same as the add artist form, but pre-populated:
![Edit artist form](/docs/readme/features//edit-artist.png)

Delete artist - before the artist is deleted, the user is directed to a warning page to ensure they really want to delete the artist in question
![Delete artist](/docs/readme/features/warning-artist-ft.png)

#### Contact page

I have implemented a simple contact page for customers to contact the store owners. Once this form is filled out, the messages are sent to the inbox (see below).

![Contact form](/docs/readme/features/contact-ft.png)

#### Login, Register and Logout

These pages are modified versions of the templates provided by [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html), which seemlessly handle all authorisation.

![Login](/docs/readme/features/login-ft.png)

![Register](/docs/readme/features/register-ft.png)

![Logout](/docs/readme/features/logout-ft.png)

#### Profile pages

Once a user has logged in, they are able to see their profile page - this page shows them:
- Their name
- Their delivery information (which is pre-populated if they have saved their information in the past)
- Their order history
- Their wishlist

![Profile page](/docs/readme/features/profile-ft.png)

Staff members also have access to a page that shows all profile pages, to allow them to know how many users the site has.

![All profiles page](/docs/readme/features/all-users-ft.png)

#### Staff only pages

When a staff member is logged in, they also have access to the following pages:
- Inbox
- All users
- All orders

**Inbox**

Here, staff members can see all messages submitted by the contact form.

![Inbox](/docs/readme/features/inbox-ft.png)

**All orders**

This view shows staff members all orders, ordered from newest to oldest.

![All orders](/docs/readme/features/all-orders-ft.png)

**All users**

Similarly to all orders, this page shows all the site's users - allowing staff to see how popular the site is

![All users](/docs/readme/features/all-users-ft.png)

#### Basket

Once a user has added an item to their basket, they will be able to navigate to it via the dropdown menu (or by clicking the basket on mobile). Here, they are able to see all of the items currently in their basket, the cost of these items, the delivery cost, how much more they need to spend to qualify for free delivery (where applicable), and their grand total.

![Bag](/docs/readme/features/basket-ft.png)

#### Checkout

From the basket, users will be able to continue through into the checkout page. Once they have filled out the checkout form, if they have been successful, they will be redirected to a success page, and an email confirmation will be sent to them.

![Checkout](/docs/readme/features/checkout-ft.png)

![Checkout Success](/docs/readme/features/checkout-success-ft.png)

![Checkout Success Email](/docs/readme/features/checkout-success-email-ft.png)

### Features to be Implemented
1. Tours: Add a section to the site which allows user's to search/buy tickets for an artist of their choice's tour.
2. Membership: Add a means for users to sign up for a paid membership, which gives them access to perks such as pre-release sales and free shipping.
3. Featured item on homepage: Add a section to the homepage in which admins can set a featured artist/product/blog.
4. Double albums: Add a double album product type that is similar to an album, but has room for two tracklists.
5. Limited edition tag: Similar to the 'sale' and 'featured' tag - add in another, different colour, tag to show that an album is limited edition/collectable.
6. Individual song pages: allow users to purchase, and see information about, individual songs.
7. Product comments: allow users to add comments on product pages, to leave their feedback.
8. Low stock tag: Add a tag - similar to the 'sale' and 'featured' tags - that let the user know that an item has low stock; this may encourage more sales if the user doesn't wish to miss the chance to purchase the item.

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [SASS/SCSS](https://sass-lang.com/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
- [SQL](https://www.w3schools.com/sql/)

### Libraries + Frameworks
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)

### Design
- [Figma](https://www.figma.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

### Other tools
- [TinyPNG](https://tinypng.com/)

## Testing

Tests can be found [here](/docs/readme/testing.md) in a separate file.

## Bugs

Bugs for this project can be found within the project's 'Issues' tab - for ease, I have added links to each bug's issue log below.

| No. | Bug | Link | Completed |
| ---- | -------------- | ---- | :----: |
| #1 | Basket dropdown scroll icon added on every hover, but not removed | [Link to issue #1](https://github.com/Samoftheforrest/forrest-records/issues/1) | :white_check_mark: |
| #2 | Blog listing page errors when no featured blog is selected  | [Link to issue #2](https://github.com/Samoftheforrest/forrest-records/issues/2) | :white_check_mark: |
| #3 | Album track listing not sorting by track number | [Link to issue #3](https://github.com/Samoftheforrest/forrest-records/issues/3) | :white_check_mark: |
| #4 |  Album info table not ordering items properly when there are 10 or more items  | [Link to issue #4](https://github.com/Samoftheforrest/forrest-records/issues/4) | :white_check_mark: |
| #5 | 'Sale' tag displays above dropdown menus  | [Link to issue #5](https://github.com/Samoftheforrest/forrest-records/issues/5) | :white_check_mark: |
| #6 | Quantity buttons' disabled state  | [Link to issue #6](https://github.com/Samoftheforrest/forrest-records/issues/6) | :white_check_mark: |
| | <strong>Issues 7 and 8 removed as they are no longer relevant</strong> | | |
| #9 | Sales prices displaying incorrectly when more than one size added to basket | [Link to issue #9](https://github.com/Samoftheforrest/forrest-records/issues/9) | :white_check_mark: |
| #10 | Basket remove button removing all sizes of same item | [Link to issue #10](https://github.com/Samoftheforrest/forrest-records/issues/10) | :white_check_mark: |
| #11 | Inbox search returning empty inbox page if no queries are matched | [Link to issue #11](https://github.com/Samoftheforrest/forrest-records/issues/11) | :white_check_mark: |
| #12 | Pages only showing for superusers. | [Link to issue #12](https://github.com/Samoftheforrest/forrest-records/issues/35) | :white_check_mark: |
| #13 | Non-superusers cannot add items to wishlist | [Link to issue #13](https://github.com/Samoftheforrest/forrest-records/issues/36) | :white_check_mark: |

## Deployment

### Local Development
1. Log in to your GitHub account and navigate to this repo
2. Copy the HTTPS code (highlighted in red below)
![GitHub Code Dropdown](/docs/readme/deployment/local-step-1.png)
3. Open your terminal and navigate to the directory you would like to clone this project into
4. Run the following command in your terminal `git clone` followed by the HTTPS link from step two
5. Once the project has cloned, open it in your code editor and add an env.py file to the main directory, this file will require the following environment variables:
- CLOUDINARY_CLOUD_NAME: This can be found on your Cloudinary account.
- CLOUDINARY_API_KEY: This can be found on your Cloudinary account.
- CLOUDINARY_API_SECRET: This can be found on your Cloudinary account.
- DATABASE_URL: Leave this one blank for now, we'll add this during Heroku setup
- EMAIL_HOST: Your smtp email host - for this project, I used Gmail
- EMAIL_HOST_USER: Your email
- EMAIL_HOST_PASS: A password generated by your email provider, to allow access into your account
- EMAIL_PORT: Your email port
- SECRET_KEY: A randomly generated key, which can be created using online services, or by running this command in your terminal 
- STRIPE_PUBLIC_KEY: Leave blank - we'll add this in during the following 'Stripe Setup' step.
- STRIPE_SECRET_KEY: Leave blank - we'll add this in during the following 'Stripe Setup' step.
- STRIPE_WH_SECRET: Leave blank - we'll add this in during the following 'Stripe Setup' step.
- AWS_ACCESS_KEY_ID: Leave blank - we'll add this in during the following 'AWS Setup' step.
- AWS_SECRET_ACCESS_KEY: Leave blank - we'll add this in during the following 'AWS Setup' step.
- DEVELOPMENT: If add this variable in with a variable of 1, it will activate debug mode in Django.

### Stripe Setup
1. Go to the [Stripe website]() and login (create an account if you haven't already).
2. From the 'Home' tab, copy both the 'Publishable key' and 'Secret key' and add them to your config variables from the previous section.
![Stripe Variables](/docs/readme/deployment/stripe-step-1.png)
3. Navigate to the 'Developers' tab, and then the 'Webhooks' in the side menu.
4. Click '+ Add endpoint', add the url of your site, with /checkout/wh added to the end - i.e. `https://www.yourwebsite.com/checkout/wh`
- **NOTE:** You will also need to take note of your webhook key here - we will need this for the environment variables.
5. (**Optional, but recommended**): Trigger a payment to test your webhook.
- **NOTE**: If you set up a `DEVELOPMENT` variable earlier, you need to get rid of it, or your webhooks will fail.

### AWS Setup

#### AWS Bucket
1. Go to the [AWS website](https://aws.amazon.com/) and login (create a personal account if you haven't already - don't be intimidated about having to enter debit card information, you will not be charged).
2. Navigate to AWS Management Console, under My Account.
3. Search for service S3, and create a new bucket; giving it the same name as your website, and selecting the nearest region to you.
- **NOTE:** Uncheck block all public access and acknowledge that the bucket will be public access.
- Also, be sure to set 'Object Ownership' to 'ACLs enabled' and 'Bucket owner preferred'
4. On the following page, click on your newly created bucket.
5. Navigate to the properties tab, and select 'Static Website Hosting', and use it to host a website.
- The index and error documents can be filled with default values, as they won't be used.
6. Next, navigate to the permissions tab, and update the following sections:
- In the CORS section, paste the following:
```
[
    {
        "AllowedHeaders": [
        "Authorization"
    ],
        "AllowedMethods": [
        "GET"
    ],
        "AllowedOrigins": [
        "*"
    ],
        "ExposeHeaders": []
    }
]
```
- In the bucket policy, select a type of 'S3 bucket policy', allow all principles by filling in the field with a star ('*'), select the action will be 'GetObject', and then paste in your arn key from the bucket policy section on the other tab, and paste it into the ARN field at the bottom of the form (keep a note of this ARN value for later). Once this is done, click 'Add Statement', then 'Generate policy', then copy this policy into the bucket policy editor.
- **NOTE:** Add a '/*' onto the end of the "Resource" key here, to allow it access to everything.
- Then, click save.
- In the ACL list tab, click edit and enable List for Everyone (public access) and
accept the warning box. If the edit button is disabled you need to change the Object Ownership
section above to ACLs enabled.

#### IAM
1. Search for 'IAM' via the services search - or locate it in the services menu.
2. Select 'User Group' from the sidebar, and create a group (it's a good idea to name it 'manage-' followed by your project name).
- You will need to click through some extra steps to see the 'Create Group' button.
3. Next, select 'Policies' from the sidebar, followed by 'Create policy'.
4. From here, click 'Import Managed Policy', search for 'S3', and import 'AmazonS3FullAccess'.
5. Copy your ARN key into the "Resource" key twice using a list, the first version should be your ARN key, and the second should be your ARN key followed by '/*', i.e.
```
"Resource": [
    'your-arn-key',
    'your-arn-key/*'
]
```
6. Click through the next pages until you find the 'Review Policy' page. From here you can give it a name and description - related to your project - and click 'Create Policy'
7. Next, we need to attach the policy to the group we made earlier. To attach the policy, on the sidebar click User Groups. Select your group, go to the permissions tab,
open the Add permissions dropdown, and click Attach policies. Select the policy and click Add
permissions at the bottom.
8. Finally, navigate to 'Users' and create a new user - named after your project name. Give them programmatic access (in the checkboxes), and continue to the next page.
9. Select your group, which has the policy attached, and click through until you can 'Create User'
10. **IMPORTANT**: Download the CSV file, which contains essential information, and cannot be downloaded again.

### Connecting Django to S3
1. Install the following packages: `pip3 install boto3` and `pip3 install django-storages` (and run freeze > requirements.txt)
2. Add storages to installed apps.
3. Create an if statement to check if there is an environment variable called 'USE_AWS' in os.environ
4. Define AWS_STORAGE_BUCKET_NAME (your bucket's name), AWS_S3_REGION_NAME (that you selected earlier on), AWS_ACCESS_KEY (which we can get from the environment - the value of which we can find from the CSV file downloaded earlier), and AWS_SECRET_ACCESS_KEY (again, from the environment, the same as AWS_ACCESS_KEY).
4. Set up a variable called AWS_S3_CUSTOM_DOMAIN, which should be set up using an f-string as follows: `f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`
5. Create a new file called 'custom_storages.py' in the root directory, and import settings and storages (`from storages.backends.s3boto3 import S3Boto3Storage`)
6. Create a custom class called StaticStorage, and another called MediaStorage, the final result will look like this:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
7. Finally, go back to settings.py and add the following to set the locations of our static files:
```
# Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}'
```

### Heroku Deployment
1. Navigate to the [Heroku Website](heroku.com) and login (sign up if you haven't already)
2. Create a new app, name it, and select the region nearest to you.
3. From here, in the 'Overview' section, navigate to 'Add-ons' and select Postgres, under the 'Hobby Dev' plan.
4. Click into your newly created Heroku Postgres database, and take a note of your database URL, and add it to your config variables as `DATABASE_URL`.
- **NOTE**: At this stage, you should also makemigrations and migrate to your new Postgres database, to ensure you have all your models set up.
5. Next, under the 'Settings' tab, scroll down and select 'Reveal Config Vars' - here we are going to set all of the required config variables set up earlier:
- **NOTE:** The 'USE_AWS' variable should only be added to the Heroku config variables, so you can add this in now: `USE_AWS` with a value of `True`
6. Navigate to the 'Deploy' tab, and under 'Deployment Method' select 'GitHub'.
7. Connect your account, select your project, and the branch you wish to deploy from.
8. Enable automatic deploys - as this will deploy your site every time you commit changes to GitHub.
9. Finally, click 'Deploy Branch'.
10. Sit back, relax, and let Heroku do the work for you!

**FINAL NOTE**

IF you encounter any problems while deploying - it is a good idea to use the Heroku build logs to find the problem. Also, temporarily enabling the DEVELOPMENT environment variable, thus turning on Django's DEBUG mode, can be very useful; **but make sure you delete the DEVELOPMENT variable when you are finished.**
 
## Credits

### Code
- [Codemy](https://www.youtube.com/watch?v=ygzGr51dbsY&ab_channel=Codemy.com) for demonstrating how to upload files through Django forms.
- [Elf Sternberg](https://stackoverflow.com/a/4151742) for the code to regroup the artists queryset used on the /artists page.
- [Code Artisan Lab](https://www.youtube.com/watch?v=fqIBA2Vpws0&ab_channel=CodeArtisanLab) for the code to set up the related items list on product pages
- [Laffuste & Phoenix](https://stackoverflow.com/a/16909142) for the syntax to iterate through RelatedManager objects.
- [Wouter J](https://stackoverflow.com/a/15146850) showed me how to use for loops in SCSS, which allowed me to add the homepage social icons animation in simply.
- [Frost.baka](https://stackoverflow.com/a/4144088), for the code to stop admin adding another model in the admin area for the homepage.
- [Geeks For Geeks](https://www.geeksforgeeks.org/richtextfield-django-models/), for showing me how to add a rich text field to the Django admin area.
- [MaximeK](https://stackoverflow.com/a/44658616), for showing me how to extend Django models - which I used to extend the Product model into the Album/Merch models.

### Media
- Thanks to [Unsplash](https://www.unsplash.com) for all the product images.
- Thanks to [Freepik](https://www.freepik.com/) for the vinyl [favicon](https://www.flaticon.com/free-icons/vinyl")
- Thanks to [Natalie Parham](https://unsplash.com/@natalieparham) for the [homepage image](https://unsplash.com/photos/fPKqpUbTL4Y?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)

### General Thanks
- I would like the thank the tech Twitter community for helping me brainstorm artist names for testing.
- I would like to thank my parter, Laura Gilbert, for helping me test the site from a user's perspective.
- I would like to thank my mentor [Simen](https://github.com/Eventyret) for all of his feedback and support with this project.
