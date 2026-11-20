from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import base64

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='tienda_gatos'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        fecha = request.form['fecha_ingreso']
        marca_id = request.form['marca_id']
        categoria_id = request.form['categoria_id']
        imagen = request.files['imagen']
        
        imagen_blob = imagen.read()
        
        cursor.execute(
            """INSERT INTO productos (nombre, precio, fecha_ingreso, imagen_producto, marca_id, categoria_id) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (nombre, precio, fecha, imagen_blob, marca_id, categoria_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('consulta'))
    
    cursor.execute("SELECT * FROM marcas")
    marcas = cursor.fetchall()
    
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('registro.html', marcas=marcas, categorias=categorias)

@app.route('/consulta')
def consulta():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT p.id, p.nombre, p.precio, p.fecha_ingreso, p.imagen_producto, 
               m.nombre AS marca, c.nombre AS categoria
        FROM productos p
        INNER JOIN marcas m ON p.marca_id = m.id
        INNER JOIN categorias c ON p.categoria_id = c.id
    """
    cursor.execute(query)
    productos_db = cursor.fetchall()
    cursor.close()
    conn.close()
    
    productos = []
    for prod in productos_db:
        imagen_b64 = base64.b64encode(prod['imagen_producto']).decode('utf-8')
        prod['imagen_b64'] = imagen_b64
        productos.append(prod)
        
    return render_template('consulta.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)