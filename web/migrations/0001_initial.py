# Generated by Django 4.1.5 on 2023-04-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliexpress_goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.TextField(null=True, verbose_name='单号')),
                ('oe', models.TextField(null=True, verbose_name='订单状态')),
                ('material', models.TextField(null=True, verbose_name='买家名称')),
                ('pic1_loc', models.DateTimeField(default='2023-01-01 00:00:00', null=True, verbose_name='付款时间')),
                ('pic2_loc', models.TextField(null=True, verbose_name='产品总金额')),
                ('pic3_loc', models.TextField(null=True, verbose_name='快递费')),
                ('pic4_loc', models.TextField(null=True, verbose_name='订单金额')),
                ('pic5_loc', models.TextField(null=True, verbose_name='商品信息')),
                ('pic6_loc', models.TextField(null=True, verbose_name='商品编码')),
                ('title', models.TextField(null=True, verbose_name='商品编码')),
                ('pic1_url', models.TextField(null=True, verbose_name='商品编码')),
                ('pic2_url', models.TextField(null=True, verbose_name='商品编码')),
                ('pic3_url', models.TextField(null=True, verbose_name='商品编码')),
                ('pic4_url', models.TextField(null=True, verbose_name='商品编码')),
                ('pic5_url', models.TextField(null=True, verbose_name='商品编码')),
                ('pic6_url', models.TextField(null=True, verbose_name='商品编码')),
                ('length', models.TextField(null=True, verbose_name='商品编码')),
                ('width', models.TextField(null=True, verbose_name='商品编码')),
                ('vid_loc', models.TextField(null=True, verbose_name='商品编码')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Google_search_picture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键ID')),
                ('title', models.TextField(null=True, verbose_name='标题')),
                ('pic1_url', models.TextField(null=True, verbose_name='图片url')),
                ('pic1_loc_img', models.TextField(null=True, verbose_name='标签图片url')),
                ('pic2_url', models.TextField(null=True, verbose_name='图片url')),
                ('pic3_url', models.TextField(null=True, verbose_name='图片url')),
                ('pic4_url', models.TextField(null=True, verbose_name='图片url')),
                ('pic5_url', models.TextField(null=True, verbose_name='图片url')),
                ('pic6_url', models.TextField(null=True, verbose_name='图片url')),
                ('pic1_loc', models.TextField(null=True, verbose_name='图片位置')),
                ('pic2_loc', models.TextField(null=True, verbose_name='图片位置')),
                ('pic3_loc', models.TextField(null=True, verbose_name='图片位置')),
                ('pic4_loc', models.TextField(null=True, verbose_name='图片位置')),
                ('pic5_loc', models.TextField(null=True, verbose_name='图片位置')),
                ('pic6_loc', models.TextField(null=True, verbose_name='图片位置')),
                ('goods1_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods2_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods3_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods4_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods5_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods6_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods7_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods8_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods9_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods10_pic_url', models.TextField(null=True, verbose_name='搜图查到的图url')),
                ('goods1_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods2_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods3_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods4_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods5_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods6_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods7_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods8_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods9_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods10_url', models.TextField(null=True, verbose_name='找到的10个产品url')),
                ('goods1_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods2_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods3_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods4_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods5_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods6_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods7_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods8_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods9_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('goods10_title', models.TextField(null=True, verbose_name='查到的标题')),
                ('search_picture', models.TextField(null=True, verbose_name='已经搜图')),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_list',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键ID')),
                ('oid', models.TextField(null=True, verbose_name='单号')),
                ('status', models.TextField(null=True, verbose_name='订单状态')),
                ('buyer', models.TextField(null=True, verbose_name='买家名称')),
                ('pay_time', models.DateTimeField(default='2023-01-01 00:00:00', null=True, verbose_name='付款时间')),
                ('product_amount', models.TextField(null=True, verbose_name='产品总金额')),
                ('shipping_fee', models.TextField(null=True, verbose_name='快递费')),
                ('order_amount', models.TextField(null=True, verbose_name='订单金额')),
                ('goods_title', models.TextField(null=True, verbose_name='商品信息')),
                ('model', models.TextField(null=True, verbose_name='商品编码')),
                ('tips', models.TextField(null=True, verbose_name='订单备注')),
                ('address', models.TextField(null=True, verbose_name='收货地址')),
                ('receiver', models.TextField(null=True, verbose_name='收件人名称')),
                ('country', models.TextField(null=True, verbose_name='国家')),
                ('express', models.TextField(null=True, verbose_name='物流')),
                ('ship_limit', models.DateTimeField(null=True, verbose_name='发货期限')),
                ('ship_time', models.DateTimeField(null=True, verbose_name='发货时间')),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('area_code', models.TextField(null=True, verbose_name='区号')),
                ('tel', models.TextField(null=True, verbose_name='电话')),
                ('zip_code', models.TextField(null=True, verbose_name='邮编')),
                ('my_tip', models.TextField(null=True, verbose_name='内部备注')),
                ('quantity', models.IntegerField(null=True, verbose_name='数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('tracking_number', models.TextField(null=True, verbose_name='跟踪号')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='名字')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('pwd', models.IntegerField(null=True, verbose_name='密码')),
                ('gender', models.CharField(max_length=10, null=True, verbose_name='性别')),
                ('grade', models.IntegerField(default=0, null=True)),
                ('is_delete', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, null=True, verbose_name='密码')),
                ('tel', models.CharField(max_length=100, null=True, verbose_name='电话')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='地址')),
                ('company', models.CharField(max_length=100, null=True, verbose_name='公司')),
                ('mail', models.CharField(max_length=100, null=True, verbose_name='邮箱')),
                ('time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='Wait_ship_aliexpress_order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键ID')),
                ('oid', models.TextField(null=True, verbose_name='单号')),
                ('status', models.TextField(null=True, verbose_name='订单状态')),
                ('buyer', models.TextField(null=True, verbose_name='买家名称')),
                ('pay_time', models.DateTimeField(default='2023-01-01 00:00:00', null=True, verbose_name='付款时间')),
                ('product_amount', models.TextField(null=True, verbose_name='产品总金额')),
                ('shipping_fee', models.TextField(null=True, verbose_name='快递费')),
                ('order_amount', models.TextField(null=True, verbose_name='订单金额')),
                ('goods_title', models.TextField(null=True, verbose_name='商品信息')),
                ('model', models.TextField(null=True, verbose_name='商品编码')),
                ('tips', models.TextField(null=True, verbose_name='订单备注')),
                ('address', models.TextField(null=True, verbose_name='收货地址')),
                ('receiver', models.TextField(null=True, verbose_name='收件人名称')),
                ('country', models.TextField(null=True, verbose_name='国家')),
                ('express', models.TextField(null=True, verbose_name='物流')),
                ('ship_limit', models.DateTimeField(null=True, verbose_name='发货期限')),
                ('ship_time', models.DateTimeField(null=True, verbose_name='发货时间')),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('area_code', models.TextField(null=True, verbose_name='区号')),
                ('tel', models.TextField(null=True, verbose_name='电话')),
                ('quantity', models.IntegerField(null=True, verbose_name='数量')),
                ('zip_code', models.TextField(null=True, verbose_name='邮编')),
                ('my_tip', models.TextField(null=True, verbose_name='内部备注')),
                ('tracking_number', models.TextField(null=True, verbose_name='跟踪号')),
                ('goods1_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods2_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods3_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods4_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods5_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods6_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods7_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods8_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods9_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods10_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods11_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods12_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods13_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods14_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods15_copy', models.IntegerField(null=True, verbose_name='份数')),
                ('goods1_model', models.TextField(null=True, verbose_name='型号')),
                ('goods2_model', models.TextField(null=True, verbose_name='型号')),
                ('goods3_model', models.TextField(null=True, verbose_name='型号')),
                ('goods4_model', models.TextField(null=True, verbose_name='型号')),
                ('goods5_model', models.TextField(null=True, verbose_name='型号')),
                ('goods6_model', models.TextField(null=True, verbose_name='型号')),
                ('goods7_model', models.TextField(null=True, verbose_name='型号')),
                ('goods8_model', models.TextField(null=True, verbose_name='型号')),
                ('goods9_model', models.TextField(null=True, verbose_name='型号')),
                ('goods10_model', models.TextField(null=True, verbose_name='型号')),
                ('goods11_model', models.TextField(null=True, verbose_name='型号')),
                ('goods12_model', models.TextField(null=True, verbose_name='型号')),
                ('goods13_model', models.TextField(null=True, verbose_name='型号')),
                ('goods14_model', models.TextField(null=True, verbose_name='型号')),
                ('goods15_model', models.TextField(null=True, verbose_name='型号')),
                ('goods1_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods2_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods3_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods4_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods5_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods6_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods7_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods8_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods9_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods10_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods11_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods12_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods13_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods14_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('goods15_total_qty', models.IntegerField(null=True, verbose_name='总数')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
