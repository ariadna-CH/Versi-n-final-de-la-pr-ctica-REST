import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_


#----------------------PETICIONES ALUMNOS-----------------------------#
#SELECT * FROM app.alumnos
#GET '/alumnos'
def lista_alumno(sesion:Session): #Mediante la Session se pueden hacer consultas
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()#Que tabla quiero utilizar y se devuelve un objeto de tipo alumno pero devuelve toda la lista alumnos
#SELECT * FROM app.alumnos WHERE id={id_al}
#GET '/alumnos/{id}'
def alumno_por_id(sesion:Session,id_alumno:int): #Mediante la Session se pueden hacer consultas
    print("SELECT * FROM app.alumnos WHERE id=", id_alumno)
    #Que tabla quiero utilizar, y se aplica un filtro ya que solo quiero que me muestre uno y que sea por id
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first() #se devuelve un objeto de tipo alumno
    
#----------------------PETICIONES FOTO-----------------------------#
#SELECT * FROM app.fotos
#GET '/fotos'
def lista_foto(sesion:Session): 
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()
#SELECT * FROM app.fotos WHERE id={id_foto}
#GET '/fotos/{id}'
def foto_por_id(sesion:Session,id_foto:int):
    print("SELECT * FROM app.fotos WHERE id=", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first() 


#----------------------PETICIONES CALIFICACIONES-----------------------------#
#SELECT * FROM app.calificaciones
#GET '/calificaciones'
def lista_calificacion(sesion:Session): 
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()
#SELECT * FROM app.calificaciones WHERE id={id_calificacion}
#para atender GET '/calificaciones/{id}'
def calificacion_por_id(sesion:Session,id_calificacion:int):
    print("SELECT * FROM app.calificaciones WHERE id=", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first() 


#----------------------PETICIONES OTROS-----------------------------#
#SELECT * FROM app.fotos WHERE id_alumno={id_al}
#GET '/alumnos/{id}/fotos'
def fotos_por_id_alumno(sesion:Session, id_alumno:int):
    print("SELECT * FROM app.fotos WHERE id_alumno= ",id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all()
#SELECT * FROM app.calificaciones WHERE id={id_foto}
#GET '/fotos/{id}/calificaciones'
def calificaciones_por_id_foto(sesion:Session, id_foto:int):
    print("SELECT * FROM app.calificaciones WHERE id= ",id_foto)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_foto).all()
#SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
#GET '/alumnos/{id}/calificaciones'
def calificaciones_por_id_alumno(sesion:Session, id_alumno:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos= ",id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_alumno).all()


#----------------------DELETE-----------------------------#
#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
#DELETE '/alumnos/{id}/alumnos'
def borrar_alumno_por_id_alumno(sesion:Session, id_alumno:int):
    print("DELETE FROM app.alumnos WHERE id_alumnos= ",id)
    print("DELETE FROM app.alumnos WHERE id_alumnos= ",id_alumno)
    #1. Primero hacemos un SELECT para ver si existe el id alumno lo que deviuelve se guarda en una variable para saber si existe 
    alumnos_alum = alumno_por_id(sesion, id_alumno) #Devuelve una lista de objetos
    #2. Borramos
    if alumnos_alum is not None:
        sesion.delete(alumnos_alum)
    sesion.commit()
    respuesta = {
        "mensaje": "alumno eliminado"
    }
    for alumno_alumno in alumnos_alum: 
        sesion.delete(alumno_alumno)
    sesion.commit()

#DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
#DELETE '/alumnos/{id}/calificaciones'
def borrar_calificcion_por_id_alumno(sesion:Session, id_alumno:int):
    print("DELETE FROM app.calificaciones WHERE id_alumnos= ",id_alumno)
    #1. Primero hacemos un SELECT para ver si existe el id alumno lo que deviuelve se guarda en una variable para saber si existe 
    calificaciones_alum = calificaciones_por_id_alumno(sesion, id_alumno) #Devuelve una lista de objetos
    #2. Borramos
    if calificaciones_alum is not None:
        for calificacion_alumno in calificaciones_alum: 
            sesion.delete(calificacion_alumno)
    sesion.commit()
#DELETE FROM app.fotos WHERE id_alumnos={id_al}
#DELETE '/alumnos/{id}/fotos'
def borrar_foto_por_id_alumno(sesion:Session, id_alumno:int):
    print("DELETE FROM app.fotos WHERE id_alumnos= ",id_alumno)
    #1. Primero hacemos un SELECT para ver si existe el id alumno lo que deviuelve se guarda en una variable para saber si existe 
    fotos_alum = fotos_por_id_alumno(sesion, id_alumno) #Devuelve una lista de objetos
    #2. Borramos
    if fotos_alum is not None:
        for foto_alumno in fotos_alum: 
            sesion.delete(foto_alumno)
    sesion.commit()
#DELETE FROM app.fotos WHERE id_fotos={id_fo}
#DELETE '/fotos/{id}/fotos'
def borrar_foto_por_id_foto(sesion:Session, id_foto:int):
    print("DELETE FROM app.fotos WHERE id_fotos= ",id_foto)
    #1. Primero hacemos un SELECT para ver si existe el id foto lo que deviuelve se guarda en una variable para saber si existe 
    fotos_foto = foto_por_id(sesion, id_foto) #Devuelve una lista de objetos
    #2. Borramos
    if fotos_foto is not None:
        for foto_foto in fotos_foto: 
            sesion.delete(foto_foto)
    sesion.commit()
#DELETE FROM app.calificaciones WHERE id_calificaciones={id_cal}
#DELETE '/calificaciones/{id}/calificaciones'
def borrar_calificacion_por_id_calificacion(sesion:Session, id_calificacion:int):
    print("DELETE FROM app.calificaciones WHERE id_calificaciones= ",id_calificacion)
    #1. Primero hacemos un SELECT para ver si existe el id calificaciones lo que deviuelve se guarda en una variable para saber si existe 
    calificaciones_cal = calificacion_por_id(sesion, id_calificacion) #Devuelve una lista de objetos
    #2. Borramos
    if calificaciones_cal is not None:
        for calificacion_cal in calificaciones_cal: 
            sesion.delete(calificacion_cal)
    sesion.commit()
