(label_PoS)=
Análisis categorial y sintáctico
=================================

```{admonition} Nota
:class: note
Para preparar este tema, consulta los capítulos 12, 13 y 14 de Juravsky y Martin (2022) *Speech and Language Processing*. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/).
```

## Unidades de comunicación básica. La palabra. *Type*, *token* y lema.

Si bien el concepto de "palabra" se suele utilizar como unidad mínima y básica de comunicación, realmente desde la palabra no tiene en lingüística una definición clara: es un concepto vago muy difícil de delimitar.

En lingüística de corpus, lingüística computacional y procesamiento del lenguaje natural, más que con el concepto de "palabra", se trabaja con los conceptos de *type* ("tipo") y *token* ("caso") ([introducidos por el filósofo Charles S. Peirce](https://es.wikipedia.org/wiki/Caso_y_tipo) a principio de siglo XX):

  - *Type* es la palabra entendida como clase o tipo. Una secuencia de caracteres diferente de cualquier otra secuencia.  
  - *Token* es cada una de las instancias o casos concretos de esas clase *type* que se pueda hallar en un texto [^1].

Se suele ejemplificar la diferencia entre ambos conceptos con el verso de G. Stein:

> "Rose is a rose is a rose is a rose";

pero para españolizarlo un poco vamos a coger como ejemplo el siguiente verso de [esta canción](https://www.youtube.com/watch?v=dv958EeZXHc) de _Mecano_, que es una versión simplificada del verso de Stein:

> "Una rosa es una rosa es".

En este verso encontramos tres *types*:

- "una"
- "rosa"
- "es";

pero seis *tokens*: 2 *tokens* del *type* "una", 2 del *type* "rosa" y 2 del *type* "es". Son por tanto $2+2+2 = 6$ *tokens*. Este texto está formado por seis *tokens* y tres *types*.

Como se puede comprobar, esta diferencia es la base conceptual del cálculo de frecuencias textuales. El cálculo más simple es contar, como se ha hecho antes, la cantidad de *tokens* de cada *type* en un texto:

|*type*|*tokens*|
|------|--------|
|una   | $2$    |
|rosa  | $2$    |
|es    | $2$    |

En esta línea, **el tamaño de un corpus siempre se mide en cantidad de *tokens*.**

### Tokenización

El primer paso a la hora de procesar un texto es, por tanto, hallar los *tokens* y, con ello, los *types* que forman el texto. A este proceso se le denomina **tokenización**.

El método de tokenización más simple es separar cada token por espacio en blaco. *Token* quedaría así definido como la secunencia de caracteres separada por un espacio en blanco. Desde un punto de vista lingüístico, esta aproximación presenta algunas limitaciones:

1. Los signos de puntuación son un *type* diferente, per aparecen pegados a la palabra anterior o posterio. Es necesario algún tipo de regla más allá del espacio en blanco que separe los signos de puntuación.
2. Hay unidades lingüísticas que están formadas por más de un *type*. Me refiero a las llamadas "unidades multipalabra", como por ejemplo las formas complejas de los verbos: "he comido", "había creídos", "fue resuelto", etc. 
3. La situación contraria se produce con las contracciones como "del" o "al" y en general formas aglutinantes ("dáselo"). En este caso se podría considerar *types* diferentes porque responde a diferentes palabras y habría que separarlas. 

Un *tokenizado* estándar resuelve el primer problema de los signos de puntuación, pero no los otros dos. Esto se deja para el lematizados, que se comentará después.

Por otro lado, no siempre la tokenización depende del espacio en blanco. Como se comentó antes, un *token* es la instancia de un *type*. Este puede ser cualquier secuencia de caracteres que se repitan en el texto, incluso se podría tokenizar por caracteres individuales.

Los sistemas neuronales explotan diversas formas de tokenización para mejorar los análisis. En capítulos siguiente se verá cómo. Los sistemas de PLN estándar suelen trabajar con la tokenización por espacio en blanco. La herramienta NLTK (*Natural Language Toolkit*) dispone de diferentes [tokenizadores](https://www.nltk.org/api/nltk.tokenize.html).[^3]

### Lematización y *stemming*

*Type* y *token* se refieren siempre a formas flexionadas, es decir, a formas con variaciones morfológicas. Así, "catamos" y "cantaré" son *types* distintos; al igual que "casa" y "casas".

Para agrupar todos los *tokens* relacionados con la misma palabra (es decir, la forma sin flexionar o la unidad léxica que podemos encontrar, por ejemplo, en los diccionarios) se realiza un proceso de _lematización_. La lematización consiste en asignar a cada palabra lo que en lingüística se denomina su "forma no marcada": el infinitivo para verbos, o la forma masculino singular para nombres y verbos. La forma no marcada es la que aparece en el diccionario. El lema es una manera de nombrar la palabra en toda su diversidad flexiva.

La lematización es un fenómenos complejo porque para saber el lema de un *token* es necesario analizar morfológicamente la palabra. Hay muchos casos de ambigüedad. Por ejemplo, el lema del *token* "traje" puede ser tanto "traer" (si es verbo) como "traje" (si es nombre), como en el siguiente texto:

> - ¿Usted no nada nada?
> - Es que no traje traje.

Por ello en algunas aplicaciones como en recuperación de información, en vez de una lematización completa, se utiliza un proceso similar pero más rápido y sencillo denominado ***stemming***. Este consiste en reducir cada *token* a su raíz o lexema, es decir, la parte invarible del *token* (siempre y cuando responda a una flexió morfológica regular) que, en principio, asume el significado general de la palabra. Así, por ejemplo, de las diferentes formas del verbo "amar" (amaría, amaré, amado, ame, etc.), un *stemmer* reduciría cada *token* a su raíz "am-", mientras que un lematizador lo relacionaría con el lema "amar".  

<!-- *Reflexión:* para minería de textos, ¿qué es mejor, dejar el corpus con los *tokens*, lematizarlo o trabajar solo con las raíces léxicas (*stemm*)? -->

## Análisis morfológico y categorial.

La herramienta de PLN que realiza el análisis morfológico y categorial es el *Part of Speech tagger* (*pos_tagger* o analizador categorial).

El objetivo principal de una analizador categorial es asignar a cada *token* de un texto su categoría gramatical correspondiente, incluidos signos de puntuación. En concreto, los datos que analiza un *pos_tagger* estándar suelen ser, por cada *token*: 

- el lema,
- la categoría gramatical ("nombre, verbo, adjetivo, ..."),
- rasgos morfológicos (género, número, voz, tiempo, etc.).

El mayor problema que resuelve un analizador categorial es la *ambigüedad categorial* que vimos anteriormente: aquellos *tokens* que pueden pertencer a dos o más categorías gramaticales.

### Algunos conceptos lingüísticos.

A modo de recordatorio, en esta sección se repasan algunos conceptos lingüísticos que se deben tener claros para trabajar con *PoS_taggers*.[^4]

Las palabras de un idioma se clasifican en categorías gramaticales o "clases de palabras". Cada categoría agrupas palabras que tienen un corportamiento lingüístico similar: palabras con rasgos distributivos y morfológicos similares, y en algunos casos también rasgos semánticos parecidos.

Si bien no hay una lista fija de categorías gramaticales (las diferentes teorías suelen presentar pequeñas variantes), en español las categorías gramaticales suelen ser: determinantes (incluyendo aquí artículos, demostrativos, posesivos, numerales e indefinidos), sustantivos, adjetivos, pronombres, verbos, adverbios, preposiciones, conjunciones e interjecciones.

Estas clases se agrupan en dos grandes grupos: las categorías abiertas y cerradas. Las abiertas son aquellas en las que constantemente está apareciendo palabras nuevas (neologismos) y desapareciendo otras (arcaísmos): nombres, verbos y adjetivos sobre todo. Las clases cerradas son las clases más estables porque apenas cambian en el tiempo (preposiciones, determinantes, conjunciones, interjecciones principalmente).

Este diferencia es relevante desde el punto de vista computacional por dos hechos:

1. Todo sistema de PLN debe estar preparado para analizar palabras nuevas. En una clase abierta el sistema de PLN se puede encontrar con palabras que no ha visto nunca antes (bien porque no está en el diccionario, bien porque no está en los corpus de aprendizaje, o bien porque es un neologismo) y debe ser capaz de analizarla. Este problema se da sobre todo con los nombres. Los sistemas neuronales actuales han mostrado ser muy eficaces para tratar este problema.
2. Las clases cerradas suelene estar formadas por pocas palabras. Esto provoca que la frecuencia de uso de las palabras de clases cerradas (preposiciones, conjunciones, pronombres, etc.) sea muy alta. Así, al extraer las frecuencias de cualquier texto encontramos pocas palabras con frecuencias muy altas (las palabras de categorías cerradas) y muchas palabras con frecuencias muy bajas (el llamado [*hápax legómena*](https://es.wikipedia.org/wiki/H%C3%A1pax), que se produce por la gran cantidad de palabras de categorías abiertas que aparecen solo una vez). Esto complica los análisis de frecuencia. Para evitar esta situación, las palabras de categoras cerradas se suelen filtrar antes de extraer frecuencias: son las llamadas *stop words*.

Por su flexión, hay categorías cuyas palabras son variables o "flexivas" y categorías de palabras invariables. Son categorías variables los nombres (con flexión de género y número), verbos (con flexión en tiempo, modo, voz, aspectos, número y persona), adjetivos (género, número y grado), pronombres y algunos adverbios y determinantes. La flexión tiene implicaciones semánticas, por lo que su análisis es más complejo. Esta es la razón de ser del análisis morfológico completo, donde de cada *token* se especifica automáticamente no solo su categoría gramatical, sino también sus rasgos flexivos. 

Finalmente, por su función en el texto, se diferencia entre clases de palabras con significado léxico (nombres, verbos, adjetivos, adverbios) y clases de palabras con "significado" gramatical (determinantes, preposiciones, pronombres, etc.). Este significado gramatical no es significado pleno. Se refiere a que esas palabras pueden modificar o determinar el significado de las palabras con significado léxico con las que aparecen, pero en sí mismas y por sí solas no podemos decir que tengan un significado completo. Una preposición como "ante", por ejemplo, podemos intuir rasgos semánticos ("frente a algo o delate de algo"), pero su función es completar ese "algo" con indicación de posición ("se paró _ante_ de la puerta").

### Relevancia del análisis categorial en Minería de textos

Así como un proceso de tokenización es un paso inleduble para realizar minería de textos, el análisis categorial no siempre es necesario. Éste es un proceso que requiere recursos computacionales y, si el corpus es muy amplio, también tiempo de procesamiento. Por ello se debe tener claro qué se necesita para valorar si es necesario utilizar un *pos tagger* o no.

Un análisis categorial es en muchas ocasiones la base del sistema de PLN, porque los análisis sintáticos y muchos de los análisis semánticos y pragmáticos dependen de las clases de palabras: necesitan saber el lema de cada *token*, la clase de palabra a la que pertenecen y/o sus rasgos morfológicos. 

Un proceso muy común en minería de texto y de poco coste computacional es realizar un filtro de "stop words": elimiar todas aquellas palabras que pertenecen a categorías cerradas y que no tienen significado léxico (preposiones, conjunciones, artículos, etc.). Este filtrado NO necesita realizar el análisis categorial completo: como son categorías cerradas (es, por tanto, un conjunto finito de palabras), se pueden listar en un fichero y filtrar con un simple *pattern matching*. También un proceso de *stemming* requiere poco tiempo de proceso (no es necesario realizar todo el ánalisis categorial) y permitiría tratar *token* de categorías flexivas como un solo *type*.

Otras aplicaciones de minería de textos sí dependen de las categorías gramaticales y por tanto requieren realizar el análisis categorial y morfológico. Entre otras: 

- la *extracción de entidades* necesita saber qué palabras son nombres y en especial los nombres propios;
- la *extracción de eventos* necesita saber qué palabras son verbos y qué palabras son nombres;
- el *análisis de sentimientos y opiniones* depende mucho de los adjetivos;
- la *detección de autoría* determina automáticamente quién es el autor de un texto sobre todo por cómo se utilizan las palabras de categorías cerradas (preposiciones, conjunciones, etc). Se ha demostrado que sus frecuencias de uso depende mucho del estilo personal de escritura de cada persona. La frecuencia de uso de otras clases de palabras como nombres o verbos depende más del tema del texto y no suelen ser buenos indicadores para detectar automáticamente la autoría de un texto.
- etc.

### Representación de la información morfológica y categorial

La información categorial y morfológica se representa explícitamente mediante etiquetas.

Actualmente hay diversas propuestas. Es necesario saber con qué juego de etiquetas representa la información el sistema de *PoS tagger* que estemos utilizando par poder interpretar la información correctamente.

Algunas propuestas:

- Penn Treebank tag set:

[https://www.cs.upc.edu/~nlp/SVMTool/PennTreebank.html](https://www.cs.upc.edu/~nlp/SVMTool/PennTreebank.html)

- EAGLES tag set:

[http://www.ilc.cnr.it/EAGLES96/annotate/annotate.html](http://www.ilc.cnr.it/EAGLES96/annotate/annotate.html)

[http://blade10.cs.upc.edu/freeling-old/doc/tagsets/tagset-es.html](http://blade10.cs.upc.edu/freeling-old/doc/tagsets/tagset-es.html)

[https://freeling-user-manual.readthedocs.io/en/latest/tagsets/](https://freeling-user-manual.readthedocs.io/en/latest/tagsets/)

- Universal tagset (*Universal dependencies project*):

[https://universaldependencies.org/u/pos/](https://universaldependencies.org/u/pos/)

### Arquitectura de un *PoS_tagger*. Algoritmos clásicos de desambiguación.

![ArquitecturaPoStagger](images/arquitecturaPoStagger.png)

Ejemplo: Freeling.

### Algoritmos de desambiguación categorial (aproximación histórica)

#### Modelo de reglas simples.

Sistema TAGGIT (1950).
71 etiquetas + 3300 reglas. 77% de precisión.

Reglas: expresiones regulares tipo

    \b.*ing\b = Verbo Infinitivo
    \b.*mente\b = adverbio
    las\s[a-z]*as → Nombre femenino plural
    etc.

### Modelo estadístico: cadena de markov.

Tiene en cuenta el contexto de aparición de las palabras.
Basados en bigramas.

Calculan dos tipos de probabilidades:
     Léxica: p(W|T)
     Contextual: p(W|T|Ctx)

ctx = palabra anterior --> bigrama.

### Modelo oculto de Markov

Basado en la probabilidad de cadenas de etiquetas (cadena oculta).

Dos tipos de probabilidades:
- Probabilidad de emisión = p(W|T)
- Probabilidad de transmisión = p(T|T-1). Esta es la parte oculta.

Así, la probabilidad final queda como:

    p(W|T) = p(W|T) * p(T|T-1)

Proceso iterativo: primero analiza lo no ambiguo, luego hace una segunda vuelta calculando probabilidades de transición y re-anotando, hasta llegar a situación estable (fin).

### Gramáticas de restricciones (*Constraint grammar*)

Modelo teórico: este tipo de gramáticas no dice cómo es un idioma, sino cómo NO es.

Las reglas, por tanto, son reglas negativas. Dada una ambigüedad, las reglas indican cuál de las opciones seguro que no es. Combinando restricciones se llega al final a la solución correcta.

Las reglas son condicionales al contexto (si la palabra anterior es X, la siguiente NO es Y).

Ejemplo:
     "Un verbo no va precedido de artículo". 

Sistema ENGCG de 1990 (Karlsson et al 1995)


### Modelos basados en aprendizaje automático.

Sistemas supervisados. Aprendizaje a partir de un corpsu anotado a mano y validado por lingüistas.

Diferentes algoritmos: árboles de decisión, vectores de soporte (SVM), etc.

Ejemplo "Transformation-based Tagger" (Brill 1995). Proceso iterativo donde va aprendiendo reglas, cada vez más específicas. Analiza aplicando primero las específicas y luego las generales. Refinamiento: revisón manual de cada iteración.

### Situación actual

Aproximaciones multilingües basadas en *embeddings* y redes neuronales:

[http://nlpprogress.com/english/part-of-speech_tagging.html](http://nlpprogress.com/english/part-of-speech_tagging.html)


### Recursos.

Cualquier sistema de PLN parte de un PoS tagger. Es el análisis básico.

- Freeling [http://nlp.lsi.upc.edu/freeling/index.php/](http://nlp.lsi.upc.edu/freeling/index.php/)
- SpaCy: [https://spacy.io/](https://spacy.io/)
- NLTK: [http://www.nltk.org/](http://www.nltk.org/)
- Standford CORE NLP: [https://stanfordnlp.github.io/CoreNLP/](https://stanfordnlp.github.io/CoreNLP/)
- Google CLOUD: [https://cloud.google.com/natural-language/](https://cloud.google.com/natural-language/)

y muchos más


## Análisis sintáctico.

Sintaxis: agrupación y relaciones de las palabras dentro de una oración.

Análisis automático: *parser*

### Arquitectura estándar de un *parser*

![ArquitecturaParser](images/parser.png)

### Modelos de representación

Análisis basado en _constituyentes_

![Constituyentes](images/constituyentes.png)

Análisis basado en _dependencias_

![Dependecias_Freeling](images/dependency_parsing_FreeLing.jpg)

(Créditos de la imagen [aquí](http://liceu.uab.cat/~joaquim/language_technology/NLP/PLN_analisis.html#An%C3%A1lisis_de_dependencias))

### Principal problema computacional

Ambigüedad estructural:

    "Ayer vi a tu hermano con los prismáticos"

Ambigüedad coordinación:

    "Sirve los platos y los cubiertos limpios"

### Gramáticas formales

Conjunto de reglas formales de análisis sintático.

#### Context free grammars

    G = (NT, T, S, P)
    NT: {no terminales},
    T: {terminales},
    S: Símbolo inicial
    P: Reglas de producción A -> w: 
        A   NT
        W   (NT U T)*

Tal que

    NT ={S,NP,VP,nprop,n,v,det}, 
    T ={Pepe,manzana, come,una},
    P:
        S -> NP VP
        NP -> nprop
        NP -> det  n
        VP -> v
        VP -> v NP

![AnalisisConstituyentes](images/constituyentes_2.png)

Estas gramáticas eran muy limitadas y fueron ampliadas con estructuras de rasgos y técnicas de unificación.

![Unificación](images/unificacion.png)

En lingüística se han desarrollado diferentes modelos basados en estas técnicas las *Head-driven phrase structure grammar* o las *Lexical-Functional Grammar* (que sigue siendo un modelo válido: [https://ling.sprachwiss.uni-konstanz.de/pages/home/lfg/](https://ling.sprachwiss.uni-konstanz.de/pages/home/lfg/) )

#### *Probabilistic Context Free Grammar* y modelos probabilísticos

Añaden peso estadístico a cada regla.

    SV → V SP SP (0.5)
    SV → V SP (0.3)
    SV → V (0.2)

Modelos de aprendizaje automático.

Corpus de aprendizaje y evaluación: *treebanks*

- Penn Treebank:
    + [https://catalog.ldc.upenn.edu/LDC99T42](https://catalog.ldc.upenn.edu/LDC99T42)
    + [https://www.kaggle.com/nltkdata/penn-tree-bank](https://www.kaggle.com/nltkdata/penn-tree-bank)

- Ancora (español, catalán):
    + [http://clic.ub.edu/corpus/en/ancora-descarregues](http://clic.ub.edu/corpus/en/ancora-descarregues)

Y muchos otros

### *Chunkers*

En ocasiones el análisis sintáctico completo (*full parsing*) es complejo, consume mucho recurso y no suele obtener buenos resultados.

Lo normal es realizar _análisis sintáctico parcial_ o *chunkers*: extraer agrupaciones sintáticas (*chunks*) sin llegar a derivar el árbol sintáctico completo (Abney 1991).

### Estrategias

Descendente:
Recursive Descendent:

(El siguiente código es Python y requiere tener instalado [NLTK](https://www.nltk.org/))

    import nltk
    nltk.app.rdparser()

Ascendente
Shift Reduce:

    import nltk
    nltk.app.srparser()


### Formato CONLL

Formato de salida estándar en análisis de dependencias. Además de la información morfológica, por cada palabra indica de quién depende y el tipo de dependencia.

        Salida CoNLL-U
        # sent_id = 1
        # text = Los hombres que fuman puro tienen cara de canguro .
        1   Los el  DET DET Definite=Def|Gender=Masc|Number=Plur|PronType=Art   2   det _   _
        2   hombres hombre  NOUN    NOUN    Gender=Masc|Number=Plur 6   nsubj   _   _
        3   que que PRON    PRON    PronType=Int,Rel    4   nsubj   _   _
        4   fuman   fumar   VERB    VERB    Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin   2   acl _   _
        5   puro    puro    ADJ ADJ Gender=Masc|Number=Sing 4   obj _   _
        6   tienen  tener   VERB    VERB    Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin   0   root    _   _
        7   cara    cara    NOUN    NOUN    Gender=Fem|Number=Sing  6   obj _   _
        8   de  de  ADP ADP _   9   case    _   _
        9   canguro canguro NOUN    NOUN    Gender=Masc|Number=Sing 7   nmod    _   _
        10  .   .   PUNCT   PUNCT   PunctType=Peri  6   punct   _   _



### Situación actual

*Transition-based dependency parsing* (Nivre 2014). Algoritmo shift-reduce.

*Neural Network Dependency Parser*: [https://nlp.stanford.edu/software/nndep.shtml](https://nlp.stanford.edu/software/nndep.shtml)

Modelo de dependencias universal: [*Universal Dependencies*](https://universaldependencies.org/):

> The Universal Dependencies project (Nivre et al., 2016) provides an inventory of dependency relations that arelinguistically motivated, computationally useful, and cross-linguistically applicable. (Juravsky y Martin 2020, cap. 14)

Representación vectorial (*embeddings*).

[http://nlpprogress.com/english/constituency_parsing.html](http://nlpprogress.com/english/constituency_parsing.html)

[http://nlpprogress.com/english/dependency_parsing.html](http://nlpprogress.com/english/constituency_parsing.html)

### Herramientas

- SpaCy: [https://spacy.io/](https://spacy.io/)
- STANZA: [https://stanfordnlp.github.io/stanza/](https://stanfordnlp.github.io/stanza/)
- Freeling: [https://nlp.lsi.upc.edu/freeling/node/1](https://nlp.lsi.upc.edu/freeling/node/1)
- UD-Pipe: [https://ufal.mff.cuni.cz/udpipe](https://ufal.mff.cuni.cz/udpipe)

## Bibliografía

- Abney S.P. (1991) "Parsing By Chunks". In: Berwick R.C., Abney S.P., Tenny C. (eds) Principle-Based Parsing. Studies in Linguistics and Philosophy, vol 44. Springer, Dordrecht. https://doi.org/10.1007/978-94-011-3474-3_10
- Emily M. Bender (2013) *Linguistic Fundamentals for Natural Language Processing. 100 Essentials from Morphology and Syntax*, Synthesis Lectures on Human Language Technologies DOI: <https://doi.org/10.1007/978-3-031-02150-3>
- Steven Bird, Ewan Klein, and Edward Loper (2009) *Natural Language Processing with Python* <https://www.nltk.org/book/>
- Juravsky y Martin (2020) *Speech and Language Processing*. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/)
- Karlsson, F., A. Voutilainen, J. Heikkilä, and A. Anttila (eds.). 1995. _Constraint Grammar. A language-independent system for parsing unrestricted text_. Berlin and New-York: Mouton de Gruyter

---

[^1]: "Token" se asimila en este caso a "occurrence". Cfr. [https://plato.stanford.edu/entries/types-tokens/#Occ](https://plato.stanford.edu/entries/types-tokens/#Occ)

[^3]: Ver [capítulo 3](https://www.nltk.org/book/ch03.html) del libro [*Natural Language Processing with Python*](https://www.nltk.org/book/ch03.html) para una explicación sencialla.

[^4]: Bender (2013) presenta una buena introducción a conceptos lingüísticos de uso común en Procesamiento del Lenguaje Natural.
