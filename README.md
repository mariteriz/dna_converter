# Conversor de ADN a ARN a proteína #

Este programa escrito en python3 convierte secuencias de ADN a ARN y de ARN a proteína a través de una interfaz CLI. 

Este programa se escribió como proyecto final del Bootcamp de Introducción a la Programación de Código Facilito en mayo 2022.

## Requisitos ##

Se requiere tener instalado **`python3`**. El programa se ejecuta en la **terminal**.

Se necesita un archivo de texto plano con la **secuencia de ADN o de ARN** que se quiere analizar. El repositorio incluye secuencias de prueba ubicadas en `secuencias_prueba/`.

## ¿Cómo ejecutar el programa? ##

1. Clonar el repositorio:
> `$ git clone ` \
> `$ cd dna_converter`
2. Ejecutar el archivo `main.py`:
> `/dna_converter $ python3 main.py`

## ¿Cómo se utiliza el programa? ##

Al ejecutar el `main.py` se desglosa un menú de opciones con las funcionalidades del programa. 

`1) Contar nucleotidos`\
`2) Transcribir ADN a ARN`\
`3) Traducir ARN a Proteína`\
\
`0) Salir`

### Funciones: ###
1. **Contar nucleótidos:** recibe una secuencia de ADN o ARN y regresa el número de nucleótidos. 
2. **Transcribir ADN a ARN:** recibe una secuencia de ADN y regresa la secuencia convertida a ARN.
3. **Traducir ARN a proteína:** recibe una secuencia de ARN y regresa la traducción a proteína. Para ejecutar esta opción se necesita una secuencia de ARN. Si no se cuenta con ella, se puede obtener a través de la opción 2.
