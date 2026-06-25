from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["QLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(255),nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column (db.Float, nullable=False)
    stock=db.Column(db.Integer,nullable=False)
    def to_dict(self): 
        return{
            "id": self.id,
            "img": self.img,
            "nombre": self.nombre,
            "descripcion": self.descripcion, 
            "precio": self.descripcion,
            "stock": self.stock,
        }

with app.app_context():
    db.create_all()


@app.route("/products")
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict () for product in products])
@app.route("/products" , methods=["POST"])

def create_product():
    data=request.json 
    product = Product(
          img=data["img"],
          nombre=data["nombre"],
          descripcion= data["descripcion"],
          precio=data ["precio"],
          stock=data ["stock"],
     )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()),  201 
    
@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id): 
    product = Product.query.get_or_404(id)
    data = request.json 
    product.img = data ["img"]
    product.nombre = data ["nombre"]
    product.descripcion = data ["descripcion"]
    product.precio = data ["precio"]
    product.stock = data ["stock"] 

    db.session.commit()
    return jsonify(product.to_dict)

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id): 
    product = Product.query.get_or_404(id)
    db.session.delete(product) 
    db.session.commit()
    return jsonify({"message": "Producto eliminado"})

if __name__=="__main__": 
    app.run(debug=True)