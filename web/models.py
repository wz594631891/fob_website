from django.db import models
#官网产品
class Aliexpress_goods(models.Model):
    height  = models.TextField(null=True,verbose_name="单号")
    oe=models.TextField(null=True,verbose_name="订单状态")
    material  = models.TextField(null=True,verbose_name="买家名称")
    pic1_loc  = models.DateTimeField(null=True,default='2023-01-01 00:00:00',verbose_name="付款时间")
    pic2_loc  = models.TextField(null=True,verbose_name="产品总金额")
    pic3_loc  = models.TextField(null=True,verbose_name="快递费")
    pic4_loc  = models.TextField(null=True,verbose_name="订单金额")
    pic5_loc  = models.TextField(null=True,verbose_name="商品信息")
    pic6_loc  = models.TextField(null=True,verbose_name="商品编码")
    title    = models.TextField(null=True,verbose_name="商品编码")
    pic1_url    = models.TextField(null=True,verbose_name="商品编码")
    pic2_url    = models.TextField(null=True,verbose_name="商品编码")
    pic3_url    = models.TextField(null=True,verbose_name="商品编码")
    pic4_url    = models.TextField(null=True,verbose_name="商品编码")
    pic5_url    = models.TextField(null=True,verbose_name="商品编码")
    pic6_url      = models.TextField(null=True,verbose_name="商品编码")
    length    = models.TextField(null=True,verbose_name="商品编码")
    width    = models.TextField(null=True,verbose_name="商品编码")
    vid_loc   = models.TextField(null=True,verbose_name="商品编码")
    model   = models.TextField(null=True,verbose_name="商品编码")

    #创建时间(只在记录创建时变动,然后不可修改)
    time =models.DateTimeField(null=True,auto_now_add=True)
#速卖通待发货
class Wait_ship_aliexpress_order(models.Model):
    """
    CharField 类型必须设置 max_length 参数
    verbose_name 是对字段的解释,每个字段都有,且是第一个默认形参,所以可以直接在第一个位置实参处写值不需要写verbose_name=
    null=True 允许字段为空
    default=0 设置默认值
    """
    # id int primary key auto_increment;(sql语句效果与下面orm语句相同)
    id = models.AutoField(primary_key=True,verbose_name="主键ID")
    # name varchar(32);
    oid = models.TextField(null=True,verbose_name="单号")
    status = models.TextField(null=True,verbose_name="订单状态")
    buyer = models.TextField(null=True,verbose_name="买家名称")
    pay_time = models.DateTimeField(null=True,default='2023-01-01 00:00:00',verbose_name="付款时间")
    product_amount = models.TextField(null=True,verbose_name="产品总金额")
    shipping_fee = models.TextField(null=True,verbose_name="快递费")
    order_amount = models.TextField(null=True,verbose_name="订单金额")
    goods_title = models.TextField(null=True,verbose_name="商品信息")
    model = models.TextField(null=True,verbose_name="商品编码")
    tips = models.TextField(null=True,verbose_name="订单备注")
    address = models.TextField(null=True,verbose_name="收货地址")
    receiver = models.TextField(null=True,verbose_name="收件人名称")
    country = models.TextField(null=True,verbose_name="国家")
    express = models.TextField(null=True,verbose_name="物流")
    ship_limit = models.DateTimeField(null=True,verbose_name="发货期限")
    ship_time = models.DateTimeField(null=True,verbose_name="发货时间")
    time=models.DateTimeField(null=True,auto_now=True)#更新时间
    #区号 电话
    area_code = models.TextField(null=True,verbose_name="区号")
    tel = models.TextField(null=True,verbose_name="电话")
    #数量(非导出获取)
    quantity=models.IntegerField(null=True,verbose_name="数量")
    #邮编
    zip_code =models.TextField(null=True,verbose_name="邮编")
    my_tip = models.TextField(null=True,verbose_name="内部备注")
    tracking_number = models.TextField(null=True,verbose_name="跟踪号")
    #拆分份数 型号 数量
    goods1_copy = models.IntegerField(null=True,verbose_name="份数")
    goods2_copy = models.IntegerField(null=True,verbose_name="份数")
    goods3_copy = models.IntegerField(null=True,verbose_name="份数")
    goods4_copy = models.IntegerField(null=True,verbose_name="份数")
    goods5_copy = models.IntegerField(null=True,verbose_name="份数")
    goods6_copy = models.IntegerField(null=True,verbose_name="份数")
    goods7_copy = models.IntegerField(null=True,verbose_name="份数")
    goods8_copy = models.IntegerField(null=True,verbose_name="份数")
    goods9_copy = models.IntegerField(null=True,verbose_name="份数")
    goods10_copy = models.IntegerField(null=True,verbose_name="份数")
    goods11_copy = models.IntegerField(null=True,verbose_name="份数")
    goods12_copy = models.IntegerField(null=True,verbose_name="份数")
    goods13_copy = models.IntegerField(null=True,verbose_name="份数")
    goods14_copy = models.IntegerField(null=True,verbose_name="份数")
    goods15_copy = models.IntegerField(null=True,verbose_name="份数")
    goods1_model=models.TextField(null=True,verbose_name="型号")
    goods2_model=models.TextField(null=True,verbose_name="型号")
    goods3_model=models.TextField(null=True,verbose_name="型号")
    goods4_model=models.TextField(null=True,verbose_name="型号")
    goods5_model=models.TextField(null=True,verbose_name="型号")
    goods6_model=models.TextField(null=True,verbose_name="型号")
    goods7_model=models.TextField(null=True,verbose_name="型号")
    goods8_model=models.TextField(null=True,verbose_name="型号")
    goods9_model=models.TextField(null=True,verbose_name="型号")
    goods10_model=models.TextField(null=True,verbose_name="型号")
    goods11_model=models.TextField(null=True,verbose_name="型号")
    goods12_model=models.TextField(null=True,verbose_name="型号")
    goods13_model=models.TextField(null=True,verbose_name="型号")
    goods14_model=models.TextField(null=True,verbose_name="型号")
    goods15_model=models.TextField(null=True,verbose_name="型号")
    goods1_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods2_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods3_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods4_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods5_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods6_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods7_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods8_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods9_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods10_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods11_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods12_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods13_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods14_total_qty= models.IntegerField(null=True,verbose_name="总数")
    goods15_total_qty= models.IntegerField(null=True,verbose_name="总数")

    #创建时间(只在记录创建时变动,然后不可修改)
    create_time=models.DateTimeField(null=True,auto_now_add=True)
