Django Article CRUD Application
Descripción
Este proyecto Django proporciona una aplicación básica para la gestión de artículos con operaciones CRUD (Crear, Leer, Actualizar, Eliminar). 
La aplicación permite a los usuarios crear, ver, actualizar y eliminar artículos a través de una interfaz web.
Requisitos
•	Python 3.x
•	Django 3.x o superior
•	﻿asgiref==3.8.1
•black==24.8.0
•click==8.1.7
•colorama==0.4.6
•Django==5.1
•mypy-extensions==1.0.0
•packaging==24.1
•pathspec==0.12.1
•platformdirs==4.2.2
•sqlparse==0.5.1
•tzdata==2024.1

Instalación
1.	Clona el repositorio:
bash
Copiar código
git clone https://github.com/ArmandoCota/ArticleCRUD/tree/main
2.	Navega al directorio del proyecto:
bash
Copiar código
cd tu_repositorio
3.	Crea un entorno virtual e instálalo:
bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
pip install -r requirements.txt
4.	Realiza las migraciones de la base de datos:
bash
Copiar código
python manage.py migrate
5.	Ejecuta el servidor de desarrollo:
bash
Copiar código
python manage.py runserver
6.	Accede a la aplicación:
Abre tu navegador web y ve a http://127.0.0.1:8000/ para ver la lista de artículos.
Estructura del Proyecto
•	models.py: Define el modelo Article con campos para el título, contenido y fecha de publicación.
•	forms.py: Contiene el formulario ArticleForm para la creación y actualización de artículos.
•	views.py: Implementa las vistas basadas en clases para listar, crear, actualizar, eliminar y ver artículos.
•	templates/: Contiene las plantillas HTML para las vistas.
o	article_list.html: Muestra una lista de artículos con paginación.
o	article_form.html: Formulario para la creación y actualización de artículos.
o	article_detail.html: Muestra los detalles de un artículo específico.
o	article_confirm_delete.html: Página de confirmación para eliminar un artículo.
•	urls.py: Configura las rutas URL para las vistas.
Vistas
•	ArticleListView: Muestra una lista paginada de artículos.
•	ArticleCreateView: Proporciona un formulario para crear un nuevo artículo.
•	ArticleUpdateView: Proporciona un formulario para actualizar un artículo existente.
•	ArticleDetailView: Muestra los detalles de un artículo.
•	ArticleDeleteView: Muestra una página de confirmación para eliminar un artículo.
Uso
•	Listar Artículos: Navega a http://127.0.0.1:8000/ para ver la lista de artículos.
•	Crear Artículo: Haz clic en "Create New Article" para acceder al formulario de creación.
•	Actualizar Artículo: Haz clic en "Edit" en la lista de artículos o en la página de detalles del artículo.
•	Eliminar Artículo: Haz clic en "Delete" en la lista de artículos o en la página de detalles del artículo.

