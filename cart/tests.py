from django.db.models import F
from django.test import TestCase

from cart.models import Cart
from cart_detail.models import CartDetail
from member.models import Member
from model import models
from product.managers import ProductManager
from product.models import Product
from random import randint


class CartTest(TestCase):
    # 로그인
    data = {
        'member_email' : 'zzanggu@naver.com',
        'member_password':'zzzz'
    }

    member = Member.enabled_objects.get(**data)

    # 상품 목록
    products = Product.sell_price_objecs.all()

    # 상품 상세페이지
    # print(products[3].__dict__)
    product = products[2]


    # 장바구니에 상품 추가

    # 내 장바구니 가져오기
    my_cart = Cart.objects.filter(status=0, member=member)

    if not my_cart.exists(): # 장바구니가 없을 때 (장바구니에 상품이 하나도 없을 때)
        # 새로운 장바구니를 만들어서 my_cart에 담아준다
        my_cart = Cart.objects.create(member=member)
    else: # 장바구니가 존재할 때(장바구니에 추가된 다른 상품이 존재할 때)
        # 기존 장바구니를 my_cart에 담아준다.
        my_cart = my_cart.first()
    #
    # CartDetail.objects.create(cart=my_cart, product=product, quantity=3)

    # 장바구니 목록
    cart_queryset = Cart.objects.filter(member_id=member.id).annotate(cart_owner=F('member__member_name')).values('id', 'cart_owner')
    # for cart in cart_queryset:
    #     print(cart)


    # 상품 정보, 수량
    ################################## 강사님 코드 #############################################
    # data = {
    #     'member_email': 'zzanggu@naver.com',
    #     'member_password': 'zzzz'
    # }
    #
    # member = Member.enabled_objects.get(**data)
    #
    # carts = CartDetail.objects.filter(status=0, cart=Cart.objects.get(member=member, status=0))
    # for cart in carts:
    #     print(cart.product.__dict__)
    #     print(cart.quantity)
    #     print("=" * 30)

    ########################################################################################
    cart_detail_queryset = CartDetail.objects.all().annotate(상품정보=F('product__product_name')).values('상품정보', 'quantity', 'product__product_price','product_id')
    #
    # for cart_detail in cart_detail_queryset:
    #     products = Product.sell_price_objects.filter(id =cart_detail['product_id'])
    #     for product in products:
    #         print(cart_detail, {product.__dict__['product_sell_price']})

    # 장바구니에 담긴 상품 임의로 삭제
    ################################## 강사님 코드 #############################################
    # 오류 발생 시 자동 롤백을 위해 사용하고,
    # 오류가 없으면 커밋된다.
    # @transaction.atomic # 메소드 전체를 하나의 트랜잭션으로 설정
    # def service(self):
    # with transaction.atomic(): # 블록 전체를 하나의 트랜잭션으로 설정
    #     data = {
    #         'member_email': 'zzanggu@naver.com',
    #         'member_password': 'zzzz'
    #     }
    #
    #     member = Member.enabled_objects.get(**data)
    #
    #     my_cart = Cart.objects.get(member=member, status=0)
    #
    #     carts = CartDetail.objects.filter(status=0, cart=my_cart)
    #     cart = carts[0]
    #     cart.status = -1
    #     cart.save(update_fields=['status'])
    #
    #     if not CartDetail.objects.filter(cart=my_cart, status=0).exists():
    #         my_cart.status = -2
    #         my_cart.save(update_fields=['status'])

    ########################################################################################
    # 장비구니 detail -> 장바구니
    # carts = Cart.objects.all().values()
    # cart_detail = CartDetail.objects.all().values()
    #
    # p_list = []
    #
    # for cart in cart_detail:
    #     p_list.append(cart['product_id'])
    # # 삭제할 상품 id
    # delete_product_id = p_list[randint(0,len(p_list) -1)]
    #
    # cart_detail = CartDetail.objects.filter(product_id =delete_product_id).values().first()
    # # 장바구니 임의의 상품 1개 삭제
    # cart_detail.update(status='-1')
    # print(cart_detail)