class Shipping_list(models.Model):
    """
    CharField 类型必须设置 max_length 参数
    verbose_name 是对字段的解释,每个字段都有,且是第一个默认形参,所以可以直接在第一个位置实参处写值不需要写verbose_name=
    null=True 允许字段为空
    default=0 设置默认值
    """
    # id int primary key auto_increment;(sql语句效果与下面orm语句相同)
    id = models.AutoField(primary_key=True,verbose_name="主键ID")
    # name varchar(32);
    oid = models.TextField(null=True,verbose_name="单号")
    status = models.TextField(null=True,verbose_name="订单状态")
    buyer = models.TextField(null=True,verbose_name="买家名称")
    pay_time = models.DateTimeField(null=True,default='2023-01-01 00:00:00',verbose_name="付款时间")
    product_amount = models.TextField(null=True,verbose_name="产品总金额")
    shipping_fee = models.TextField(null=True,verbose_name="快递费")
    order_amount = models.TextField(null=True,verbose_name="订单金额")
    goods_title = models.TextField(null=True,verbose_name="商品信息")
    model = models.TextField(null=True,verbose_name="商品编码")
    tips = models.TextField(null=True,verbose_name="订单备注")
    address = models.TextField(null=True,verbose_name="收货地址")
    receiver = models.TextField(null=True,verbose_name="收件人名称")
    country = models.TextField(null=True,verbose_name="国家")
    express = models.TextField(null=True,verbose_name="物流")
    ship_limit = models.DateTimeField(null=True,verbose_name="发货期限")
    ship_time = models.DateTimeField(null=True,verbose_name="发货时间")
    time=models.DateTimeField(null=True,auto_now=True)#更新时间
    #区号 电话
    area_code = models.TextField(null=True,verbose_name="区号")
    tel = models.TextField(null=True,verbose_name="电话")
    #邮编
    zip_code =models.TextField(null=True,verbose_name="邮编")
    my_tip = models.TextField(null=True,verbose_name="内部备注")
    #数量(非导出获取)
    quantity=models.IntegerField(null=True,verbose_name="数量")
    #创建时间(只在记录创建时变动,然后不可修改)
    create_time=models.DateTimeField(null=True,auto_now_add=True)
    tracking_number = models.TextField(null=True,verbose_name="跟踪号")
class Student(models.Model):
    """
    CharField 类型必须设置 max_length 参数
    verbose_name 是对字段的解释,每个字段都有,且是第一个默认形参,所以可以直接在第一个位置实参处写值不需要写verbose_name=
    null=True 允许字段为空
    default=0 设置默认值
    """
    # id int primary key auto_increment;(sql语句效果与下面orm语句相同)
    id = models.AutoField(primary_key=True,verbose_name="主键ID")
    # name varchar(32);
    name = models.CharField(null=True,max_length=32,verbose_name="名字")
    # age int;
    age = models.IntegerField(null=True,verbose_name="年龄")
    # pwd int;
    pwd = models.IntegerField(null=True,verbose_name="密码")
	#性别
    gender=models.CharField(null=True,max_length=10,verbose_name="性别")
	#年级
    grade = models.IntegerField(null=True,default=0)
	#
    is_delete = models.IntegerField(null=True,default=0)

