from django.db.models import *

from account.models import User
from home.models import Reviews


class Catalog(Model):
    name = CharField(max_length=64, verbose_name="catalog")
    gender = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "catalog"
        verbose_name_plural = "catalogs"
        db_table = "catalog"


class SubCatalog(Model):
    name = CharField(max_length=64, verbose_name="sub catalog")
    catalog = ForeignKey(Catalog, on_delete=CASCADE, related_name='sub_catalogs')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sub catalog"
        verbose_name_plural = "sub catalogs"
        db_table = "sub_catalog"


class Material(Model):
    name = CharField(max_length=32, verbose_name="name of material")
    fit = CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materials"
        db_table = "material"


class Compound(Model):
    name = CharField(max_length=16, verbose_name="compound")
    percentage = CharField(max_length=4, verbose_name="percentage")
    material = ForeignKey(Material, on_delete=CASCADE, related_name='compounds')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "compound"
        verbose_name_plural = "compounds"
        db_table = "compound"


class Product(Model):
    name = CharField(max_length=64, verbose_name="product")
    price = PositiveIntegerField(verbose_name="price")
    discount = PositiveIntegerField(default=0, null=True, blank=True, verbose_name="discount")
    style = CharField(max_length=64, verbose_name="style")
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="creation date")
    updated_at = DateTimeField(auto_now=True, null=True, blank=True, verbose_name="update date")
    category = ForeignKey(SubCatalog, on_delete=CASCADE, related_name='products', verbose_name="category")
    material = ForeignKey(Material, on_delete=CASCADE, related_name='material_products', verbose_name="material")
    description = TextField(verbose_name="description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "product"


def get_upload_to(*args):
    print(args)
    # return path.join(self.product.category.name, self.product.name)
    return 'products/'


class Images(Model):
    image = ImageField(upload_to=get_upload_to, verbose_name="image")
    product = ForeignKey(Product, on_delete=CASCADE, related_name='images')
    is_main = BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} image"

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        db_table = "image"


class Parameter(Model):
    size = CharField(max_length=8, verbose_name="size")
    color = CharField(max_length=8, verbose_name="color")
    available = PositiveSmallIntegerField(verbose_name="available")
    product = ForeignKey(Product, on_delete=CASCADE, related_name='parameters')

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
