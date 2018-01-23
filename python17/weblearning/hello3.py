from flask import Flask,url_for

app = Flask(__name__)

"""第一种情况定义的url 忘记结尾斜线时 会在访问/projects 时自动重定向到 /projects/"""
@app.route('/projects/<name>/')
def projects(name):
	return 'the page %s' % name 

"""第二种情况定义的url ,会在访问/about 时 得到响应 
而添加结尾斜线 则会得到NOT found的结果 """
@app.route('/about')
def about():
	return 'the page about'


"""url_for()使用路由视图函数函数名为第一个参数"""

with app.test_request_context():
	print (url_for('about'))
	"""还可以有一些关键字参数，对应url 规则的变量部分"""
	print(url_for('projects',name = 'lin'))

if __name__ == '__main__':
	app.run(debug = True)




