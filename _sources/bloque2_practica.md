
Práctica. Lectura y documentación del código de un extractor de entidades
=========================================================================

[ Acceso rápido a la carpeta con el [código fuente][ner] ]

En esta práctica leerás el código de un programa escrito por otros y lo documentarás para demostrar que entiendes lo que hace. La documentación resultante es por lo que se te evaluará. La práctica se ha de realizar en parejas.

Desde diversos frentes se [defiende][defiende] la lectura de código escrito por otros como un enfoque adecuado para aprender a programar o mejorar las habilidades como programador. La metodología [PRIMM][primm], por ejemplo, incentiva la discusión entre los estudiantes sobre cómo funciona un determinado programa y usa código ya existente  para integrar la lectura de código como una etapa anterior a la escritura. 

Esta asignatura incluye algunas prácticas en las que utilizarás modelos preentrenados para ciertas tareas de procesamiento del lenguaje natural, pero tanto la programación de los modelos subyacentes como el procesamiento de los datos quedarán normalmente ocultos tras la interfaz de los programas correspondientes. Partiendo de la premisa de que entender cómo funcionan las cosas ayuda a sacarles provecho y dado que la asignatura no incluye entre sus objetivos la escritura desde cero de un programa completo, esta práctica propone un acercamiento intermedio al estudiar el código escrito por terceros como preparación necesaria para poder más adelante crear tus propios programas o modificar los existentes. Tener que modificar código es una tarea más frecuente de lo que en principio se puede pensar: en el desarrollo de la profesión de científico de datos te encontrarás en situaciones en las que no existe un modelo que resuelva exactamente tu problema y deberás plantearte modificar el funcionamiento de un sistema base.

[defiende]: https://www.stevejgordon.co.uk/become-a-better-developer-by-reading-source-code
[primm]: https://blog.teachcomputing.org/using-primm-to-structure-programming-lessons/

Algunos estudios asemejan la labor de leer código a la de leer un texto escrito en lenguaje natural; otros lo equiparan más bien al procesamiento mental de ecuaciones matemáticas; otros [estudios][estudios] sugieren que el cerebro usa mecanismo distintos para la asimilación del código fuente.

[estudios]: https://www.sciencedaily.com/releases/2020/12/201215131236.htm


## Objetivo

En esta práctica vas a estudiar un programa que permite entrenar y probar un sistema neuronal de reconocimiento de entidades nombradas. El programa se compone de varios módulos escritos en Python, algunos de los cuales usan la librería Pytorch para la programación del modelo neuronal. El código está en [esta carpeta][ner] del repositorio de la asignatura, que tendrás que clonar. A efectos de reconocimiento de la autoría, el código está tomado del que utilizan como inspiración para sus proyectos los estudiantes del curso Deep Learning ([CS230][cs230]) de la Universidad de Stanford.

[cs230]: https://github.com/cs230-stanford/cs230-code-examples/
[ner]: https://github.com/jaspock/mtextos2122/blob/main/code/ner/

El código original tiene algunos comentarios que puedes consultar en el repositorio del curso CS230 y que han sido eliminados en la versión de este curso; estos comentarios originales son relativamente generales. En esta práctica tienes que añadir muchos más comentarios para explicar con cierto nivel de detalle qué hacen las principales líneas del código. 

Para hacerte una idea de cómo funciona el reconocedor de entidades nombradas, ejecuta en primer lugar el programa tal y como se explica en el README saltando la parte opcional que descarga datos de Kaggle. Puedes leer también esta [guía][guía] sobre el uso y propósito del programa.

[guía]: https://cs230.stanford.edu/blog/tips/

## Comentarios en Python

Los comentarios en Python pueden ser de [dos tipos][tipos]: comentarios de tipo *docstring* (que pueden aparecer en cualquier lugar del código, aunque suelen colocarse justo después de la definición de una clase o una función para documentarlas) y comentarios de una línea. Los primeros aparecen rodeados por una secuencia de tres comillas al principio y al final, y pueden ocupar más de una línea; los segundos se extienden desde el carácter de la almohadilla hasta el final de la línea. Dado que el propósito de esta práctica es escribir una documentación elaborada, es recomendable que uses más los comentarios de tipo *docstring*, aunque no para documentar únicamente clases o funciones, sino líneas concretas.

