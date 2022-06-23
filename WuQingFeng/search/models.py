from django.db import models


# Create your models here.

class Goods(models.Model):
    id = models.BigAutoField(primary_key=True)  # 商品的主键
    store = models.CharField('店铺的名称', max_length=125)  # 品牌名称
    score = models.IntegerField('商品得分', default=100)  # 由用户评价等级最后得出的分数
    title = models.CharField(max_length=225)  # 商品名称
    goods_image = models.TextField('展示图片')  # 展示图片
    shop = models.CharField(max_length=225)  # 店铺名称
    price = models.IntegerField()

    class Meta:
        db_table = 'goods'
