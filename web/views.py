#v1.3 0316
#  0302 添加了登陆页面认证(未登录时访问student_list/会跳转login/,用sessionid验证) 1.1:查询是否数据库已有相同用户名0303 0306:美化了student_list.html;添加google_search_picture.html v1.3:230316:添加多种搜索框&导航栏
#
# from django.views.generic import TemplateView#图标
from django.shortcuts import render,HttpResponse,redirect
from . import models
from exsql import execute
from .models import Student,Username,Aliexpress_goods
from django.core.paginator import Paginator   #这个是处理分页的
#福步产品页
def product(request):
	if request.method=="GET":
		#当有搜索参数时
		if request.GET.get('model') :
			#搜索参数 从title中搜索
			model=request.GET.get('model')
			print('查询型号:',model)
			
			product = models.Aliexpress_goods.objects.filter(model__endswith=model)[0:1]
			product1 = models.Aliexpress_goods.objects.filter(model__endswith=model).first()
			print('类型',type(product1))
			print(product)
		

			#返回结果
			return render(request,"product.html",{'list':product,"title":"搜索产品(官网)"})
#福步搜索产品(官网)
def search(request):
	if request.method=="GET":
		print('参数',request.GET.get('search_string'))
		if not request.GET.get('search_string'):
			page = request.GET.get('page', 1)  # 获取第几页,默认1
			limit = request.GET.get('limit', 20)  # 每页有20条数据
			print('页码',page,'每页条数',limit)
			#类目搜索
			if request.GET.get('category'):
				category=request.GET.get('category')
				print('类目',category)#category为两位数 11 22...
				regex=r'^'+category+'[0-9-]{3,6}' #11XXX 11XXX-01 后面数字3-6位
				search = models.Aliexpress_goods.objects.filter(model__regex=regex)
			else:
				search = models.Aliexpress_goods.objects.all()
				category=""
			print('类型')
			print(type(models.Aliexpress_goods))
			# search = models.Aliexpress_goods.objects.all()
			paginator = Paginator(search, limit)
			page_obj  = paginator.get_page(page)
			print('总条数',page_obj.paginator.count)
			count=page_obj.paginator.count
			import math
			# 计算页数=总条数/每页条数
			page_qty=math.ceil(int(page_obj.paginator.count)/int(limit))
			print('总页数',page_qty)
			page_list=range(1,page_qty)
			# print(search)
			# return render(request,"search.html",{"list":search,"title":"搜索产品(官网)"})
			return render(request,"search.html",{'category':category,'count':count,'page_list':page_list,"list":page_obj ,"title":"搜索产品(官网)"})
		# elif request.method=="POST":
		#当有搜索参数时
		if request.GET.get('search_string') :
			#搜索参数 从title中搜索
			search_string=request.GET.get('search_string')
			print('查询:',search_string)
			#类目搜索
			if request.GET.get('category'):
				category=request.GET.get('category')
				print('类目',category)#category为两位数 11 22...
				regex=r'^'+category+'[0-9-]{3,6}' #11XXX 11XXX-01 后面数字3-6位
				search = models.Aliexpress_goods.objects.filter(title__icontains=search_string,model__regex=regex)
			else:
				category=""
				search = models.Aliexpress_goods.objects.filter(title__icontains=search_string)
			#分页
			page = request.GET.get('page', 1)  # 获取第几页,默认1
			limit = request.GET.get('limit', 20)  # 每页有20条数据
			paginator = Paginator(search, limit)
			page_obj  = paginator.get_page(page)
			#总条数
			print('总条数',page_obj.paginator.count)
			count=page_obj.paginator.count
			import math
			# 计算页数=总条数/每页条数
			page_qty=math.ceil(int(page_obj.paginator.count)/int(limit))
			print('总页数',page_qty)
			page_list=range(1,page_qty)
			
			#返回结果
			return render(request,"search.html",{'category':category,'count':count,'page_list':page_list,'search_string':search_string,"list":page_obj ,"title":"搜索产品(官网)"})
def shipping_list(request):
	# if request.method=="GET":
	if not request.GET.get('oid'):
		shipping_list = models.Shipping_list.objects.all()
		return render(request,"shipping_list.html",{"list":shipping_list,"title":"速卖通发货单"})
	# elif request.method=="POST":
	#当有搜索参数时
	if request.GET.get('oid') or request.GET.get('status') or request.GET.get('goods_title') or request.GET.get('model'):
		#搜索参数1 oid
		oid=request.GET.get('oid')
		print('查询:',oid)
		# 搜索参数2 status
		status=request.GET.get('status')
		print('查询:',status)
		# 搜索参数3 title
		goods_title=request.GET.get('goods_title')
		print('查询:',goods_title)
		# 搜索参数4 model
		model=request.GET.get('model')
		print('查询:',model)
		#查询包含search_string的数据
		shipping_list = models.Shipping_list.objects.filter(oid__icontains=oid).filter(status__icontains=status).filter(goods_title__icontains=goods_title).filter(model__icontains=model)
		#返回结果
		return render(request,"shipping_list.html",{"list":shipping_list,"title":"速卖通发货单"})
