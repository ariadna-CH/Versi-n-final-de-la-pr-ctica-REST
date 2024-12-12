from pydantic import BaseModel
class AlumnoBase(BaseModel): #Aqui no aparece el id ni la fecha de registro porque no quiero que el usuario lo modifique
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

class CalificacionBase(BaseModel):
    uea:str
    calificación:str

class FotoBase(BaseModel):
    titulo:str
    descripcion:str
    ruta:str 

