SIGEC - Sistema de Gestión de Pacientes (Prueba Técnica)
Aplicación web desarrollada en Django para la gestión básica de pacientes en un entorno clínico simplificado. Permite registrar, listar y consultar pacientes mediante una API REST y una interfaz HTML interactiva.

📌 Funcionalidades
📋 Registrar nuevos pacientes

🔍 Ver listado de pacientes registrados

🌐 API RESTful para consultar, crear y obtener pacientes

🧩 Interfaz web con HTML, CSS y JavaScript (Fetch API)

✅ Validación básica de formularios

🚀 Tecnologías usadas
Django 4+

Django REST Framework

HTML5 + CSS3 + JavaScript (Fetch API)

SQLite (por defecto)

🛠️ Instalación del proyecto
1. Clona el repositorio
bash
Copiar
Editar
git clone https://github.com/tu_usuario/sigec.git
cd sigec
2. Crea y activa un entorno virtual
bash
Copiar
Editar
python -m venv env
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate
3. Instala dependencias
bash
Copiar
Editar
pip install -r requirements.txt
4. Aplica las migraciones (esto crea la base de datos sigec_db)
bash
Copiar
Editar
python manage.py migrate
5. Ejecuta el servidor de desarrollo
bash
Copiar
Editar
python manage.py runserver
🌐 Uso de la aplicación
📄 Interfaz Web (Frontend)
Accede a la URL:

arduino
Copiar
Editar
http://127.0.0.1:8000/inicio/
Desde allí puedes:

Llenar el formulario de paciente

Guardar pacientes

Ver todos los pacientes guardados

🧪 API REST (JSON)
Puedes acceder y probar los siguientes endpoints:

GET /pacientes/: Lista todos los pacientes

POST /pacientes/: Crea un nuevo paciente

GET /pacientes/<id>/: Consulta un paciente por ID

Ejemplo usando curl:

bash
Copiar
Editar
curl http://127.0.0.1:8000/pacientes/
🗃️ Estructura de la base de datos
Tabla: pacientes

Campo	Tipo	Restricción
id	Entero	Clave primaria, autoincremental
nombre	Texto	No nulo
apellido	Texto	No nulo
fecha_nacimiento	Fecha	Opcional
genero	Texto (M/F/O)	No nulo
numero_identificacion	Texto	Único, no nulo

🖼️ Captura de pantalla
(Agrega aquí una imagen de tu interfaz cargada y funcionando)

📤 Entrega
🗂️ Repositorio: https://github.com/tu_usuario/sigec

⏱️ Tiempo invertido: [por ejemplo, 1h 45min]

📧 Enviar enlace del repo + captura a: gestionit@ipsclinicasantamaria.com

✅ Requisitos cumplidos
 Base de datos sigec_db y tabla pacientes

 API RESTful con endpoints GET, POST, GET/<id>

 Formulario funcional con Fetch API

 Lista dinámica de pacientes

 Estilos presentables

 Repositorio público con instrucciones

