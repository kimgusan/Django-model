from django.db import models
from django.db.models import ForeignKey

from cart.models import Cart
from model.models import Period
from product.models import Product


class CartDetail(Period):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, null=False)
    product = ForeignKey(Product, on_delete=models.PROTECT, null=False)
    quantity = models.IntegerField(null=False, default=1)
    # 게시중 0, 결제 완료 1, 결제 취소 -1
    status = models.SmallIntegerField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'tbl_cart_detail'
        ordering = ['-id']