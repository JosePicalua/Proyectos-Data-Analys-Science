**PROYECTO VENTAS DE CARROS**

🔹 Paso 1: Creación de la Base de Datos
Voy a proporcionarte el código SQL para crear una base de datos en PostgreSQL con datos de ventas de autos.

Tablas clave:

vehiculos – Información de los autos (marca, modelo, año, precio, etc.).
ventas – Registro de ventas de autos (fecha, cliente, concesionario, etc.).
clientes – Datos de los clientes que compraron autos.
concesionarios – Ubicaciones donde se vendieron los autos.
Aquí está el SQL para que crees la base de datos en tu PostgreSQL:




-- 1. Crear la base de datos
CREATE DATABASE autos_db;
\c autos_db;

-- 2. Crear tabla de Vehículos
CREATE TABLE vehiculos (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    years INT,
    precio DECIMAL(10,2),
    tipo VARCHAR(30),  -- SUV, Sedán, Hatchback, etc.
    combustible VARCHAR(20),  -- Gasolina, Diésel, Eléctrico, Híbrido
    transmision VARCHAR(20)  -- Automático, Manual
);

-- 3. Crear tabla de Clientes
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    genero VARCHAR(10),
    ciudad VARCHAR(50),
    ingresos DECIMAL(10,2)
);

-- 4. Crear tabla de Concesionarios
CREATE TABLE concesionarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50),
    estado VARCHAR(50)
);

-- 5. Crear tabla de Ventas
CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    vehiculo_id INT REFERENCES vehiculos(id),
    cliente_id INT REFERENCES clientes(id),
    concesionario_id INT REFERENCES concesionarios(id),
    fecha_venta DATE,
    precio_final DECIMAL(10,2),
    metodo_pago VARCHAR(20) -- Crédito, Contado, Leasing
);


🔹 Paso 2: Inserción de Datos
Ahora llena las tablas con datos de prueba. ¿Quieres que te genere algunas inserciones aleatorias o prefieres hacerlo tú?


Voy a generar datos realistas y en una cantidad suficiente para que puedas practicar bien tus consultas en SQL y luego llevarlas a Power BI.

📌 Cantidad de datos:

vehiculos: 50 modelos de autos de distintas marcas.
clientes: 500 clientes con distintos perfiles de edad, género e ingresos.
concesionarios: 10 concesionarios en diferentes ciudades.
ventas: 200 registros de ventas distribuidas entre los autos, clientes y concesionarios.

🔹 Paso 3: Carga de datos individual o en BEGIN

-- Habilitar la extensión para manejar archivos en PostgreSQL
CREATE EXTENSION IF NOT EXISTS file_fdw;

-- Crear la función para cargar datos desde CSV
DO $$
BEGIN
    -- Cargar datos de Vehículos

    \COPY vehiculos(id, marca, modelo, ano, precio, tipo, combustible, transmision) FROM 'C:\\Users\\josep\\OneDrive\\Escritorio\\Proyectos-Junior\\DataSe-SQL\\Ventas De Carros\\vehiculos csv' DELIMITER ',' CSV HEADER;
    
    \COPY clientes(id, nombre, edad, genero, ciudad, ingresos) FROM 'C:\\Users\\josep\\OneDrive\\Escritorio\\Proyectos-Junior\\DataSe-SQL\\Ventas De Carros\\clientes.csv' DELIMITER ',' CSV HEADER;
    
    \COPY concesionarios(id, nombre, ciudad, estado) FROM 'C:\\Users\\josep\\OneDrive\\Escritorio\\Proyectos-Junior\\DataSe-SQL\\Ventas De Carros\\concesionarios.csv' DELIMITER ',' CSV HEADER;
    
    \COPY ventas(id, vehiculo_id, cliente_id, concesionario_id, fecha_venta, precio_final, metodo_pago) FROM 'C:\\Users\\josep\\OneDrive\\Escritorio\\Proyectos-Junior\\DataSe-SQL\\Ventas De Carros\\ventas2.csv' DELIMITER ',' CSV HEADER;

END $$;

🔹 Paso 4: Preguntas Empresariales
Aquí algunas preguntas que una empresa automotriz podría hacer:
"Resueltos"
📊 ¿Cuál es la marca más vendida en el último año?
🏆 ¿Qué modelo tiene más ventas en cada concesionario?
📈 ¿Cuál es la tendencia de ventas de autos eléctricos en los últimos 3 años?
💰 ¿Cuáles son los ingresos totales por concesionario?
""A resolver""
🛣️ ¿En qué ciudad se venden más autos de lujo (>50,000 USD)?
👥 ¿Qué grupo de edad compra más autos y de qué tipo?
⚡ ¿Los clientes con ingresos altos prefieren autos eléctricos o de combustión?
💳 ¿Qué método de pago es el más usado por los clientes?
🚘 ¿Cuál es la tasa de compra de autos nuevos vs usados (si lo agregamos)?
🛒 ¿Cuál es el ticket promedio de una venta?


***Todas las consultas que se haran, se guardaran en el archivo proyectoBuyCar.db***