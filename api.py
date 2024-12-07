from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid

from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones
#Funciones para hacer las consultas a la BD
import orm.repo as repo #El as repo es un alias 

#Creación del servidor
app = FastAPI()
#----------------------ALUMNOS---------------------------------#
#Alumno
#SELECT * FROM app.alumnos
#GET '/alumnos'
@app.get("/alumnos")
def lista_alumno(sesion:Session=Depends(generador_sesion)): 
    print("Api consultando todos los alumnos")
    return repo.lista_alumno(sesion)
#Alumno por id
#SELECT * FROM app.alumnos WHERE id={id_al}
#GET '/alumnos/{id}'
@app.get("/alumnos/{id}")
def alumno_por_id(id_alumno: int, sesion:Session=Depends(generador_sesion)): #Es obligatorio mandar el id
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id_alumno) #manda el objeto alumno pero lo convierte a .json

#----------------------FOTOS---------------------------------#
#Fotos
#SELECT * FROM app.fotos
#GET '/fotos'
@app.get("/fotos")
def lista_foto(sesion:Session=Depends(generador_sesion)): 
    print("Api consultando todas las fotos")
    return repo.lista_foto(sesion)
#Foto por id
#SELECT * FROM app.fotos WHERE id={id_foto}
#GET '/fotos/{id}'
@app.get("/fotos/{id}")
def foto_por_id(id: int, sesion:Session=Depends(generador_sesion)): 
    print("Api consultando foto por id")
    return repo.foto_por_id(sesion, id) 

#----------------------CALIFICACIONES---------------------------------#
#Calificaciones
#SELECT * FROM app.calificaciones
#GET '/calificaciones'
@app.get("/calificaciones")
def lista_calificacion(sesion:Session=Depends(generador_sesion)): 
    print("Api consultando todas las calificaciones")
    return repo.lista_calificacion(sesion)
#Calificacion por id
#SELECT * FROM app.calificaciones WHERE id={id_calificacion}
#para atender GET '/calificaciones/{id}'
@app.get("/calificaciones/{id}")
def calificacion_por_id(id: int, sesion:Session=Depends(generador_sesion)): 
    print("Api consultando calificacion por id")
    return repo.calificacion_por_id(sesion, id) 

#----------------------OTROS---------------------------------#
#Buscar fotos por id alumno
#SELECT * FROM app.fotos WHERE id_alumno={id_alumno}
#GET '/alumnos/{id}/fotos'
@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos del alumno", id)
    return repo.fotos_por_id_alumno(sesion,id)
#Buscar calificaciones por id foto
#SELECT * FROM app.calificaciones WHERE id={id_foto}
#GET '/fotos/{id}/calificaciones'
@app.get("/fotos/{id}/calificaciones")
def calificaciones_por_id_foto(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por id_foto", id)
    return repo.calificaciones_por_id_foto(sesion,id)
#Buscar calificaciones por id alumno
#SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
#GET '/alumnos/{id}/calificaciones'
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por id_alumno", id)
    return repo.calificaciones_por_id_alumno(sesion,id)

#----------------------DELETE---------------------------------#
#Borrar alumno por id alumno
#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
#DELETE '/alumnos/{id}/alumnos'
@app.delete("/alumnos/{id}")
def borrar_usuario(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_alumno_por_id_alumno(sesion,id)   
    return {"alumno_borrado", "ok"}
#Borrar calificacion por id alumno
#DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
#DELETE '/alumnos/{id}/calificaciones'
@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificacion_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificcion_por_id_alumno(sesion,id)
    return {"calificacion_borrada", "ok"}
#Borrar foto por id alumno
#DELETE FROM app.fotos WHERE id_alumnos={id_al}
#DELETE '/alumnos/{id}/fotos'
@app.delete("/alumnos/{id}/fotos")
def borrar_foto_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_foto_por_id_alumno(sesion,id)
    return {"foto_borrada", "ok"}
#Borrar fotos por id fotos
#DELETE FROM app.fotos WHERE id_fotos={id_fo}
#DELETE '/fotos/{id}/fotos'
@app.delete("/fotos/{id}")
def borrar_foto(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_foto_por_id_foto(sesion,id)   
    return {"foto_borrada", "ok"}
#Borrar calificaciones por id calificaciones
#DELETE FROM app.calificaciones WHERE id_calificaciones={id_cal}
#DELETE '/calificaciones/{id}/calificaciones'
@app.delete("/calificaciones/{id}")
def borrar_calificacion(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificacion_por_id_calificacion(sesion,id)   
    return {"calificacion_borrada", "ok"}