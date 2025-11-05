import uuid

from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, SlugField, DateTimeField, ForeignKey, CASCADE, DecimalField, ImageField
from django.utils.text import slugify


class SlugBasedModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)  # <- title o‘rniga name ishlatildi
            slug = base_slug
            counter = 1

            while self.__class__.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug or str(uuid.uuid4())[:8]

        super().save(*args, **kwargs)


class Category(SlugBasedModel):
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Product(SlugBasedModel):
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    quantity = DecimalField(decimal_places=2, max_digits=10)
    price_in = DecimalField(max_digits=12, decimal_places=2, help_text="Kelish narxi (so‘mda)")
    price_out = DecimalField(max_digits=12, decimal_places=2, help_text="Sotish narxi (so‘mda)")
    image = ImageField(upload_to='products/', blank=True, null=True)
    price_discounted = DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Agar chegirma bo‘lsa, bu narxni kiriting (so‘mda)"
    )

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def clean(self):
        if self.price_discounted is not None:
            if self.price_discounted > self.price_out - self.price_in:
                raise ValidationError({
                    'price_discounted': f"Chegirma narxi kelish narxidan ({self.price_in}) past bo‘la olmaydi!"
                })

    # def calculate_final_price(self):
    #     if self.price_discounted:
    #         return self.price_discounted
    #     return self.price_out

    def save(self, *args, **kwargs):
        self.full_clean()
        # self.final_price = self.calculate_final_price()
        super().save(*args, **kwargs)

    # def get_profit(self):
    #     return self.final_price - self.price_in


