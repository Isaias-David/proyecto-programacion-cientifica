# Análisis de Datos — Población Atendida Hospital General

## Leer y explorar el dataset utilizando Python.
* Analizar y limpiar los datos.
* Encontrar patrones, tendencias o recurrencias interesantes.
* Crear gráficos que permitan visualizar los resultados.
* Presentar brevemente los principales hallazgos y conclusiones

# 1. Definición del Problema, Objetivos y Alcance
**Problema:** 
La idea de esta activida es saber cual es el sexo que mas consulta en los diferentes servicios del Hospital General de Medellin.

* **Objetivos:** 
  * Leer,Normalizar, limpiar y parsear el dataset `poblacion_atendida_hospital_general.csv`
  * Identificar patrones en función del género, edad, servicio y departamento de procedencia

* **Alcance:** 
Analizar los datos desde el 2023 hasta el 2025

## 2. Dataset Seleccionado
* **Fuente:**
 Datos de población atendida en el Hospital General descargada de Medata del departamento se Secretaria se salud
* **Registros:** 
182,700 filas y 12 columnas según la lectura
* **Variables analizadas:**
 `servicio`, `sexo`, `edad`, `rango_edad`, `Departamento`, `regimen`, `fecha_atencion`.

## 3. Hallazgos y Conclusiones
1. **Cual es el servici y genero que mas se atiende en el hosptal General?:**
 La atención ambulatoria tiene el mayor registro de consultas. La población femenina presenta un mayor volumen de atención frente a la masculina en ambos servicios.

2. **Cual es el rango de edad que mas consulta en el Hospital General?:** 
Hay dos rangos de edades, los niños y la población de la tercera edad.

3. **Cuales son los departamentos que mas atiende el Hospital General:** Aunque Antioquia representa el principal origen de pacientes, tambien se registra pacientes provenientes de Chocó y Córdoba.