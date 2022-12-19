
(label_Semantica_Vectorial)=
Análisis semántico vectorial
============================

## Índice

- Introducción a los modelos semánticos vectoriales.
- Estudio de caso: *topic modeling*.

## Lectura obligatoria:

Peter D. Turney y Patrick Pantel (2010) "From Frequency to Meaning: Vector Space Models of Semantics" en *Journal of Artificial Intelligence  Research*, 37, págs. 141-188.  DOI: https://doi.org/10.1613/jair.2934

[https://www.jair.org/index.php/jair/article/view/10640](https://www.jair.org/index.php/jair/article/view/10640)

[https://www.jair.org/index.php/jair/article/view/10640/25440](https://www.jair.org/index.php/jair/article/view/10640/25440)

## Objetivos

- Definir semántica distribucional.
- Comprender cómo se representa el significado mediante vectores.
- Conocer los principales factores que determinan la representación vectorial.
- Conocer los conceptos de distancia y similitud, y medidas básicas.

## Introducción

Semántica vectorial: Nueva aproximación **formal** a la **semántica** de las lenguas naturales.

- Formalismo:
  - Espacios vectoriales y álgebra lineal.
  - *Quantum semantics*: similar al caso de la mecánica cuántica matricial de
    [Heisenberg](https://es.wikipedia.org/wiki/Werner_Heisenberg).
  - Geometría: relaciones de *similitud semántica* basadas en
    *distancias* (Widdows 2004).

- Semántica contextual y distribucional (basada en el uso).
  - vs. unidad atómica (lógica formal): "casa"
  - vs. definición (semántica léxica).
  - vs. relaciones léxicas paradigmáticas (WordNet *synset*).

## Origen

**Recuperación de información** (*Information Retrieval*): ej.
buscadores de internet.

- Tarea: dada una *query* (uno o más términos), obtener una lista de
  documentos ordenada por relevancia.
- Matriz Término - Documento.
- Cada documento se representa como una "bolsa de palabras" (*bag of
  words*): conjunto de palabras sin relación entre ellas.

Matriz Término - Documento

- Columnas: documentos.
- Líneas: términos
- Valores: frecuencia del término en cada documento.

Con dos documentos:

doc1 $= \{casa, madera, mesa\}$

doc2 $= \{papel, rama, madera\}$


  -------- ------- ------- ------ ---------
            Doc 1   Doc 2   \...   Doc $n$
    casa      1       0     \...    \...
    madera    1       1     \...    \...
    mesa      1       0     \...    \...
    papel     0       1     \...    \...
    rama      0       1     \...    \...
  -------- ------- ------- ------ ---------

Matriz Término-Documento

## Fundamentos lingüísticos

Los modelos semánticos vectoriales asumen básicamente tres propuestas teóricas (Clarke 2011):

1.  La idea de Wittgenstein (1953) de "meaning just is use"
    (Wittgenstein 1953);

2.  El concepto de *collocation* de Firth (1957) y su idea
    de que

    > "you shall know a word by the company it keeps";

3.  La hipótesis distribucional de Harris (1968):

    > "words will occur in similar contexts if and only if they have similar meanings".

Todo ello se engloba dentro del concepto de "significado
distribucional".

## Representación vectorial del significado

Un vector captura la semántica contextual/distribucional de la palabra (token o lema) al representar el número de veces (frecuencia) que la palabra aparece en cada contexto (documento).

  ------- ------ ------
           doc1   doc2
    car     7      6
    taxi    5      6
    train   6      1
  ------- ------ ------

$car = (7,6)$\
$taxi = (5,6)$\
$train = (6,1)$

Representación en un espacio euclídeo (plano o lineal). Representación mediante coordenadas cartesianas. Los valores del vector se proyecta en los ejes de coordenadas.

Espacios $n$-dimesionales o multidimensionales: para representar el significado de una palabra, las dimensiones (coordenadas) son los contextos en los aparece la palabra (en este caso, documentos).

Plano cartesiano (dos dimensiones):

![cartesanio1](images/cartesiano_1.png)

![cartesanio2](images/cartesiano_2.png)

----------------

La representación del significado varía según se diseñe el espacio vectorial.

Factores relevantes:

- Representación del contexto (dimensiones)
- Representación de las palabras (filas)
- Valores o pesos de cada palabra en cada contexto.


### Representación del contexto

Cada uno de los contextos donde pueda aparece una palabra será una
dimensión.

¿Cómo delimitar el contexto?

Matriz Término-Documento. Modelo de representación propio de Recuperación de Información. El contexto es todo el texto o documento donde aparece la palabra. El concepto de contexto muy laxo, pero es eficiente. No tiene en cuenta las relaciones entre palabras y puede haber contextos de difererente tamaño.

Esta idea se puede llevar a contextos con una mayor motivación lingüística:

- oración,
- párrafo u otra unidad textual,
- capítulos,
- etc.


Matriz de co-ocurrencias: Matriz Término-Término: número de veces que dos palabras aparecen en los mismos contexto.

Contexto más pequeño y motivado lingüísticamente: oración, relación sintáctica, ventana de palabras u oraciones (párrafo deslizante), etc.

  ------ ----- ---------- ------
           red   readable   blue
    car     5       0        1
    book    3       6        0
  ------ ----- ---------- ------

Ejemplo de matriz con motivación lingüística fuerte: matriz *Pair-Pattern* (TurneyPantel 2010): Las filas son parejas de palabras ("carpenter:wood"), las columnas son relaciones entre palabras co-ocurrentes ("X cut Y").

Y por aquí se pueden definir variantes. En todos estos casos, lo que cambia es cómo se representa el contexto.

### Representación de las palabras

Según vimos en sesiones anteriores:

- Token
- Raíz (stem)
- Lemas
- Lema + Categoría Gramatical
- Filtro *stopwords*
- Sólo nombres (o sólo verbos, o sólo adjetivos, etc.)
- Lema + Función sintáctica
- etc.

Requieren pre-proceso del corpus con técnicas de PLN vistas con anterioridad.

### Cálculo de los valores o pesos

Representación cuantitativa de la relevancia (peso) que tiene la palabra en cada contexto.

Frecuencias simples y relativas: número de veces que la palabra aparece en el contexto, normalizado por el tamaño del contexto.

Problemas:

- Depende del tamaño del contexto.
- No discrimina la importancia real de cada palabra en el contexto.
- El *[hapax legomenon]*(https://en.wikipedia.org/wiki/Hapax_legomenon)


#### TF/IDF: *term frequency / inverse document frequency* (Sparck Jones, 1972)

Idea intuitiva: palabras de uso común que aparecen con alta frecuencia en muchos contextos no son discriminativas ni relevantes. TF/IDF intenta dar más peso a las palabras específicas de cada documento.

- *Term frequency* (tf): frecuencia de una palabra en un documento dado.
- *Document frequency* (df): cantidad de documentos donde aparece una determinada palabra.
- *Inverse document frequency* (idf): $N/df$ donde N = cantidad total de documentos.

Así, el valor tf-idf ($w$) de una palabra $t$ en un documento $d$ es:

$$w_t,_d = tf_t,_d · idf_t$$


#### Matriz dispersa y matriz densa

Dadas las caracterísiticas de los idiomas, este tipo de matrices son siempre muy dispersas, en las que la mayoría de los valores con cero.

> *Sparse matrix*: la mayoría de los valores son ceros.

Para solucionar esto se reduce la dimensionalidad de la matriz, generando así  matrices densas (*dense matrix*) donde la mayoría de los valores no son ceros pero manteniendo las relaciones semánticas entre las palabras (los valores semánticos).

[*Latent semantic analysis*](https://en.wikipedia.org/wiki/Latent_semantic_analysis): descomposición de la matriz dispesar en valores singulares ([*singular value decomposition*](https://en.wikipedia.org/wiki/Singular_value_decomposition)), generando una matriz densa de 300 dimensiones. Se considera que mantiene relaciones semánticas "latentes". Origen de los *word embeddings* que veréis en próximos temas.


## Interpretación semántica: distancia y similitud.

La interpretación en esta aproximación vectorial a la semántica distribucional se realiza por relaciones de similitud entre palabras o documentos. La similitud se calcular según la distancia entre los vectores en el espacio vectorial: a menor distancia entre vectores, mayor similitud semántica.

Así, desde un punto de vista lingüístico, dos vectores (de palabras) serán similares en la medida que tengan valores relevantes en los mismos contextos.

Cualquier aplicación de semántica vectorial debe pensarse en términos de
similitudes (entre palabras, grupos de palabras, textos, etc.).

Hay diferentes medidas. Las más utilizada es la similitud del coseno, que mide el ángulo entre dos vectores ambos con origen en 0,0.

$$cos(a,b) = \frac{a · b}{||a|| ||b||}$$


![cartesanio2](images/cartesiano_2.png){height="10cm"}



### Conclusiones

- Representación formal del significado distribucional.
- El significado se represente mediante vectores dentro de un espacio semántica vectorial.
- El vector está formado por el peso de la palabra en cada uno de los contextos (documentos, oraciones, etc.)
- El proceso de interpretación se basa en la distancia entre vectores: similitud.

## Situación actual

De aquí derivan los *word embeddings* que, junto con las redes neuronales, han revolucionado el campo del PLN. De todo esto os hablará el prof. Juan Antonio Pérez Ortiz en las próximas sesiones.

## Herramientas y recursos

Para crear espacios vectoriales y calcular similitudes:

- [GENSIM](https://radimrehurek.com/gensim/)
- [NLTK](http://www.nltk.org/)
- [Pattern](http://www.clips.ua.ac.be/pattern)
- [SpaCy](https://spacy.io/)

## Apéndice. Estudio de caso.

Extracción de *topics* con *Topic Modeling*.

[Acceso a la presentación](https://docs.google.com/presentation/d/e/2PACX-1vRhjksmebwfZ8CfMNCqp7ucPr0i--fPNCa6dqb0NH3jiMOQV1lSvnlnF7qptbtqEsA5O4IzpcJa-F9r/pub?start=false&loop=false&delayms=60000)

## Bibliografía

David M. Blei (2012) "Probabilistic topic models" en *Communications of the ACM* vol. 55 (4), April 2012. Doi:10.1145/2133806.2133826
[https://dl.acm.org/doi/10.1145/2133806.2133826](https://dl.acm.org/doi/10.1145/2133806.2133826)

Juravsky y Martin (2020) *Speech and Language Processing*. https://web.stanford.edu/~jurafsky/slp3/ 
(Caps. 12-14)

Ferrone Lorenzo y Zanzotto Fabio Massimo (2020) "Symbolic, Distributed, and Distributional Representations for Natural Language Processing in the Era of Deep Learning: A Survey" en *Frontiers in Robotics and AI*, pags, 153. DOI 10.3389/frobt.2019.00153
[https://www.frontiersin.org/article/10.3389/frobt.2019.00153](https://www.frontiersin.org/article/10.3389/frobt.2019.00153)

Navarro Colorado, Borja (2021) "Sistemas de anotación semántica para corpus de español" en Giovanni Parodi, Pascual Cantos & Lewis Howe (Editores) *The Routledge Handbook of Spanish Corpus Linguistics* Routledge (en prensa).

D. Widdows (2004) *Geometry and meaning*, CSLI.