#添加数据表数据
#删除数据表数据
def delete(request):
	if request.method == "GET":
		#table = request.GET.get('table')#删除条目所在表
		delete_id=request.GET.get('id') #删除条目的id
		print('删除',delete_id)
		models.Wait_ship_aliexpress_order.objects.filter(id=delete_id).delete()
		return redirect('/wait_ship_aliexpress_order/')#重定向回速卖通订单
##速卖通订单导出
def wait_ship_aliexpress_order(request):
	# if request.method=="GET":
	if not request.GET.get('oid'):
		wait_ship_aliexpress_order_list = models.Wait_ship_aliexpress_order.objects.all()
		return render(request,"wait_ship_aliexpress_order.html",{"list":wait_ship_aliexpress_order_list,"title":"速卖通订单"})
	# elif request.method=="POST":
	if request.GET.get('oid'):
		#搜索参数1 oid
		oid=request.GET.get('oid')
		print('查询:',oid)
		# 搜索参数2 status
		status=request.GET.get('status')
		print('查询:',status)
		# 搜索参数3 title
		goods_title=request.GET.get('goods_title')
		print('查询:',goods_title)
		# 搜索参数4 model
		model=request.GET.get('model')
		print('查询:',model)
		#查询包含search_string的数据
		wait_ship_aliexpress_order_list = models.Wait_ship_aliexpress_order.objects.filter(oid__icontains=oid).filter(status__icontains=status).filter(goods_title__icontains=goods_title).filter(model__icontains=model)
		#返回结果
		return render(request,"wait_ship_aliexpress_order.html",{"list":wait_ship_aliexpress_order_list,"title":"速卖通订单"})

##谷歌搜图
def google_search_picture(request):
	if request.method=="GET":
		google_search_picture_list = models.Google_search_picture.objects.all()
		return render(request,"google_search_picture.html",{"list":google_search_picture_list})
	elif request.method=="POST":
		#获取搜索参数
		search_string=request.POST.get('search_string')
		print('查询:',search_string)
		#查询包含search_string的数据
		google_search_picture_list=models.Google_search_picture.objects.filter(goods1_title__icontains=search_string)
		#返回结果
		return render(request,"google_search_picture.html",{"list":google_search_picture_list})

def student_list(request):
	##用户认证
	#获取浏览器cookies的sessionid
	sessionid=request.session.get('username')
	print(sessionid,type(sessionid))
	if not sessionid :#不存在sessionid:未登录
		return redirect('/login/')#回到登录界面
	#获取数据
	student_queryset = models.Student.objects.all()
	#插入数据
	models.Student.objects.create(name='He Qiuhao',age=20)
	create=models.Student.objects.create(name='Ye Zhihao',age=30)
	yzh=models.Student.objects.filter(name__contains='Ye').first()#查询name包含Ye的数据
	print(create)
	print(yzh)
	print(yzh.name)
	# print(models.Student.objects.filter(name_contains='Zhihao'))
	# print('所有',models.Student.objects.all())
	# print(models.Student.objects.get(name="Ye Zhihao"))#获得1个对象 超过1个符合时报错
	print(models.Student.objects.get(id=3).name)#获取id为1的记录的name str
	# print(models.Student.objects.get(id=1))#获取id为1的记录的name str
	# print(models.Student.objects.get(id=1).delete())#删除
	return render(request,"student_list.html",{"student_queryset":student_queryset})
	# return HttpResponse('haha')
def index(request):
	# return HttpResponse('<h1>你好</h1>')#回应简单文本
	# # 微滤网
	# micro_filter_list = models.Aliexpress_goods.objects.filter(model__regex=r'^11[0-9-]{3,6}$')[0:10]
	# print('微滤网')
	# print(micro_filter_list)
	# # O型圈
	# o_ring_list = models.Aliexpress_goods.objects.filter(model__regex=r'^21[0-9-]{3,6}$')[0:10]
	# print('O型圈')
	# print(o_ring_list)
	# # 密封圈
	# rubber_seal_list = models.Aliexpress_goods.objects.filter(model__regex=r'^22[0-9-]{3,6}$')[0:10]
	# print('密封圈')
	# print(rubber_seal_list)
	# # 塑料件
	# plastic_parts_list = models.Aliexpress_goods.objects.filter(model__regex=r'^3(2|1)[0-9-]{3,6}$')[0:10]
	# print('塑料件')
	# print(plastic_parts_list)
	#更多产品
	# search = models.Aliexpress_goods.objects.all()[0:10]
	print('加载首页')
	# return render(request,"index.html",{'micro_filter_list':micro_filter_list,'o_ring_list':o_ring_list,'rubber_seal_list':rubber_seal_list,'plastic_parts_list':plastic_parts_list,'list':search,"title":"搜索产品(官网)"})
	return render(request,'index.html')
	# return render(request,'index.html',{'name':'叶志豪'})