class Username(models.Model):
	"""website项目	用户表"""
	#建立字段
	username=models.CharField(null=True,verbose_name='用户名' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	password=models.CharField(null=True,verbose_name='密码' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	tel=models.CharField(null=True,verbose_name='电话' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	address=models.CharField(null=True,verbose_name='地址' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	company=models.CharField(null=True,verbose_name='公司' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	mail=models.CharField(null=True,verbose_name='邮箱' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	# age=models.IntegerField(null=True,verbose_name='用户表密码' ) #charfield 整数类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	# account=models.DecimalField(null=True,verbose_name='用户表密码' ,max_digits=10,decimal_places=2) #精准数据类型 最大数位 精确到2位

	time=models.DateTimeField(null=True,verbose_name='时间',auto_now_add=True)#时间戳
class Google_search_picture(models.Model):
    """
    CharField 类型必须设置 max_length 参数
    verbose_name 是对字段的解释,每个字段都有,且是第一个默认形参,所以可以直接在第一个位置实参处写值不需要写verbose_name=
    null=True 允许字段为空
    default=0 设置默认值
    """
    # id int primary key auto_increment;(sql语句效果与下面orm语句相同)
    id = models.AutoField(primary_key=True,verbose_name="主键ID")
    # name varchar(32);
    title = models.TextField(null=True,verbose_name="标题")
    #图片url
    pic1_url = models.TextField(null=True,verbose_name="图片url")
    pic1_loc_img = models.TextField(null=True,verbose_name="标签图片url")
    pic2_url = models.TextField(null=True,verbose_name="图片url")
    pic3_url = models.TextField(null=True,verbose_name="图片url")
    pic4_url = models.TextField(null=True,verbose_name="图片url")
    pic5_url = models.TextField(null=True,verbose_name="图片url")
    pic6_url = models.TextField(null=True,verbose_name="图片url")
    #图片位置
    pic1_loc = models.TextField(null=True,verbose_name="图片位置")
    pic2_loc = models.TextField(null=True,verbose_name="图片位置")
    pic3_loc = models.TextField(null=True,verbose_name="图片位置")
    pic4_loc = models.TextField(null=True,verbose_name="图片位置")
    pic5_loc = models.TextField(null=True,verbose_name="图片位置")
    pic6_loc = models.TextField(null=True,verbose_name="图片位置")
    #搜图查到的图url
    goods1_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods2_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods3_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods4_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods5_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods6_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods7_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods8_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods9_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    goods10_pic_url = models.TextField(null=True,verbose_name="搜图查到的图url")
    #找到的10个产品url
    goods1_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods2_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods3_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods4_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods5_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods6_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods7_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods8_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods9_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    goods10_url = models.TextField(null=True,verbose_name="找到的10个产品url")
    #查到的标题
    goods1_title = models.TextField(null=True,verbose_name="查到的标题")
    goods2_title = models.TextField(null=True,verbose_name="查到的标题")
    goods3_title = models.TextField(null=True,verbose_name="查到的标题")
    goods4_title = models.TextField(null=True,verbose_name="查到的标题")
    goods5_title = models.TextField(null=True,verbose_name="查到的标题")
    goods6_title = models.TextField(null=True,verbose_name="查到的标题")
    goods7_title = models.TextField(null=True,verbose_name="查到的标题")
    goods8_title = models.TextField(null=True,verbose_name="查到的标题")
    goods9_title = models.TextField(null=True,verbose_name="查到的标题")
    goods10_title = models.TextField(null=True,verbose_name="查到的标题")
    #已经搜图
    search_picture = models.TextField(null=True,verbose_name="已经搜图")
    #更新时间
    time=models.DateTimeField(null=True,auto_now=True)
    #创建时间(只在记录创建时变动,然后不可修改)
    create_time=models.DateTimeField(null=True,auto_now_add=True)
    # # age int;
    # age = models.IntegerField(null=True,verbose_name="年龄")
    # # pwd int;
    # pwd = models.IntegerField(null=True,"密码",null=True)
    # #性别
    # gender=models.CharField(null=True,max_length=10,verbose_name="性别")
    # #年级
    # grade = models.IntegerField(null=True,default=0)
    # #
    # is_delete = models.IntegerField(null=True,default=0)