[tipos]: https://realpython.com/documenting-python-code/

## Uso de Pycco para generar la documentación

En lugar de entregar el código fuente documentado, vas a generar una vista en HTML de los comentarios y el código que facilita su lectura. Para ello, vas a usar la herramienta [Pycco][pycco]. Para aprender sobre su funcionamiento basta con estudiar un pequeño [tutorial][tutorial]. Estudia también uno de los ficheros del código fuente de Pycco (que se usa a sí mismo para generar su documentación) como, por ejemplo, [main.py][pyccomain], y observa después como se muestran sus comentarios en la [página web generada][pyccoejemplo]. Como ves, se puede utilizar *markdown* para dar un formato sencillo al texto de los comentarios.

Para generar en la carpeta *docs* la documentación en HTML del código del detector de entidades nombradas:

```{code-block} python
  pip install pycco
  pycco --generate-index *.py model/*.py
```

[pycco]: https://github.com/pycco-docs/pycco
[pyccomain]: https://github.com/pycco-docs/pycco/blob/master/pycco/main.py
[pyccoejemplo]: https://pycco-docs.github.io/pycco/
[tutorial]: https://realpython.com/generating-code-documentation-with-pycco/


Puedes estudiar el fichero `build_vocab.py` que contiene algunos ejemplos de comentarios.

```{admonition} Nota
:class: note
Algunas versiones de Pycco pueden provocar un error en Windows al intentar generar la documentación. Si es tu caso, puedes aplicar este [parche][parche] al código fuente de Pycco para arreglarlo.
```

[parche]: https://github.com/pycco-docs/pycco/issues/109


## Orden sugerido para el estudio del código

La {numref}`tab-ficheros` muestra el orden aproximado en que se recomienda ir documentando el código. Es posible que en ocasiones tengas que consultar parte de los ficheros de filas inferiores debido a las dependencias. En general, es recomendable que realices un primer repaso general sobre el código antes de ponerte a documentarlo. No hay que documentar los ficheros `search_hyperparams.py`, `synthesize_results.py` y `build_kaggle_dataset.py`.

<p></p>

```{list-table} Ficheros a documentar y orden recomendado.
:header-rows: 1
:name: tab-ficheros

* - Fichero
  - Dependencias
  - Semana
  - Clases o funciones
* - `build_vocab.py`
  - 
  - S1
  - save_vocab_to_text_file, save_dict_to_json, update_vocab
* - `utils.py`
  - 
  - S1
  - Params, RunningAverage, set_logger, save_dict_to_json, save_checkpoint, load_checkpoint
* - `model/net.py`
  - 
  - S2
  - Net, accuracy, loss_fn
* - `evaluate.py`
  - utils, model.net, model.data_loader
  - S3
  - evaluate
* - `model/data_loader.py`
  - utils
  - S4
  - DataLoader
* - `train.py`
  - model.net, model.data_loader, utils
  - S4
  - train, train_and_evaluate
```

## Entrega

La fecha límite para entregar la práctica es el 5 de abril de 2022 a las 23.59 horas. Entrega a través del [servidor de prácticas][servidor] del Departamento un fichero zip de nombre `mtextos-ner-21-22.zip` que contenga directamente en la carpeta raíz el código fuente (incluida la carpeta `model`) con la estructura original que permita ejecutarlo, así como la carpeta `docs` generada por Pycco; no incluyas en el zip las carpetas `data` y `experiments`, ya que pueden ocupar demasiado espacio si has probado el código con datos de cierto tamaño.

En el momento de realizar la entrega indica los datos de tu pareja. Solo uno de los dos miembros de la pareja ha de realizar la entrega.

[servidor]: https://pracdlsi.dlsi.ua.es/index.cgi
