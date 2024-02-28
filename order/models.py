from django.db import models

from member.models import Member
from model.models import Period

class Order(Period):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False, blank=False)
    payment = models.TextField(null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)
    delivery_address = models.TextField(null=False, blank=False)
    # 결제 완료 1, 결제 취소 -1
    status = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'tbl_order'
        ordering = ['-id']
