from flask import Flask
""" __name__ 为当前模块名，当程序在模块自身直接执行时，模块名为__main__
	若是被当作被导入的模块，__name__ != __main__ 
	__name__ 为导入的模块自身的名字""" 
app = Flask(__name__)

"""定义路由 处理url 和 函数之间的关系"""
"""app.route修饰器把修饰的函数注册为路由"""
"""视图函数 def hello_world()"""
""" 修饰器告诉flask什么url可以触发函数"""
@app.route('/')
def hello_world():
	"""返回值为响应"""
	return 'Hello World!'

print(__name__)
if __name__ == '__main__':
	"""app.run()启动flask的开发web服务器"""
	app.run()

	"""可外部访问的服务器 将服务器公开可用"""
	#app.run(host ='0.0.0.0')

	"""调试模式
		服务器在代码变更时 自动重新载入，并在发生错误时提供一个有效的调试器
		不能在生产服务器上使用"""
	"""	app.debug = True
		app.run()
		或者
		app.run(debug = True)"""