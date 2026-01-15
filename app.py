from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/product/<name>')
def product_detail(name):
    # 예: /product/sunflower 접속 시 products/sunflower.html을 보여줌
    return render_template(f'products/{name}.html')

if __name__ == '__main__':
    app.run(debug=True)