
Representaciones de palabras y oraciones
========================================

Un aspecto fundamental en el procesamiento del lenguaje natural es utilizar representaciones numéricas adecuadas de los textos en los diferentes niveles (subpalabras, palabras, frases,  párrafos, etc.). En este apartado nos centraremos especialmente en las palabras y en uno de los algoritmos más utilizados para obtener dichas representaciones conocidas como *word embeddings*.

## Introducción a los embeddings de palabras

Para una introducción sencilla al tema puedes seguir la [guía ilustrada][guía] sobre embeddings de palabras de Jay Alammar. Esta guía describe la familia de algoritmos conocidos como *word2vec*que incluye las técnicas denominadas *contextual bag of words* (CBOW) y *skip-grams*. Aquí nos centraremos en una versión simplificada de la segunda, pero las ideas en las que se basa la primera son muy similares.

[guía]: https://jalammar.github.io/illustrated-word2vec/

Los contenidos nucleares del tema son los incluidos en las secciones 6.4 y 6.8-6.12 del capítulo 6 ("Vector semantics and embeddings") de la tercera edición del libro "[Speech and language processing][jurafsky]". Usa esos contenidos junto con los apuntes de clase en tu aprendizaje. Algunos conceptos básicos como la entropía cruzada o el algoritmo de descenso por gradiente se introducen en las secciones 5.4-5.6, aunque estos se discutirán en clase y en otras asignaturas.

[jurafsky]: https://web.stanford.edu/~jurafsky/slp3/

```{admonition} Nota
:class: note
Los algoritmos de word2vec no son la única manera de obtener embeddings de palabras.

Se puede utilizar una red neuronal *feedforward* con una capa oculta que usa a la entrada los embeddings de las *n* palabras anteriores y emite a la salida la probabilidad de la siguiente palabra. En este caso, las activaciones de la capa oculta se podrían tomar como los embeddings de dicha palabra. A diferencia de CBOW, aquí habría una capa oculta y se usarían solo las palabras anteriores, aunque es trivial adaptar la red para que use a la entrada un contexto de palabras anteriores y posteriores.

Una opción más elaborada pasa por usar una red neuronal recurrente con una capa oculta entrenada para predecir la siguiente palabra. Una vez finalizado el entrenamiento, se podrían utilizar las representaciones de estado de la capa oculta como embeddings de las palabras. A diferencia de CBOW, los embeddings aquí no son estáticos (incontextuales): dada una frase en particular, se puede ir suministrando a la red recurrente los embeddings de las palabras anteriores y obtener una representación vectorial de la siguiente palabra en el contexto anterior concreto de dicha frase.</p>
<p>Más adelante, veremos arquitecturas aún más avanzadas (como BERT) que permiten obtener embeddings contextuales más profundos.
```

De los embeddings aprendidos con word2vec se pueden obtener ciertas analogías interesantes con simples operaciones aritméticas sobre los embeddings. Así, si consideramos el embedding más cercano al vector resultante de calcular embedding("France") - embedding("Paris") + embedding("Rome"), este resulta ser el correspondiente a "Italy". Otras analogías interesantes se pueden ver en la figura {numref}`analogia-word2vec`.

```{figure} images/mikolov-word2vec-analogies.png
---
height: 400px
name: analogia-word2vec
---
Analogías mostradas en el trabajo de [Mikolov et al.][mikolov2013] de 2013.

[mikolov2013]: https://arxiv.org/pdf/1301.3781.pdf
```

```{admonition} Nota
:class: note
Es recomendable que amplíes tus conocimientos sobre la [entropia][entropía] y la [entropía cruzada][cruzada] siguiendo estos enlaces, ya que son conceptos fundamentales en aprendizaje automático, en general, y procesamiento del lenguaje natural, en particular.

[entropía]: https://towardsdatascience.com/cross-entropy-loss-function-f38c4ec8643e
[cruzada]: https://towardsdatascience.com/cross-entropy-for-classification-d98e7f974451
```

## Visualización de embeddings

Mediante la herramienta [Embedding Projector][projector] vamos a explorar visualmente la distribución de las palabras en el espacio de embeddings. 

[projector]: https://projector.tensorflow.org/

La herramienta tiene varios paneles:

- El panel de datos en el que seleccionamos los datos a examinar; nos vamos a centrar en el conjunto *Word2Vec All* (embeddings de dimensión 200 para unas 71000 palabras).
- El panel de proyección en el que se selecciona la técnica de reducción de dimensionalidad utilizada para representar los datos en un espacio de bi o tridimensional; podemos empezar por seleccionar PCA (*principal component analysis*), que es más rápida.
- El panel de visualización en el que se muestran los embeddings.
- El panel de inspección en el que podemos introducir una palabra y ver la lista de sus vecinos más cercanos.

Para visualizar sesgos en las distribuciones podemos ir al panel de proyección y en *Custom* elegir el embedding de una palabra para el lado izquierdo y otro para el derecho. En el panel de *bookmarks* (abajo a la derecha) puedes encontrar un ejemplo ya creado. La expresión regular para una palabra exacta es /^bad$/, por ejemplo.

## Colecciones de embeddings para palabras y frases

Existen colecciones como [fastText][fasttext], que incluyen embeddings para dos millones de palabras en inglés (obtenidos procesando un corpus de 16.000 millones de palabras) o embeddings multilingües para más de cien idiomas. Aunque las representaciones a nivel de frase se pueden obtener mediante la integración de las representaciones individuales de las palabras, hay sistemas más avanzados como [LASER][laser] que ofrecen un codificador neuronal capaz de emitir embeddings de frases en 93 idiomas (23 alfabetos diferentes).

[fasttext]: https://fasttext.cc/
[laser]: https://github.com/facebookresearch/LASER
