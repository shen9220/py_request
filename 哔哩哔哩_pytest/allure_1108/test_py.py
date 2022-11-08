#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

class TestCase:
    #一个类里面所有的用例执行之前（之后）的要做的事情
	def setup_method(self):
		print('所有用例执行之前的事情---如：连接数据库，登陆账号')
	def teardown_method( self ):
		print('所有用例执行之后的事情---断开数据库，退出账号')
	
	# 单个用例执行之前的前置条件，如：打开浏览器，进入网页，输入账号
	# 一般用于登陆的时候
	def setup( self ):
	    print('单个用例执行之前的事情---如：打开浏览器，进入网页，输入账号')
	    
	# 用例执行之前的前置条件，如：关闭浏览器
	def teardown( self ):
		print ( '单个用例执行之后的事情---如：关闭浏览器' )
		print('-----------------------')
		
	#一个函数代表一条用例
	#正确的用例
	def test_01( self ):
		print('第一条用例')
		assert 1==1
		
	#密码错误的用例
	def test_02(self):
		print('第二条用例')
		assert 1==2
		
	# 账号错误的用例
	def test_03 ( self ):
		print('第三条用例')
		assert 1=='1'
	 
	#运行用例的方法：1、终端命令运行：pytest    2、main方法运行
	#多个文件都是测试用例，必须制定用例文件执行
if __name__ == '__main__':
	pytest.main(['-sv','test_py'])   #-sv让用例的结果更加详细