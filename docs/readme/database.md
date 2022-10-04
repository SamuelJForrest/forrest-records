###### Product

```
class Product(models.Model):
    """
    Model for all products.
    """
    
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    sku = models.CharField(
        max_length=254,
        null=True,
        blank=False)

    description = models.TextField()

    product_type = models.ForeignKey(
        'ProductType',
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    artist = models.ForeignKey(
        Artist,
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False)

    rating = models.IntegerField(
        null=True,
        blank=True,
        default=0)

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True)

    image = models.ImageField(
        null=True,
        blank=True)

    on_sale = models.BooleanField(
        default=False,
        null=True,
        blank=True)

    product_group = models.ForeignKey(
        'ProductGroup',
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
```

###### ProductType

```
class ProductType(models.Model):
    """
    Model for product types.
    """

    name = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    friendly_name = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        """
        Returns friendly version of the product type name for users.
        """
        return self.friendly_name
```

###### ProductGroup

```
class ProductGroup(models.Model):
    """
    Model for product groups.
    """
    
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    friendly_name = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        """
        Returns friendly version of the product type name for users.
        """
        return self.friendly_name
```

###### Album - extended from Product model

```
class Album(Product):
    """
    Model for albums - extended from product model.
    """

    record_label = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    release_year = models.CharField(
        max_length=4,
        null=True,
        blank=True)

    genre = models.ForeignKey(
        'Genre',
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    digital_download = models.BooleanField(
        default=True,
        null=True,
        blank=True)

    digital_download_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)

    def __str__(self):
        return self.name
```

###### Genre

```
class Genre(models.Model):
    """
    Model for genres.
    """

    name = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    friendly_name = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        """
        Returns friendly version of the product type name for users.
        """
        return self.friendly_name
```

###### Song

```
class Song(models.Model):
    """
    Model for songs.
    """

    title = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    album = models.ForeignKey(
        'Album',
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    artist = models.ForeignKey(
        Artist,
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    duration = models.CharField(
        max_length=6,
        null=True,
        blank=True)

    track_number = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],
        null=False,
        blank=False)

    def __str__(self):
        return self.title
```

###### Merch - extends the Product model

```
class Merch(Product):
    """
    Model for merch - extended from product model.
    """
    class Meta:
        """
        Admin settings for merch model.
        """
        verbose_name_plural = 'Merch'

    has_sizes = models.BooleanField(
        default=True,
        null=False,
        blank=False)

    def __str__(self):
        return self.name
```

###### Blog

```
class Blog(models.Model):
    """
    Model for individual blogs.
    """

    title = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    author = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    content = RichTextField()

    image_url = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    def __str__(self):
        return self.title
```

###### Blog page
```
class BlogPage(models.Model):
    """
    Model for blog page.
    """
    class Meta:
        """
        Model admin settings.
        """
        verbose_name_plural = 'Blog Page'

    title = models.CharField(
        max_length=16,
        null=False,
        blank=False)

    subtitle = models.CharField(
        max_length=64,
        null=False,
        blank=False)

    featured_blog = models.ForeignKey(
        Blog,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return 'Blog page'
```

###### Artists

```
class Artist(models.Model):
    """
    A class for artist information: name and friendly name. 
    """

    name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        help_text="This name should be all lowercase, and contain no spaces.")

    friendly_name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        help_text="This should be the artist name you want users to see.")

    def __str__(self):
        return str(self.friendly_name)
```

###### Users

###### User Profiles

```
class UserProfile(models.Model):
    """
    A user profile model to store delivery information and order history
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)

    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True)

    default_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True)

    default_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True)

    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True)

    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True)

    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True)

    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True)

    def __str__(self):
        return self.user.username
```

###### Order

```
class Order(models.Model):
    """
    Model to create order details
    """

    user_profile = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        related_name='orders',
        on_delete=models.SET_NULL
    )

    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False
    )

    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )

    phone_number = models.CharField(
        max_length=20,
        null=False, 
        blank=False
    )

    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False
    )

    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )

    address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )

    address2 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )

    county = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )

    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
    )

    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    def _generate_order_number(self):
        """
        Generate a random, unqiue order using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
```

###### Order Line Item

```
class OrderLineItem(models.Model):
    """
    Generate an individual order, to be added to the overall order
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )

    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    
    product_size = models.CharField(
        max_length=2,
        null=True,
        blank=True
    ) # XS, S, M, L, XL

    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )

    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
```

###### Home page

```
class Homepage(models.Model):
    """
    Model for the homepage.
    """
    class Meta:
        """
        Admin settings for the homepage.
        """
        verbose_name_plural = 'Home Page'

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False)

    lead_paragraph = models.TextField()

    shop_button = models.CharField(
        max_length=15,
        null=False,
        blank=False)

    blog_button = models.CharField(
        max_length=15,
        null=False,
        blank=False)

    facebook_link = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    instagram_link = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    soundcloud_link = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    bandcamp_link = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    def __str__(self):
        return 'Homepage'
```

###### Contact page

```
class ContactPage(models.Model):
    """
    Model for the contact page.
    """
    class Meta:
        """
        Admin settings for contact page.
        """
        verbose_name_plural = 'Contact Page'

    title = models.CharField(max_length=16, null=False, blank=False)
    subtitle = models.CharField(max_length=16, null=False, blank=False)

    def __str__(self):
        return 'Contact Page'
```