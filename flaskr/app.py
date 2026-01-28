from flaskr import create_app
from .modelos import db, Cancion, Medio, Album, Usuario
from .modelos import AlbumSchema,CancionSchema, UsuarioSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion, VistasSignIn, VistaLogIn, VistaAlbumsUsuario,VistaAlbum, VistaCancionesAlbum

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistasSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')


#PRUEBA

with app.app_context():
    c = Cancion(titulo="Prueba", minutos=2, segundos=20, interprete="Sultanito")
    c_schema = CancionSchema()
    db.session.add(c)
    db.session.commit()
    print([c_schema.dump(c) for c in Cancion.query.all()])
