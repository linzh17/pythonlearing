from flask import Flask

app = Flask(__name__)

"""@app.route('/hello')
def hello():
	return "hello world 2"""

""" 构造动态的url 给url 添加变量 记为<variable_name>"""
"""@app.route('/user/<name>')
def user(name):
	return 'user %s' % name"""

"""转化器<converter:variable_name>"""
"""转化器
	int 整数
	float 浮点数
	path 与默认相似 接受斜线"""
@app.route('/user/<int:post_id>')
def show_user(post_id):
	return 'user'+str(post_id)

if __name__ == '__main__':
	app.run(debug = True)


