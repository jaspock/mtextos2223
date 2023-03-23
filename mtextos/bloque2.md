
(label_tecnicas)=
Técnicas para la minería de textos
==================================

En este bloque se aborda el estudio de algunos modelos neuronales utilizados para procesar textos. El profesor de este bloque es Juan Antonio Pérez Ortiz. El bloque comienza con un repaso del funcionamiento del regresor logístico, que nos servirá para asentar los conocimientos necesarios para entender posteriores modelos. A continuación se estudia con cierto nivel de detalle *skip-grams*, uno de los algoritmos para la obtención de *embeddings* incontextuales de palabras. Después se repasa el funcionamiento de las arquitecturas neuronales *feedforward* y se estudia su aplicación a modelos de lengua. El objetivo último es abordar el estudio de la arquitectura más importante de los sistemas actuales de procesamiento de textos: el transformer. Una vez estudiadas estas arquitecturas, finalizaremos con un análisis del funcionamiento de los modelos preentrenados.

Los materiales de clase complementan la lectura de algunos capítulos de un libro de texto ("Speech and Language Processing" de Dan Jurafsky y James H. Martin, borrador de la tercera edición, disponible online) con anotaciones realizadas por el profesor.

## Práctica a entregar para este bloque

Durante las sesiones de este bloque, estudiaremos diferentes implementaciones en PyTorch de modelos neuronales para procesar textos. Para cada ejemplo de código, excepto el último, has de entregar un notebook con el código original y bloques de texto con tus comentarios explicando el código en base a lo que has aprendido sobre el tema y sobre PyTorch. Entrega todos los notebooks en forma de enlaces de Google Colab a través de una tutoría de UACloud. Crea los cuadernos de Google Colab con tu cuenta de `gcloud.ua.es` y compártelos con la cuenta del profesor que te indicará en clase. Para el último bloque de código (implementación del transformer), tendrás que complementar el cuaderno con código propio para realizar una tarea adicional que será convenientemente anunciada. El plazo de entrega acaba el 26 de mayo de 2023 a las 23.59 horas.

## Primera sesión (29 de marzo de 2023)

**Contenidos a preparar antes de la sesión del 29/03/2023**

Las actividades a realizar antes de esta clase son:

- Lectura y estudio de los contenidos de [esta página](https://jaspock.github.io/me/materials/transformers/regresor) sobre regresión logística. Puedes saltar por ahora el apartado de [implementación en PyTorch](https://jaspock.github.io/me/materials/transformers/regresor#regresores-implementados-en-pytorch), ya que será el eje central de la clase presencial. Como verás, la página te indica qué contenidos has de leer del libro. Tras una primera lectura, lee las anotaciones del profesor, cuyo propósito es ayudarte a entender los conceptos clave del capítulo. Después, realiza una segunda lectura del capítulo del libro. En total, esta parte debería llevarte unas 3 horas 🕒️ de trabajo.
- Visionado y estudio de los tutoriales en vídeo de esta [playlist oficial de PyTorch](https://www.youtube.com/playlist?list=PL_lsbAsL_o2CTlGHgMxNrKhzP97BaG9ZN).  Estudia al menos los 4 primeros vídeos (“Introduction to PyTorch”, “Introduction to PyTorch Tensors”, “The Fundamentals of Autograd” y “Building Models with PyTorch”). En total, esta parte debería llevarte unas 2 horas 🕒️ de trabajo.
- Tras acabar con las dos partes anteriores, realiza este [test de evaluación](https://forms.gle/E1xzZHw6hzMWJaNr7) de estos contenidos. Son pocas preguntas y te llevará unos minutos.

**Contenidos para la sesión presencial del 29/03/2023**

En la clase presencial, repasaremos los contenidos de la semana anterior y veremos cómo se implementa el regresor logístico en PyTorch siguiendo la implementación de un regresor logístico binario y de uno multinomial que se comentan en [este apartado](https://jaspock.github.io/me/materials/transformers/regresor#regresores-implementados-en-pytorch).

La idea es que vayas creando una serie de notebooks en Google Colab en los que incluyas y comentes cada uno de los programas que vamos a ir viendo. En la última clase se presentará una práctica más avanzada que implicará modificar el código del transformer.

## Segunda sesión (26 de abril de 2023)

Entre la sesión anterior y la del 26 de abril transcurren varias semanas, por lo que la carga de trabajo es mayor que en la sesión anterior.

**Contenidos a preparar antes de la sesión del 26/04/2023**

Las actividades a realizar antes de esta clase son:

- Lectura y estudio de [esta página](https://jaspock.github.io/me/materials/transformers/embeddings) sobre la obtención de embeddings incontextuales. Puedes saltar de nuevo el apartado de [implementación en PyTorch](https://jaspock.github.io/me/materials/transformers/embeddings#implementación-en-pytorch), ya que se estudiará en la próxima clase presencial. Como verás, la página te indica qué contenidos has de leer del libro. Tras una primera lectura, lee las anotaciones del profesor, cuyo objetivo es ayudarte a entender los conceptos clave del capítulo. Después, realiza una segunda lectura del capítulo. En total, esta parte debería llevarte unas 4 horas 🕒️ de trabajo.
- Lectura y estudio de [esta página](https://jaspock.github.io/me/materials/transformers/ffw) sobre las redes neuronales hacia delante. Puedes saltar de nuevo el apartado de [implementación en PyTorch](https://jaspock.github.io/me/materials/transformers/ffw#implementación-en-pytorch), ya que se estudiará también en la próxima clase presencial. En total, esta parte debería llevarte unas 3 horas 🕒️ de trabajo.
- Primeros pasos en el estudio del modelo transformer. Volveremos a dedicar más horas a esta arquitectura para la próxima sesión de forma que la abordaremos en dos fases. Por ahora, lee con detenimiento la introducción a mecanismos de atención de ["Visualizing A Neural Machine Translation Model"](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/), así como la introducción visual a los transformers de ["The Illustrated Transformer"](http://jalammar.github.io/illustrated-transformer/). A continuación, lee el apartado 9.7 (solo este apartado) del capítulo ["Deep learning architectures for sequence processing"](https://web.archive.org/web/20221216193204/https://web.stanford.edu/~jurafsky/slp3/9.pdf); el objetivo es que entiendas conceptualmente el mecanismo de atención de los transformers, pero no es necesario que en este momento comprendas todos los detalles técnicos (especialmente las ecuaciones del modelo), ya que volverás a dedicarle tiempo a este capítulo más adelante. En total, esta parte debería llevarte ahora unas 4 horas 🕒️ de trabajo.
- Realización del [test de evaluación](https://forms.gle/Eb3ZwwGxbQp88t4FA) de estos contenidos. Son pocas preguntas y te llevará unos minutos.

**Contenidos para la sesión presencial del 26/04/2023**

En la clase presencial, repasaremos los contenidos de la semana anterior y veremos sendas implementaciones en PyTorch del algoritmo [skip-grams](https://jaspock.github.io/me/materials/transformers/embeddings#implementación-en-pytorch) y de un modelo de lengua basado en [redes feedforward](https://jaspock.github.io/me/materials/transformers/ffw#implementación-en-pytorch).

## Tercera sesión (10 de mayo de 2023)

**Contenidos a preparar antes de la sesión del 10/05/2023**

**Contenidos para la sesión del 10/05/2023**
