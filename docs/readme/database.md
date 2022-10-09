# Database models

## Album - extended from Product model
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| record_label | Char | max_length=254 <br> null=True <br> blank=True | |
| release_year | Char | max_length=4 <br> null=True <br> blank=True | |
| genre | ForeignKey | null=True <br> blank=True <br> on_delete=models.SET_NULL | default=1 |
| digital_download | BooleanField |  null=True <br>  blank=True | | 

## Artist
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254 <br> null=False <br> blank=False <br> help_text="This name should be all lowercase, and contain no spaces, e.g. \"forrest_records\"." | |
| friendly_name | Char | max_length=254 <br> null=False <br> blank=False <br> help_text="This should be the artist name you want users to see." | |

## Blog
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=254 <br> null=False <br> blank=False | |
| author | ForeignKey | UserProfile <br> null=True <br> blank=True <br> on_delete=models.SET_NULL | |
| content | RichTextField (requires ckeditor installation) | | |
| image | ImageField | upload_to='images/' <br> null=True <br> blank=True | |
| image_url | Char | max_length=254 <br> null=True <br> blank=True | |
| date_published | DateField | auto_now_add=True | |

## BlogPage
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=16 <br> null=False <br> blank=False | |
| subtitle | Char | max_length=64 <br> null=False <br> blank=False | |
| featured_blog | ForeignKey | Blog <br> null=True <br> blank=True <br> on_delete=models.SET_NULL | |

## ContactPage
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=16 <br> null=False <br> blank=False | |
| subtitle | Char | max_length=16 <br> null=False <br> blank=False | |

## Genre
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254 <br> null=False <br> blank=False | |
| friendly_name | Char | max_length=254 <br> null=False <br> blank=False | |

## Homepage
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=50 <br> null=False <br> blank=False | |
| lead_paragraph | TextField | | |
| shop_button | Char | max_length=15 <br> null=False <br> blank=False | |
| blog_button | Char | max_length=15 <br> null=False <br> blank=False | |
| facebook_link | Char | max_length=254 <br> null=True <br> blank=True | |
| instagram_link | Char | max_length=254 <br> null=True <br> blank=True | |
| soundcloud_link | Char | max_length=254 <br> null=True <br> blank=True | |
| bandcamp_link | Char | max_length=254 <br> null=True <br> blank=True | |
| bg_image | ImageField | upload_to="images/" <br> null=True <br> blank=True | |

## Merch - extended from Product model
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| has_sizes | BooleanField | null=True <br> blank=True <br> | default=True |

## Messages
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=128 <br> null=False <br> blank=False | |
| email | EmailField | max_length=254 <br> null=False <br> blank=False | |
| message | TextField | null=False <br> blank=False <br> | default="" |
| date_sent | DateField | auto_now_add=True | |

## Order
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| user_profile | ForeignKey | UserProfile <br> null=True <br> blank=True <br> related_name='orders' <br> on_delete=models.SET_NULL | |
| order_number | Charfield | max_length=32 <br> null=False <br> blank=False | |
| full_name | Char | max_length=50 <br> null=False <br> blank=False | |
| email | EmailField | max_length=254 <br> null=False <br> blank=False | |
| phone_number | Char | max_length=20 <br> null=True <br> blank=True | |
| country | CountryField | blank_label="Country *" <br> null=True <br> blank=True | |
| postcode | Char | max_length=20 <br> null=True <br> blank=True | |
| town_or_city | Char | max_length=40 <br> null=True <br> blank=True | |
| address1 | Char | max_length=80 <br> null=True <br> blank=True | |
| address2 | Char | max_length=80 <br> null=True <br> blank=True | |
| county | Char | max_length=80 <br> null=True <br> blank=True | |
| date | DateField | auto_add_now=True | |
| delivery_cost | DecimalField | max_digits=6 <br> decimal_places=2 <br> null=False | default=0 |
| order_total | DecimalField | max_digits=10 <br> decimal_places=2 <br> null=False | default=0 |
| grand_total | DecimalField | max_digits=10 <br> decimal_places=2 <br> null=False | default=0 |
| original_bag | TextField | null=False <br> blank=False | default='' |
| stripe_pid | Char | max_length=254 <br> null=False <br> blank=False | default='' |

## OrderLineItem
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| order | ForeignKey | Order <br> null=False <br> blank=False <br> on_delete=models.CASCADE <br> related_name="lineitems" | |
| product | ForeignKey | Product <br> null=False <br> blank=False <br> on_delete=models.CASCADE | |
| product_size | Char | max_length=2 <br> null=True <br> blank=True | |
| quantity | IntegerField | null=False <br> blank=False | default=0 |
| lineitem_total | DecimalField | max_digits=2 <br> decimal_places=2 <br> null=False <br> blank=False <br> editable=False | |

## Product
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254 <br> null=False <br> blank=False | |
| sku | Char | max_length=254 <br> null=False <br> blank=False | |
| description | TextField | | |
| product_type | ForeignKey | 'ProductType' <br> null=True <br> blank=True <br> on_delete=models.SET_NULL | default=1 |
| artist | ForeignKey | 'Artist' <br> null=True <br> blank=True <br> on_delete=models.SET_NULL | default=1 |
| price | DecimalField | max_digits=6 <br> decimal_places=2 <br> null=False <br> blank=False | |
| image_url | URLField | max_length=1024 <br> null=True <br> blank=True <br> help_text='If you have your image hosted anywhere else, add the link here to server as a backup.' | |
| image | ImageField | upload_to='images/' <br> null=True <br> blank=True | |
| on_sale | BooleanField | null=True <br> blank=True | default=False |

## ProductType
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| name | Char | max_length=254 <br> null=False <br> blank=False | |
| friendly_name | Char | max_length=254 <br> null=False <br> blank=False | |

## Song
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| title | Char | max_length=254 <br> null=True <br> blank=True | |
| album | ForeignKey | 'Album' <br> null=True <br> blank=True <br> on_delete=models.SET_NULL | default=1 |
| artist | ForeignKey | 'Artist' <br> null=True <br> blank=True <br> on_delete=models.SET_NULL | default=1 |
| duration | Char | max_length=6 <br> null=True <br> blank=True | |
| track_number | IntegerField | validators=[MaxValueValidator(100), MinValueValidator(1)] <br> null=False <br> blank=False | |

## UserProfiles
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| user | OnetoOneField | User <br> on_delete=models.CASCADE | |
| default_phone_number | Char | max_length=20 <br> null=True <br> blank=True | |
| default_address1 | Char | max_length=80 <br> null=True <br> blank=True | |
| default_address2 | Char | max_length=80 <br> null=True <br> blank=True | |
| default_town_or_city | Char | max_length=40 <br> null=True <br> blank=True | |
| default_county | Char | max_length=80 <br> null=True <br> blank=True | |
| default_postcode | Char | max_length=20 <br> null=True <br> blank=True | |
| default_country | CountryField | blank_label="Country *" <br> null=True <br> blank=True | |

## Wishlist
| Field | Type | Settings | Defaults |
| ----- | ---- | -------- | -------- |
| products | ManyToManyField | Product <br> blank=True | |
| created_by | OneToOneField | Userprofile <br> on_delete.models.CASCADE | |