from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return "INICIO"  "What's up boaitch?!"

@app.route("/logueate")
def logueate():
    return "Log you all in MF's!"

@app.route("/productos")
def consultarProductos():
    return "Returns a list of products MF's!"

@app.route("/productos/agregar")
def agregarProducto():
    return "Adding a product to the list boaitch!"

@app.route("/productos/actualizar")
def actualizarProducto():
    return "Hold on a minute, I'm actualizing the list, boaitch!"
@app.route("/cesta")
def consultarCesta():
    return "Checking your Shopping Cart..."

@app.route("/productos/categoria/<int:id>")
def consultarProductosCategoria(id):
    return "Showing the products of the category number: " + str(id) + ", boaitch!"

@app.route("/clientes/<string:nombre>")
def consultarCliente(nombre):
    return "The client's name is: " + str(nombre) + ", boaitch!"

@app.route("/productos/<float:precio>")
def consultaProductosPorPrecio (precio):
    return "Checking out products, whose prices match: " + str(precio) + "MXN $."

if __name__=='__main__':
    app.run(debug=True)

