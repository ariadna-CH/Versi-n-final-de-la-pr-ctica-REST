import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_
<<<<<<< HEAD
import orm.esquemas as esquemas 
=======
>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8

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
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first() #se devuelve un objeto de tipo usalumno
<<<<<<< HEAD
#----------------------RES-2-----------------------------#
#POST '/alumnos'
#Insertar alumno
def insertar_alumno(sesion:Session, alumno_nuevo:esquemas.AlumnoBase):
    #1. Crear un nuevo objeto de la clase modelo alumno
    alumno_bd = modelos.Alumno()
    #2. Llenar los parámetros del nuuevo objeto con los parámetros que nos pasó el usuario
    alumno_bd.nombre = alumno_nuevo.nombre
    alumno_bd.edad = alumno_nuevo.edad
    alumno_bd.domicilio = alumno_nuevo.domicilio
    alumno_bd.carrera = alumno_nuevo.carrera
    alumno_bd.trimestre = alumno_nuevo.trimestre
    alumno_bd.email = alumno_nuevo.email
    alumno_bd.password = alumno_nuevo.password
    #3. Insertar el nuevo objeto a la BD
    sesion.add(alumno_bd)
    #4. Confirmamos el cambio
    sesion.commit()
    #5. Hacemos un refresh
    sesion.refresh(alumno_bd)
    return alumno_bd

#PUT '/alumnos/{id}'
#Actualizar datos de un alumno
def actualiza_alumno(sesion:Session, id_alumno:int,alumno_actualizado:esquemas.AlumnoBase):
    #1. Verfificar si el alumno existe
    alumno_bd = alumno_por_id(sesion,id_alumno)
    if alumno_bd is not None:
        #2. Actualizamos los datos del alumno en la base de datos
        alumno_bd.nombre = alumno_actualizado.nombre
        alumno_bd.edad = alumno_actualizado.edad
        alumno_bd.domicilio = alumno_actualizado.domicilio
        alumno_bd.carrera = alumno_actualizado.carrera
        alumno_bd.trimestre = alumno_actualizado.trimestre
        alumno_bd.email = alumno_actualizado.email
        alumno_bd.password = alumno_actualizado.password
        #3. Confirmamos los cambios
        sesion.commit()
        #4. Reflescar la base de datos
        sesion.refresh(alumno_bd)
        #5. Imprimir los datos nuevos
        print(alumno_actualizado)
        return(alumno_actualizado)
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
    
=======

>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8
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

<<<<<<< HEAD
#----------------------RES-2-----------------------------#
#PUT '/fotos/{id}'
#Actualizar datos de fotos
def actualiza_foto(sesion:Session, id_foto:int,foto_actualizada:esquemas.FotoBase):
    #1. Verfificar si foto existe
    foto_bd = foto_por_id(sesion,id_foto)
    if foto_bd is not None:
        #2. Actualizamos los datos del la foto en la base de datos
        foto_bd.titulo = foto_actualizada.titulo
        foto_bd.descripcion = foto_actualizada.descripcion
        foto_bd.ruta = foto_actualizada.ruta
        #3. Confirmamos los cambios
        sesion.commit()
        #4. Reflescar la base de datos
        sesion.refresh(foto_bd)
        #5. Imprimir los datos nuevos
        print(foto_actualizada)
        return(foto_actualizada)
    else:
        respuesta = {"mensaje":"No existe la foto"}
        return respuesta
    
=======
>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8
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

<<<<<<< HEAD
#----------------------RES-2-----------------------------#
#PUT '/calificaciones/{id}'
#Actualizar datos de calificaciones
def actualiza_calificacion(sesion:Session, id_calificacion:int,calificacion_actualizada:esquemas.CalificacionBase):
    #1. Verfificar si calificacion existe
    calificacion_bd = calificacion_por_id(sesion,id_calificacion)
    if calificacion_bd is not None:
        #2. Actualizamos los datos del la calificacion en la base de datos
        calificacion_bd.uea = calificacion_actualizada.uea
        calificacion_bd.calificacion = calificacion_actualizada.calificación
        #3. Confirmamos los cambios
        sesion.commit()
        #4. Reflescar la base de datos
        sesion.refresh(calificacion_bd)
        #5. Imprimir los datos nuevos
        print(calificacion_actualizada)
        return(calificacion_actualizada)
    else:
        respuesta = {"mensaje":"No existe la calificacion"}
        return respuesta
=======
>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8
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
<<<<<<< HEAD
#----------------------RES-2-----------------------------#
#POST("/alumnos/{id}/calificaciones")
#Insertar una nueva calificacion al alumno existente
def insertar_cal_alumno(sesion:Session, id_alumno:int, cal_por_alumno:esquemas.CalificacionBase):
    #1. Crear un nuevo objeto de la clase modelo calificacion
    cal_alumno_bd = modelos.Calificacion()
    #2. Llenar los parámetros del nuevo objeto con los parámetros que nos pasó el usuario
    cal_alumno_bd.id_alumno = id_alumno
    cal_alumno_bd.uea = cal_por_alumno.uea
    cal_alumno_bd.calificacion = cal_por_alumno.calificación
    #3. Insertar el nuevo objeto a la BD
    sesion.add(cal_alumno_bd)
    #4. Confirmamos el cambio
    sesion.commit()
    #5. Hacemos un refresh
    sesion.refresh(cal_alumno_bd)
    return cal_alumno_bd

#POST("/alumnos/{id}/fotos")
#Insertar una nueva foto al alumno existente
def insertar_foto_alumno(sesion:Session, id_alumno:int, foto_por_alumno:esquemas.FotoBase):
    #1. Crear un nuevo objeto de la clase modelo foto
    foto_alumno_bd = modelos.Foto()
    #2. Llenar los parámetros del nuevo objeto con los parámetros que nos pasó el usuario
    foto_alumno_bd.id_alumno = id_alumno
    foto_alumno_bd.titulo = foto_por_alumno.titulo
    foto_alumno_bd.descripcion = foto_por_alumno.descripcion
    foto_alumno_bd.ruta = foto_por_alumno.ruta
    #3. Insertar el nuevo objeto a la BD
    sesion.add(foto_alumno_bd)
    #4. Confirmamos el cambio
    sesion.commit()
    #5. Hacemos un refresh
    sesion.refresh(foto_alumno_bd)
    return foto_alumno_bd
=======
>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8

#----------------------DELETE-----------------------------#
#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
#DELETE '/alumnos/{id}/alumnos'
def borrar_alumno_por_id_alumno(sesion:Session, id_alumno:int):
<<<<<<< HEAD
    print("DELETE FROM app.alumnos WHERE id_alumnos= ",id)
=======
    print("DELETE FROM app.alumnos WHERE id_alumnos= ",id_alumno)
>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8
    #1. Primero hacemos un SELECT para ver si existe el id alumno lo que deviuelve se guarda en una variable para saber si existe 
    alumnos_alum = alumno_por_id(sesion, id_alumno) #Devuelve una lista de objetos
    #2. Borramos
    if alumnos_alum is not None:
<<<<<<< HEAD
        sesion.delete(alumnos_alum)
    sesion.commit()
    respuesta = {
        "mensaje": "alumno eliminado"
    }
=======
        for alumno_alumno in alumnos_alum: 
            sesion.delete(alumno_alumno)
    sesion.commit()
>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8
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
<<<<<<< HEAD
    sesion.commit()

=======
    sesion.commit()
>>>>>>> 0f9377d59a515054e9bb80f4c90ee35d849a8fe8
