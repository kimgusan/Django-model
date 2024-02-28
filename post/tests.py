from django.test import TestCase

from member.models import Member
from post.models import Post
import random as r
# print(r.randint(1,10))


class PostTest(TestCase):
    # 총 98개 게시글 작성하기
    # 랜넘한 회원을 작성자로 설정하기

    # random_list = []
    # member_queryset = Member.objects.all()
    # for member in member_queryset:
    #     random_list.append(member.id)
    #
    # for i in range(98):
    #     random_index = r.randint(0, len(random_list) - 1)
    #     random_value = random_list[random_index]
    #     Post.objects.create(
    #     post_title = f"게시글제목{i}",
    #     post_content = f"게시글내용{i}",
    #     member_id = random_value
    #     )

# ======================================
#     posts = []
#     # 랜덤한 회원을 작성자로 설정하기
#     member_queryset = Member.objects.all()
#     # 총 98개 게시글 작성하기
#     for i in range(98):
#
#         post = {
#             'post_title': f'테스트 제목{i + 1}',
#             'post_content': f'테스트 내용{i + 1}',
#             'member': member_queryset[randint(0, len(member_queryset) - 1)]
#         }
        # 트러블 슈팅
        # Code: posts.append(post)
        # Error: AttributeError: 'dict' object has no attribute 'pk'

        # dict객체를 Django ORM에 전달하면 정확히 인식이 안되었다.
        # 이를 모델 객체에 담아서 전달하니 정확이 인식되었다.
    #
    #     posts.append(Post(**post))
    #
    # Post.objects.bulk_create(posts)

    # 로그인된 회원의 마이페이지에서 내가 작성한 게시글 조회하기
    #     member = Member.objects.get(member_status=True, id=3)
    #     for post in member.post_set.all():
    #         print(post)
#===========================================================
    #     posts = Post.objects.filter(member_id=3)
    #     for post in posts:
    #         print(post.__dict__, post.member.member_name, sep ='\n')

    # 나이가 30 미만인 회원이 작성한 게시글 목록 조회
    # 단, 회원의 이름과 회원의 나이까지 같이 조회하기
    # (member__member_name, member__member_age)

# ※ 과제
    #   1. 정방향으로 직접 참조
    # members = Member.objects.filter(member_status=True, member_age__lt=30)
    # for member in members:
    #     post_queryset = Post.objects.filter(member_id=member.id)
    #     for post in post_queryset:
    #         print(post.post_content, post.member.member_name, post.member.member_age, sep=' / ')

    # posts = Post.objects.filter(member__member_status=True, member__member_age__lt=30).order_by('member_id')
    # for post in posts:
    #     print(post.post_content, post.member.member_name, post.member.member_age, sep=' / ')

    print("------------------------------------------------------------------------")
    #   2. 한번에 참조(member__member_name, member__member_age)
    posts = Post.objects.filter(member__member_age__lt=30).values('id','post_content', 'member__member_name','member__member_age')
    for post in posts:
        print(post)

    # A필드에 b가 있다고 가정한다.
    # a.b: a로 b필드에 접근하면 정방향 참조이고, b의 null 상태에 따라 내부 또는 외부조인이 실행된다.
    # b.a: b로 a필드에 접근하면 역방향 참조이고, b의 모든 정보가 나와야하기 때문에 항상 외부조인이  실행된다.

    # EAGER(즉시)
    # 실행하는 순간 쿼리가 실행된 뒤, 이후 쿼리가 발생하지 않는다.
    # 하나의 서비스에서 여러 번 JOIN해야 할 경우 사용한다.
    # print(Post.objects.select_related('member', 'reply', 'category').values('id','post_title', 'member__member_name').query)

    # LAZY(지연)
    # 실행할 때 쿼리가 만들어지고 킬드에 접근할 때마다 쿼리가 발생한다.
    # print(Post.objects.values('member__member_name').query)
    # print(Member.objects.values('post__post_title').query)
    pass

