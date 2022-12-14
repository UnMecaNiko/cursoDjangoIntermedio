# Curso de Django Intermedio: Testing, Static Files, Django Admin | [platzi](https://platzi.com/cursos/django-intermedio/)
 
En este segundo curso de la saga de Django analizarás los conceptos fundamentales sobre el Testing. Mejorarás el administrador de Django con nuevos atributos, implementarás archivos estáticos en tu proyecto, y llegarás a la primera versión para presentar al público de la aplicación que trabajamos en la saga. Todo esto de la mano de tu profesor Facundo García Martoni.

- Conocer el significado y las ventajas de hacer tests.
- Escribir tus primeros tests en Django.
- Agregar archivos CSS e imágenes a tu proyecto.
- Personalizar el administrador de datos a tu gusto.

*Lo que verás a continuación son mis notas del curso 🚀 Si ves algún error o punto a mejorar no dudes en hacer tu aporte 💚*


**Este curso tiene como base el curso [DjangoBasico](https://github.com/UnMecaNiko/djangoBasico) donde se explica cómo se creó el proyecto ue trata sobre una app de votos**

## Testing

>TDD o Test-Driven Development (desarrollo dirigido por tests) es una práctica de programación que consiste en escribir primero las pruebas (generalmente unitarias), después escribir el código fuente que pase la prueba satisfactoriamente y, por último, refactorizar el código escrito.

### ¿Qué son los tests?

Los tests son funciones que nos ayudan a que nuestro código opere correctamente.

Generalmente se testean modelos o vistas

### ¿Por qué debería hacer tests?

Porque me permite evitar errores futuros a través de funciones que trabajan sobre las funciones principales de mi código.

- Nos permite ver errores que a simple vista no hubiéramos visto.
- Nos hace ver más profesionales.
- Permite trabajar en equipo.

### Primer test en nuestro proyecto

```bash
python3 manage.py shell
```
```py
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here
class QuestionModelTests(TestCase):

    def test_was_publish_recently_with_future_questions(self):
        """was_published_recently returns False for question whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(
            question_text="¿Quien es el mejor Couse Director de platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```
En la función del test definimos el código que se debe ejecutar para hacer la prueba, en este caso está comprendido en la sentencia `def`, para hacer la comprobación usamos el método `self.assertIs({tu resultado},{lo que esperas})`

Luego, corremos la prueba con `python3 manage.py test polls`













# Helpful Links

- [.gitignore](https://www.toptal.com/developers/gitignore)

- [Basic writing and formatting syntax](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

- [Django documentation](https://docs.djangoproject.com/en/3.2/)


