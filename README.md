## Proyecto

El archivo records controla los registros a realizar
El archivo objects controla los objetos controlados


MODELS

-METAEQUIPOS
* marca
* modelo
* serie
* fecha de adquisicion
* fecha ultimo retiro 

-EQUIPO: METAEQUIPOS
* marca
* modelo
* serie
* id
* estatus
* is interno (bool)

    - AREA asignada
    - AREA DE USO ACTUAL
    * descripción
    * atenciones (autoincremental)

    - REPORTE
    * fecha
    * hora
    * descripción : mantenimiento preventivo / correctivo
    * area
    * estatus inicial
    * estatus final
    * evaluación (equipo, uso, otro)
    * count : numero de veces arrendado

        -BITACORA
        * fecha
        * hora
        * reporta 
        * atiende
        * count : numero de veces arrendado

else (is_interno)

- PROVEEDOR
* nombre
* numero
* correo

* EQUIPOS: METAEQUIPOS
    * marca
    * modelo
    * serie
    * count : numero de veces arrendado