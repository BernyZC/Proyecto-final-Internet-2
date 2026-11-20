-- 1. Tabla de Marcas
CREATE TABLE marcas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    pais_origen VARCHAR(100)
);

-- 2. Tabla de Categorías
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- 3. Tabla de Productos (Accesorios para gatos)
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    imagen_producto LONGBLOB NOT NULL,
    marca_id INT NOT NULL,
    categoria_id INT NOT NULL,
    FOREIGN KEY (marca_id) REFERENCES marcas(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
);

-- 4. Tabla de Ventas (Completa las 4 entidades del modelo)
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT NOT NULL,
    nombre_cliente VARCHAR(255) NOT NULL,
    cantidad INT NOT NULL,
    fecha_venta DATE NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
);

-- Datos iniciales para los selectores
INSERT INTO marcas (nombre, pais_origen) VALUES 
('Catit', 'Canadá'),
('Kong Cat', 'Estados Unidos'),
('MichiCraft', 'México'),
('PetSafe', 'Estados Unidos');

INSERT INTO categorias (nombre) VALUES 
('Rascadores y Torres'),
('Juguetes Interactivos'),
('Camas y Cuevas'),
('Comederos y Fuentes'),
('Collares y Arneses');