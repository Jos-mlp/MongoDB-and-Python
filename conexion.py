import pymongo

def ObtenerConexion():
    MONGO_HOST="localhost"
    MONGO_PUERTO="27017"
    MONGO_TIEMPO_FUERA=1000

    MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

    MONGO_BASEDATOS="escuela"
    MONGO_COLECCION="alumnos"
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    return coleccion
