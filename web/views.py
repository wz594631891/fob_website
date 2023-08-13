#v1.3 0316
#  0302 添加了登陆页面认证(未登录时访问student_list/会跳转login/,用sessionid验证) 1.1:查询是否数据库已有相同用户名0303 0306:美化了student_list.html;添加google_search_picture.html v1.3:230316:添加多种搜索框&导航栏
#
# from django.views.generic import TemplateView#图标
from django.shortcuts import render,HttpResponse,redirect
from . import models
from exsql import execute
from .models import Student,Username,Aliexpress_goods
from django.core.paginator import Paginator   #这个是处理分页的
# 介绍页
def profile(request):
	return render(request,"profile.html")
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

#添加数据表数据

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
