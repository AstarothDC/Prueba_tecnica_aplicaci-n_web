CREATE DATABASE sigec_db;

-- Conectar a la base de datos 
\c sigec_db;

-- Crear la tabla pacientes
CREATE TABLE pacientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    genero VARCHAR(1) CHECK (genero IN ('M', 'F', 'O')),
    numero_identificacion VARCHAR(50) UNIQUE NOT NULL
);
