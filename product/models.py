from django.db.models import *
from account.models import User
from home.models import Reviews
from django.utils.translation import gettext_lazy as _


class Catalog(Model):
    name = CharField(max_length=64, verbose_name=_("catalog"))
    gender = BooleanField(default=True, verbose_name="gender")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "catalog"
        verbose_name_plural = "catalogs"
        db_table = "catalog"


class SubCatalog(Model):
    name = CharField(max_length=64, verbose_name=_("sub catalog"))
    catalog = ForeignKey(Catalog, on_delete=CASCADE, related_name='sub_catalogs')
    description = TextField(verbose_name=_("description"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sub catalog"
        verbose_name_plural = "sub catalogs"
        db_table = "sub_catalog"


class Description(Model):
    title = CharField(max_length=128, verbose_name=_("title"))
    description = TextField(verbose_name=_("description"))
    category = ForeignKey(SubCatalog, on_delete=CASCADE, related_name='descriptions')


class Material(Model):
    name = CharField(max_length=32, verbose_name=_("material"))
    fit = CharField(max_length=32, verbose_name=_("fit"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materials"
        db_table = "material"


class Compound(Model):
    name = CharField(max_length=16, verbose_name=_("compound"))
    percentage = PositiveSmallIntegerField(verbose_name=_("percentage"))
    material = ForeignKey(Material, on_delete=CASCADE, related_name=_('compounds'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "compound"
        verbose_name_plural = "compounds"
        db_table = "compound"


class Product(Model):
    name = CharField(max_length=64, verbose_name=_("product"))
    price = PositiveIntegerField(verbose_name=_("price"))
    prev_price = PositiveIntegerField(verbose_name=_("previous price"), null=True, blank=True)
    discount = PositiveIntegerField(default=0, null=True, blank=True, verbose_name=_("discount"))
    style = CharField(max_length=64, verbose_name="style")
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_("creation date"))
    updated_at = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_("update date"))
    category = ForeignKey(SubCatalog, on_delete=CASCADE, related_name='products', verbose_name=_("category"))
    material = ForeignKey(Material, on_delete=CASCADE, related_name='material_products', verbose_name=_("material"))
    description = TextField(verbose_name=_("description"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "product"


def upload_to_path(instance, filename):
    return f'images/{instance.product.name}/{filename}'


class Images(Model):
    image = ImageField(upload_to=upload_to_path, verbose_name="image")
    product = ForeignKey(Product, on_delete=CASCADE, related_name='images')
    is_main = BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} image"

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        db_table = "image"


class Parameter(Model):
    size = CharField(max_length=8, verbose_name=_("size"))
    color = CharField(max_length=8, verbose_name=_("color"))
    available = PositiveSmallIntegerField(verbose_name=_("available"))
    product = ForeignKey(Product, on_delete=CASCADE, related_name=_('parameters'))

    def __str__(self):
        return f"{self.size} {self.color} {self.available}"

    class Meta:
        verbose_name = "parameter"
        verbose_name_plural = "parameters"
        db_table = "parameter"


class ProductReview(Reviews):
    user = ForeignKey(User, on_delete=CASCADE, related_name='product_reviews')
    product = ForeignKey(Product, on_delete=CASCADE, related_name='reviews')
    is_bought = BooleanField(default=False)

    class Meta:
        verbose_name = "product review"
        verbose_name_plural = "product reviews"
        db_table = "product_review"
