#Esta clase base de las clases modelo las hereda
#Los modelos o clases modelo son las clases que se mapean a las tablas
from orm.config import BaseClass
#Importar de SQLALchemy los tipos de datos que usan las columnas de las tablas
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
#PAra calcular la hora actual 
import datetime

#Por convención las clases tienen nombres en singular y comienzan con mayusculas
class Alumno(BaseClass): #la clase Alumno se extiende de BaseClass
    __tablename__="alumnos" #Nombre de la tabla en la BD
    id=Column(Integer, primary_key=True) #tipo de dato y es llave primaria
    nombre=Column(String(100)) #tipo de dato y tamaño
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column("email",String(100)) #se coloca el "email" para que lo distinga pero no es obligatorio
    password=Column(String(40))
    fecha_registro=Column(DateTime(timezone=True),default=datetime.datetime.now) #Cuando ponemos (timezone=True) y con default=datetime toma la hora actual


class Calificacion(BaseClass):
    __tablename__="calificaciones"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    uea=Column(String(100))
    calificacion=Column(String(100))


class Foto(BaseClass):
    __tablename__="fotos"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(50)) 