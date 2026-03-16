# 🔐 CiberSeguro — Portal de Ciberseguridad

Proyecto desarrollado con **Django** como parte del Módulo 6 del bootcamp
de desarrollo web full-stack en **Alke Solutions**.

---

## 📋 Descripción

CiberSeguro es una aplicación web informativa sobre ciberseguridad,
desarrollada con el framework Django. Presenta información sobre amenazas
digitales, protocolos de defensa y cuenta con un diseño de estética
hacker/terminal con animaciones CSS.

---

## 🚀 Tecnologías utilizadas

- Python 3.x
- Django
- HTML5
- CSS3 (personalizado con variables y animaciones)
- Bootstrap 5.3 (CDN)
- Google Fonts: `Share Tech Mono` y `Orbitron`
- JavaScript Vanilla (Matrix rain canvas)

---

## 📁 Estructura del proyecto
ciberseguridad/
├── manage.py
├── requirements.txt
├── ciberseguridad/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── base/
│ ├── init.py
│ ├── apps.py
│ ├── views.py
│ └── urls.py
├── templates/
│ └── base/
│ ├── base.html
│ ├── inicio.html
│ ├── amenazas.html
│ ├── consejos.html
│ └── easter_egg.html
└── static/
└── css/
└── estilos.css


---

## ⚙️ Instalación y ejecución local

### 1. Clona el repositorio

git clone https://github.com/tu-usuario/ciberseguro.git
cd ciberseguro

2. Crea y activa el entorno virtual

# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate

3. Instala las dependencias
pip install -r requirements.txt

4. Ejecuta el servidor de desarrollo
python manage.py runserver

5. Abre en tu navegador
http://127.0.0.1:8000/

🗂️ Páginas disponibles
Ruta	Descripción
/	Página de inicio con hero y módulos
/amenazas/	Listado de amenazas cibernéticas con nivel de riesgo
/consejos/	Protocolos de defensa y buenas prácticas

🎯 Requerimientos del módulo cubiertos
✅ Proyecto Django creado y ejecutable

✅ Aplicación base registrada en INSTALLED_APPS

✅ URLs configuradas a nivel de proyecto y de aplicación

✅ Vistas que responden a solicitudes HTTP

✅ Templates HTML con herencia mediante base.html

✅ Datos dinámicos enviados desde vistas con contexto

✅ Archivos estáticos CSS propios integrados

✅ Bootstrap 5 integrado vía CDN

🕹️ Easter Egg
El proyecto incluye una página secreta.
Pista: 01110010 01100101 01110110 01101001 01110011 01100001 00100000 01100101 01101100 00100000 01100110 01101111 01101111 01110100 01100101 01110010 00100000 01100011 01101111 01101110 00100000 01100001 01110100 01100101 01101110 01100011 01101001 11000011 10110011 01101110

👤 Autor
Rodolfo Cádiz
Bootcamp Full-Stack — Alkemy
2026
