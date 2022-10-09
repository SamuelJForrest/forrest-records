# Database models

## Album - extended from Product model
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| record_label | Char | max_length=254  null=True  blank=True | |
| release_year | Char | max_length=4  null=True  blank=True | |
| genre | ForeignKey | null=True  blank=True  on_delete=models.SET_NULL | default=1 |
| digital_download | BooleanField  null=True  blank=True | | |

## Artist
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254  null=False  blank=False  help_text="This name should be all lowercase, and contain no spaces, e.g. \"forrest_records\"." | |
| friendly_name | Char | max_length=254  null=False  blank=False  help_text="This should be the artist name you want users to see." | |

## Blog
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=254  null=False  blank=False | |
| author | ForeignKey | UserProfile  null=True  blank=True  on_delete=models.SET_NULL | |
| content | RichTextField (requires ckeditor installation) | | |
| image | ImageField | upload_to='images/'  null=True  blank=True | |
| image_url | Char | max_length=254  null=True  blank=True | |
| date_published | DateField | auto_now_add=True | |

## BlogPage
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=16  null=False  blank=False | |
| subtitle | Char | max_length=64  null=False  blank=False | |
| featured_blog | ForeignKey | Blog  null=True  blank=True  on_delete=models.SET_NULL | |

## ContactPage
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=16  null=False  blank=False | |
| subtitle | Char | max_length=16  null=False  blank=False | |

## Genre
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254  null=False  blank=False | |
| friendly_name | Char | max_length=254  null=False  blank=False | |

## Homepage
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=50  null=False  blank=False | |
| lead_paragraph | TextField | | |
| shop_button | Char | max_length=15  null=False  blank=False | |
| blog_button | Char | max_length=15  null=False  blank=False | |
| facebook_link | Char | max_length=254  null=True  blank=True | |
| instagram_link | Char | max_length=254  null=True  blank=True | |
| soundcloud_link | Char | max_length=254  null=True  blank=True | |
| bandcamp_link | Char | max_length=254  null=True  blank=True | |
| bg_image | ImageField | upload_to="images/"  null=True  blank=True | |

## Merch - extended from Product model
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| has_sizes | BooleanField | null=True  blank=True | default=True |

## Messages
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=128  null=False  blank=False | |
| email | EmailField | max_length=254  null=False  blank=False | |
| message | TextField | null=False  blank=False | default="" |
| date_sent | DateField | auto_now_add=True | |

## Order
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| user_profile | ForeignKey | UserProfile  null=True  blank=True  related_name='orders'  on_delete=models.SET_NULL | |
| order_number | Charfield | max_length=32  null=False  blank=False | |
| full_name | Char | max_length=50  null=False  blank=False | |
| email | EmailField | max_length=254  null=False  blank=False | |
| phone_number | Char | max_length=20  null=True  blank=True | |
| country | CountryField | blank_label="Country *"  null=True  blank=True | |
| postcode | Char | max_length=20  null=True  blank=True | |
| town_or_city | Char | max_length=40  null=True  blank=True | |
| address1 | Char | max_length=80  null=True  blank=True | |
| address2 | Char | max_length=80  null=True  blank=True | |
| county | Char | max_length=80  null=True  blank=True | |
| date | DateField | auto_add_now=True | |
| delivery_cost | DecimalField | max_digits=6  decimal_places=2  null=False | default=0 |
| order_total | DecimalField | max_digits=10  decimal_places=2  null=False | default=0 |
| grand_total | DecimalField | max_digits=10  decimal_places=2  null=False | default=0 |
| original_bag | TextField | null=False  blank=False | default='' |
| stripe_pid | Char | max_length=254  null=False  blank=False | default='' |

## OrderLineItem
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| order | ForeignKey | Order  null=False  blank=False  on_delete=models.CASCADE  related_name="lineitems" | |
| product | ForeignKey | Product  null=False  blank=False  on_delete=models.CASCADE | |
| product_size | Char | max_length=2  null=True  blank=True | |
| quantity | IntegerField | null=False  blank=False | default=0 |
| lineitem_total | DecimalField | max_digits=2  decimal_places=2  null=False  blank=False  editable=False | |

## Product
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254  null=False  blank=False | |
| sku | Char | max_length=254  null=False  blank=False | |
| description | TextField | | |
| product_type | ForeignKey | 'ProductType'  null=True  blank=True  on_delete=models.SET_NULL | default=1 |
| artist | ForeignKey | 'Artist'  null=True  blank=True  on_delete=models.SET_NULL | default=1 |
| price | DecimalField | max_digits=6  decimal_places=2  null=False  blank=False | |
| image_url | URLField | max_length=1024  null=True  blank=True  help_text='If you have your image hosted anywhere else, add the link here to server as a backup.' | |
| image | ImageField | upload_to='images/'  null=True  blank=True | |
| on_sale | BooleanField | null=True  blank=True | default=False |

## ProductType
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254  null=False  blank=False | |
| friendly_name | Char | max_length=254  null=False  blank=False | |

## Song
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=254  null=True  blank=True | |
| album | ForeignKey | 'Album'  null=True  blank=True  on_delete=models.SET_NULL | default=1 |
| artist | ForeignKey | 'Artist'  null=True  blank=True  on_delete=models.SET_NULL | default=1 |
| duration | Char | max_length=6  null=True  blank=True | |
| track_number | IntegerField | validators=[MaxValueValidator(100), MinValueValidator(1)]  null=False  blank=False | |

## UserProfiles
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- |
| user | OnetoOneField | User  on_delete=models.CASCADE | |
| default_phone_number | Char | max_length=20  null=True  blank=True | |
| default_address1 | Char | max_length=80  null=True  blank=True | |
| default_address2 | Char | max_length=80  null=True  blank=True | |
| default_town_or_city | Char | max_length=40  null=True  blank=True | |
| default_county | Char | max_length=80  null=True  blank=True | |
| default_postcode | Char | max_length=20  null=True  blank=True | |
| default_country | CountryField | blank_label="Country *"  null=True  blank=True | |

## Wishlist
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| products | ManyToManyField | Product  blank=True | |
| created_by | OneToOneField | Userprofile  on_delete.models.CASCADE | |