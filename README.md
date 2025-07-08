#  SIGEC - Sistema de Gestión de Pacientes (Prueba Técnica)

Aplicación web desarrollada en **Django** para la gestión básica de pacientes en un entorno clínico simplificado. Permite registrar, listar y consultar pacientes mediante una API REST y una interfaz HTML interactiva.

---

##  Funcionalidades

-  Registrar nuevos pacientes
-  Ver listado de pacientes registrados
-  API RESTful para consultar, crear y obtener pacientes
-  Interfaz web con HTML, CSS y JavaScript (Fetch API)
-  Validación básica de formularios

---

##  Tecnologías usadas

- Django 4+
- Django REST Framework
- HTML5 + CSS3 + JavaScript (Fetch API)
- SQLite (por defecto)

---

##  Instalación del proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/sigec.git
cd sigec
```
### 2. Crea y activa un entorno virtual
```bash
python -m venv env
```
 Windows:
```bash
env\Scripts\activate
```
 macOS/Linux:
```bash
source env/bin/activate
```
### 3. Instala dependencias
```bash
pip install -r requirements.txt
```
### 4. Aplica las migraciones (esto crea la base de datos sigec_db)
```bash
python manage.py migrate
```
### 5. Ejecuta el servidor de desarrollo
```bash
python manage.py runserver
```
 Uso de la aplicación
 Interfaz Web (Frontend)
Accede a:

```bash
http://127.0.0.1:8000/inicio/
```
Desde allí puedes:

Llenar el formulario de paciente

Guardar pacientes

Ver todos los pacientes guardados

* API REST (JSON)
Puedes acceder y probar los siguientes endpoints:

GET /pacientes/: Lista todos los pacientes

POST /pacientes/: Crea un nuevo paciente

GET /pacientes/<id>/: Consulta un paciente por ID

Ejemplo usando curl:

```bash
curl http://127.0.0.1:8000/pacientes/
```
* Requisitos cumplidos
 Base de datos sigec_db y tabla pacientes

 API RESTful con endpoints GET, POST, GET/<id>

 Formulario funcional con Fetch API

 Lista dinámica de pacientes

 Estilos presentables

 Repositorio público con instrucciones
