#-----------------------
# 匯入Flask類別
#-----------------------
from flask import Flask,render_template

#-----------------------
# 產生一個Flask物件
# 名稱為app
#-----------------------
app = Flask(__name__)

#-----------------------
# 用裝飾器定義app的路由
#-----------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer/test')
def customer_test():
    """
    data={}
    data["name"]="王小明"
    data["gender"]="F"
    """
    data={'name':'王小明','gender':'F','age':20}
    return render_template("test.html",data=data)

@app.route('/customer/list')
def customer_list():

    data=[{"name":"王小明","gender":"F","age":20},
          {"name":"王小明","gender":"F","age":21},
          {"name":"王小明","gender":"M","age":22},
          {"name":"王小明","gender":"F","age":23},
          {"name":"王小明","gender":"F","age":24}]
    return render_template("list.html",data=data)
    

#-----------------------
# 執行app
#-----------------------
if __name__ == '__main__':
    app.run(port=5000,debug=True)