const mix = require('laravel-mix');

mix.sass('frontend/sass/base.scss', 'static/css/base.css')
.js('frontend/js/bootstrap.js', 'static/js/bootstrap.js')
.js('frontend/js/navigation.js', 'static/js/navigation.js')
.js('frontend/js/quantity-input-script.js', 'static/js/quantity-input-script.js');