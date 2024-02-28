from django.db import models

from member.models import Member
from model.models import Period
from post.models import Post


class Reply(Period):
    PRIVATE_CHOICE = [
        (0, '공개'),
        (1, '비공개')
    ]

    reply_content = models.CharField(null=False, blank=False, max_length=200)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.PROTECT)
    group_id = models.BigIntegerField(null=False, blank=False, default=1)
    reply_depth = models.BigIntegerField(null=False, blank=False, default=1)
    reply_private_status = models.BooleanField(null=False, blank=False, default=0, choices=PRIVATE_CHOICE)

    class Meta:
        db_table = 'tbl_reply'
        ordering = ['-id']

    def __str__(self):
        return self.reply_content
