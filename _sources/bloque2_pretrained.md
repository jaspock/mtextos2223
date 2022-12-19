Modelos preentrenados
=====================

```{image} images/elmo.png
:alt: ELMo
:width: 120px
:align: left
```
% http://123emoji.com/wp-content/uploads/2017/08/sticker-19-70.png

Los denominados *modelos neuronales preentrenados* han supuesto todo un lavado de cara para el procesamiento del lenguaje natural. Aunque la cantidad de este tipo de modelos existente hoy día es enorme, casi todos comparten los mismos fundamentos. El punto de inflexión de estos modelos lo podemos situar en el año 2018 con la aparición de ELMo, en primer lugar, y BERT, unos meses después. Nos centraremos en este último en nuestro estudio, pero sin descuidar otras propuestas.


```{admonition} Nota
:class: note
Podemos decir que estos modelos son un ejemplo de *aprendizaje por transferencia* (*transfer learning*) en el que lo aprendido para una tarea secundaria ayuda a resolver la tarea principal. La tarea secundaria en este caso es *no supervisada* (*unsupervised*) en el sentido de que no utiliza datos etiquetados externamente (como cuando anotamos la polaridad de un texto), pero el entrenamiento sigue teniendo una función de pérdida en la que el valor emitido se compara con el deseado, por lo que para evitar confusión se habla de entrenamiento *autosupervisado*. En el entrenamiento autosupervisado las etiquetas que conforman el valor esperado se obtienen automáticamente a partir de la muestra con un algoritmo normalmente muy simple, pero, al mismo tiempo, la tarea de generarlas adecuadamente no es trivial e implica que para hacerlo la red ha de generar buenas representaciones intermedias.
```

```{figure} images/pretrained.png
---
height: 360px
name: fig-pretrained
---
Algunos de los hitos en la historia reciente del procesamiento del lenguaje natural. Tomado de "2019, [year of BERT and Transformer][year]" de Manu Suryavansh.
```
[year]: https://towardsdatascience.com/2019-year-of-bert-and-transformer-f200b53d05b9


## Introducción a ELMo y BERT

Para comenzar con el tema, vamos a seguir la guía ilustrada de Jay Alammar sobre los modelos [BERT y ELMo][bertilustrado]. 

[bertilustrado]: http://jalammar.github.io/illustrated-bert/


```{admonition} Problema
:class: note
Obtén los códigos BPE resultantes de aplicar 4 operaciones de unión al texto "para el bus en la parada abandonada". A continuación, aplica los códigos a la entrada "ensalada para la empanada".
% p a  |  pa r  |  d a</w>  | a da</w>
% e@@ n@@ s@@ a@@ l@@ ada par@@ a la e@@ m@@ pa@@ n@@ ada
```

## Tipología de modelos preentrenados

Ahora vamos a ahondar en las características de estos modelos con las diapositivas del tema "[Pretraining][diapositivas]" que John Hewitt usa en el curso "CS224n: Natural Language Processing with Deep Learning" de la Universidad de Stanford.

[diapositivas]: http://web.stanford.edu/class/cs224n/slides/cs224n-2021-lecture10-pretraining.pdf
