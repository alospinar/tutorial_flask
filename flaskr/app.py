from flaskr import create_app
from .modelos import db, Cancion, Medio, Album, Usuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#PRUEBA

with app.app_context():
    u=Usuario(nombre='admin',contrasena='12345')
    a=Album(titulo='Album1',anio=2020, descripcion='texto',medio=Medio.CD)
    c=Cancion(titulo='mi cancion', minutos=2,segundos=23,interprete='yo')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())