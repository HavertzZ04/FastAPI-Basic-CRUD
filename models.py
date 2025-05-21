'''
En tu caso, ¿para qué sirve (o no) models.py?
Como ahora usas solo un diccionario en memoria (sin base de datos), no necesitas un archivo models.py.

Todo está en schemas.py (modelos de validación) y crud.py (lógica de acceso/modificación del diccionario).

Cuando decidas conectar MongoDB o cualquier otra base, ahí sí crearás un models.py para definir las colecciones o tablas usando la librería correspondiente (como ODMantic, Motor o SQLAlchemy).
'''