#注册页 register/
def register(request):
	# return HttpResponse('<h1>你好</h1>')#回应简单文本
	##post发送注册信息，get访问页面
	#POST
	if request.method=='POST':
		#注册页面 实现获取用户注册信息
		username=request.POST.get('username')
		password=request.POST.get('password')
		address=request.POST.get('address')
		province=request.POST.get('province')
		tel=request.POST.get('tel')
		company=request.POST.get('company')
		mail=request.POST.get('mail')
		print('用户:',username,type(username))#Nonetype
		print('密码:',password)
		print('地址:',address)
		print('省份:',province)
		print('电话:',tel)
		print('公司:',company)
		#查询是否数据库已有相同用户名 0303
		from .models import Student, Username
		sql_username=Username.objects.filter(username=username)
		#当用户名已存在时
		if sql_username :
			print('用户名已存在')
			return render(request,'register.html',{'error_msg':'用户名已存在'})
		#当用户名,电话或密码为空时传回错误信息
		if username=='' or password==''or tel=='':
			return render(request,'register.html',{'error_msg':'用户名,电话或密码不能为空'})
		##检测用户名,电话或密码格式,当用户名,电话或密码为非法字符时传回错误信息
		# 正则判断 re.fullmatch 全匹配
		import re
		#(patern ,text)
		#匹配用户名 密码 电话
		#当不匹配时,
		if not re.fullmatch(r'\w+',username) or not re.fullmatch(r'\w+',username) or not re.fullmatch(r'\d+',username):
			return render(request,'register.html',{'error_msg':'用户名,电话或密码包含非法字符'})
		#判断nonetype(首次访问
		elif username is None or password is None or tel is None:
			return render(request,'register.html',{'name':'叶志豪'})
		#当用户名,电话或密码为非空时传回注册成功
		elif username!='' and password!=''and tel!='':
			# print('insert into wk.username(username,password,address,province,tel,company)values("%s","%s","%s","%s","%s","%s")'%(username,password,address,province,tel,company))
			# execute('insert into wk.username(username,password,address,province,tel,company)values("%s","%s","%s","%s","%s","%s")'%(username,password,address,province,tel,company))
			# return HttpResponse('注册成功')

			#写入注册信息到数据库
			from .models import Username
			Username.objects.create(username=username,password=password,tel=tel,address=address,company=company,mail=mail)
			#读取数据库
			print('用户名',Username.objects.get(id=1).username)
			# 设置cookie和session
			request.session['username']=username
			return HttpResponse('注册成功')
		#存入数据库
	elif request.method=='GET':
		return render(request,'register.html')


#显示chenyi_aliexpress的数据库
def show_chenyi_aliexpress(request):
	return render(request,'show_chenyi_aliexpress.html')
#登录页面
def login(request):
	if request.method=='POST':
		#验证用户的用户名和密码是否正确
		# 获取用户输入用户名&密码
		u_username=request.POST.get('username')

		u_password=request.POST.get('password')
		print(u_username,u_password,type(u_username),type(u_password))
		# 从数据库获取用户名和密码
		#获取密码
		# user_info=Username.objects.filter(username=u_username)#execute('select password from wk.username where username=%s'%u_username)
		user_info=Username.objects.filter(username=u_username,password=u_password).first()#execute('select password from wk.username where username=%s'%u_username)

		print(user_info)
		#找不到用户名或者密码
		if not user_info:
			return render(request, 'login.html', {'error_msg': '用户名或者密码错误'})

		# print('长度',len(user_info))
		# length=len(password)
		#如果用户名不存在
		# if len(user_info)==0:
		# 	return render(request,'login.html',{'error_msg':'用户名不存在'})
		# #用户名存在但是密码错误
		# password=user_info.first().password
		# if u_password!=password:
		# 	return render(request,'login.html',{'error_msg':'密码错误'})
		#用户认证
		#获取session看是否为空

		# if not user_session:#session为Nonetype 即为不存在
		# 	return render(request,'login.html',{'error_msg':'会话不存在'})

		#成功:设置cookie和session 60s
		#username写入sessionid到cookie session信息写入django_session 数据表
		request.session['username']=u_username
		response=HttpResponse('设置cookie')
		response.set_cookie('username',u_username,max_age=60*3)
		return redirect('/index/')#挑战index/
	elif request.method=='GET':#get获取
		#登录页
		return render(request,'login.html')