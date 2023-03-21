
(label_tecnicas)=
Técnicas para la minería de textos
==================================

En este bloque se aborda el estudio de algunos modelos neuronales utilizados para procesar textos. El profesor de este bloque es Juan Antonio Pérez Ortiz. El bloque comienza con un repaso del funcionamiento del regresor logístico, que nos servirá para asentar los conocimientos necesarios para entender posteriores modelos. A continuación se estudia con cierto nivel de detalle *skip-grams*, uno de los algoritmos para la obtención de *embeddings* incontextuales de palabras. Después se repasa el funcionamiento de las arquitecturas neuronales *feedforward* y se estudia su aplicación a modelos de lengua. El objetivo último es abordar el estudio de la arquitectura más importante de los sistemas actuales de procesamiento de textos: el transformer. Una vez estudiadas estas arquitecturas, finalizaremos con un análisis del funcionamiento de los modelos preentrenados.

Los materiales de clase complementan la lectura de algunos capítulos de un libro de texto ("Speech and Language Processing" de Dan Jurafsky y James H. Martin, borrador de la tercera edición, disponible online) con anotaciones realizadas por el profesor.

## Primera sesión (29 de marzo de 2023)

#### Contenidos a preparar antes de la sesión del 29/03/2023

Las actividades a realizar antes de esta clase son:

- Lectura y estudio de los contenidos de [esta página](https://jaspock.github.io/me/materials/transformers/regresor) sobre regresión logística. Puedes saltar por ahora el apartado de [implementación en PyTorch](https://jaspock.github.io/me/materials/transformers/regresor#regresores-implementados-en-pytorch), ya que será el eje central de la clase presencial. Como verás, la página te indica qué contenidos has de leer del libro. Tras una primera lectura, lee las anotaciones del profesor, cuyo propósito es ayudarte a entender los conceptos clave del capítulo. Después, realiza una segunda lectura del capítulo del libro. En total, esta parte debería llevarte unas 3 horas 🕒️ de trabajo.
- Visionado y estudio de los tutoriales en vídeo de esta [playlist oficial de PyTorch](https://www.youtube.com/playlist?list=PL_lsbAsL_o2CTlGHgMxNrKhzP97BaG9ZN).  Estudia al menos los 4 primeros vídeos (“Introduction to PyTorch”, “Introduction to PyTorch Tensors”, “The Fundamentals of Autograd” y “Building Models with PyTorch”). En total, esta parte debería llevarte unas 2 horas 🕒️ de trabajo.
- Tras acabar con las dos partes anteriores, realiza este [test de evaluación](https://forms.gle/E1xzZHw6hzMWJaNr7) de estos contenidos. Son pocas preguntas y te llevará unos minutos.

#### Contenidos para la sesión presencial del 29/03/2023

En la clase presencial, repasaremos los contenidos de la semana anterior y veremos cómo se implementa el regresor logístico en PyTorch siguiendo la implementación de un regresor logístico binario y de uno multinomial que se comentan en [este apartado]((https://jaspock.github.io/me/materials/transformers/regresor#regresores-implementados-en-pytorch)).

La idea es que vayas creando una serie de notebooks en Google Colab en los que incluyas y comentes cada uno de los programas que vamos a ir viendo. En la última clase se presentará una práctica más avanzada que implicará modificar el código del transformer.

## Segunda sesión (26 de abril de 2023)

Entre la sesión anterior y la del 26 de abril transcurren varias semanas de trabajo, por lo que la carga de trabajo es mayor que en la sesión anterior.

Nota: los contenidos de este apartado son provisionales.

#### Contenidos a preparar antes de la sesión del 26/04/2023

Las actividades a realizar antes de esta clase son:

- Lectura y estudio de [esta página](https://jaspock.github.io/me/materials/transformers/embeddings) sobre la obtención de embeddings incontextuales. Puedes saltar de nuevo el apartado de [implementación en PyTorch](https://jaspock.github.io/me/materials/transformers/embeddings#implementación-en-pytorch), ya que se estudiará en la próxima clase presencial. Como verás, la página te indica qué contenidos has de leer del libro. Tras una primera lectura, lee las anotaciones del profesor, cuyo objetivo es ayudarte a entender los conceptos clave del capítulo. Después, realiza una segunda lectura del capítulo. En total, esta parte debería llevarte unas 4 horas 🕒️ de trabajo.
- Lectura y estudio de [esta página](https://jaspock.github.io/me/materials/transformers/ffw) sobre la obtención de embeddings incontextuales. Puedes saltar de nuevo el apartado de [implementación en PyTorch](https://jaspock.github.io/me/materials/transformers/ffw#implementación-en-pytorch), ya que se estudiará también en la próxima clase presencial. En total, esta parte debería llevarte unas 3 horas 🕒️ de trabajo.
- Primeros pasos en el estudio del modelo transformer. Volveremos a dedicar más horas a esta arquitectura para la próxima sesión para abordarla en dos fases. Ahora, lee con detenimiento la introducción a mecanismos de atención de ["Visualizing A Neural Machine Translation Model"](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/), así como la introducción visual a los transformers de ["The Illustrated Transformer"](http://jalammar.github.io/illustrated-transformer/). A continuación, realiza una lectura no muy pausada del apartado 9.7 (solo este apartado) del capítulo ["Deep learning architectures for sequence processing"](https://web.archive.org/web/20221216193204/https://web.stanford.edu/~jurafsky/slp3/9.pdf). En total, esta parte debería llevarte unas 4 horas 🕒️ de trabajo. Volveremos a este capítulo para la próxima sesión. 
- Realización del [test de evaluación]() de estos contenidos. Son pocas preguntas y te llevará unos minutos.

#### Contenidos para la sesión presencial del 26/04/2023


## Tercera sesión (10 de mayo de 2023)

#### Contenidos a preparar antes de la sesión del 10 de mayo
