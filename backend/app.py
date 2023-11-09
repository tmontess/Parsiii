from flask import Flask, jsonify, request
from flask_cors import CORS
from articles import articles

app = Flask(__name__)
CORS(app)




# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/articles')
def getArticles():
    # return jsonify(products)
    return jsonify({'articles': articles})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        article for article in articles if article['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Create Data Routes
@app.route('/articles', methods=['POST'])
def addArticle():
    new_article = {
        'id': request.json['id'],
        'title': request.json['title'],
        'body': request.json['body'],
        'fecha': request.json['fecha']
    }
    articles.append(new_article)
    return jsonify({"message":"Artículo agregado satisfactoriamente", 'artcles': articles})

# Update Data Route
@app.route('/products/<string:article_name>', methods=['PUT'])
def editProduct(article_name):
    productsFound = [article for article in articles if article['title'] == article_name]
    if (len(productsFound) > 0):
        productsFound[0]['title'] = request.json['title']
        productsFound[0]['body'] = request.json['body']
        productsFound[0]['fecha'] = request.json['fecha']
        return jsonify({
            'message': 'Article Updated',
            'article': productsFound[0]
        })
    return jsonify({'message': 'Article Not found'})

# DELETE Data Route
@app.route('/products/<string:article_name>', methods=['DELETE'])
def deleteProduct(article_name):
    productsFound = [article for article in articles if article['name'] == article_name]
    if len(productsFound) > 0:
        articles.remove(productsFound[0])
        return jsonify({
            'message': 'Article Deleted',
            'article': articles
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)