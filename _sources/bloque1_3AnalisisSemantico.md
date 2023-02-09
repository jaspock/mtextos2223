(label_Semantica)=
Análisis semántico
==================

Borja Navarro Colorado

```{admonition} Nota
:class: note

Para completar este tema, debe leer el [capítulo 23 "Word Senses and WordNet"](https://web.stanford.edu/~jurafsky/slp3/23.pdf) de Jurafsky y Martin (2023) *Speech and Language Processing*. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/). Los "contextual word embeddings" serán tratados en próximos temas, por lo que puedes hacer una lectura oblicua (es decir, sin entrar en detalles: solo las ideas principales) del apartado 23.4.2, y también desde el apartado 23.5.3 hasta el final.  
```


## La semántica. Tipos de significados.

La semántica estudia significado de los textos. El propio concepto de significado es, sin embargo, bastante vago. En este tema se presenta modelos de representación y procesamiento del significado lingüístico según el estándar actual en PLN: por un lado el significado léxico y por otro el significado oracional.

## Semántica léxica. *Word Sense Disambiguation*.

La semántica léxica se refiere al significado de las palabras.

En PLN hay actualmente dos modelos para tratar la semántica léxica:

- La consideración del sentido de la palabra como una representación discreta, es decir, un conjunto de significados (una o más por palabra) que puede ser representado en un diccionario mediante, por ejemplo, definiciones.
- La consideración del sentido a partir de las relaciones contextuales entre las palabras en su uso comunicativo real. Este es el modelo distribucional en el que se basan los *word embeddings* que veremos en próximos temas.

Este capítulo se centra en el primer modelo.

### Significado léxico como unidad discreta

Según este modelo, por tanto, una palabra puede tener uno o más significados que además podemos especificar en un diccionario. Las palabras que tienen dos o más significados son palabras ambiguas. Se calcula que más del 60% de las palabras de un idioma son ambiguas: basta echar un vistazo a un diccionario para comprobarlo.

En un contexto determinado, esa ambigüedad se reduce, de tal manera que un ser humano al interpretar el texto es capaz de determinar, a partir del conjunto de significado de una palabra, el sentido apropiado para ese contexto.

> mouse1:  .... a mouse controlling a computer system in 1968.

> mouse2:  .... a quiet animal like a mouse

(Ejemplo tomado de [Juravsky y Martin 2020, cap. 18, pág. 2](https://web.stanford.edu/~jurafsky/slp3/18.pdf))

Este es el modelo de semántica léxica que conocemos desde el colegio, en el que ante una palabra desconocida buscamos en el diccionario el significado que mejor se ajusta al contexto.

Que una palabra tenga dos o más significados puede parecer en un principio ilógico. Este hecho se debe a dos fenómenos lingüísticos: la homonimia y la polisemia.

La _homonimia_ se produce cuando dos palabras, en un principio diferentes en significante y significado, han evolucionado de tal manera que sus significantes (es decir, la forma de la palabra, cómo se pronuncia o escribe) se han hecho iguales. Así ocurre por ejemplo con palabras como "bota", que puede ser el odre para beber (la bota de vino), procedente del latín "buttis"; o la bota de calzado, procedente del francés "botte".[^1] Son por tanto dos palabras distintas que, por evolución, ahora se pronuncian igual. Lo característico de la homonimia es que los significados de la palabra suelen ser muy diferentes dado que provienen de palabras diferentes.

La _polisemia_, por su parte, se produce por la evolución del propio significado de una palabra. Dado una palabra, el uso diario puede producir que se genere un nuevo significado. Por ejemplo, mediante procesos de metaforización ("ratón"), metonimia ("pluma"), especificación ("banco entidad" vs. "banco edificio"), etc. Desde un punto de vista computacional, la polisemia suele ser más compleja de procesar, pues esto significados nuevos siempre están relacionados de alguna manera con el significado original. Hay casos que la diferencia en la polisemia es muy sutil.

### *Word Sense Disambiguation*

En PLN, el proceso de seleccionar el significado apropiado de una palabra en un contexto concreto, a partir de los significados establecidos en un diccionario, se denomina *Word Sense Disambiguation* (WSD). Es una de las tareas del PLN con larga tradición, junto al análisis categorial o el análisis sintáctico que vimos en temas anteriores.

Los sistemas de WSD están formados por dos componentes fundamentales: un diccionario en el que se representan todos los significados de las palabras y un algoritmo de desambiguación.

### Representación del significado léxico: WordNet.

En PLN se han desarrollado (y se siguen desarrollando) diversos diccionarios electrónicos. Pero de todos ellos uno ha tenido especial relevancia: [WordNet](https://wordnet.princeton.edu/) (Miller 1995, Fellbau 1998). Hoy día sigue siendo el principal recurso léxico utilizado hoy día en PLN. En su origen fue un diccionario para el inglés, pero luego fue ampliado a lenguas europeas (EuroWordNet) y otras familias lingüísticas (balkanet, arabic wordnet, etc.) y más tarde a todas las lenguas del mundo.[^2]

WordNet en inglés se puede consultar desde la [página oficial](http://wordnetweb.princeton.edu/perl/webwn). WordNet en otros idiomas se puede consultar desde el [proyecto Open Multilingual WordNet](http://compling.hss.ntu.edu.sg/omw/cgi-bin/wn-gridx.cgi?gridmode=grid).

Las características principales de WordNet, que están presentes en el resto de proyectos, son:

- WordNet se define como una red de sentidos: la unidad básica (cada nodo de la red) es el sentido. Esto lo diferencia del diccionario tradicional y del manual, en el que la unidad principal es la palabra y no el sentido.
- Cada sentido se representa mediante el conjunto de palabras sinónimas en un idioma, denominado "synset" (*set of synonyms*).
- Cada *synset*, además del conjunto de sinónimos, dispone de información léxica como: un ID único de sentido, ejemplos de uso del sentido en oraciones reales, glosas o definiciones, dominio semántico en el que se utiliza, etc. Excepto el ID (que es único porque identifica el nodo en la red), el resto de información es opcional.
- La red se forma a partir de relaciones léxicas entre sentidos. La principal relación léxica es la sinonimia en la que se basa la idea del *synset*. Aparte de esto hay otras según la categoría gramatical de las palabras.
- Entre nombres, las relaciones principales son hiperonimia (relación tipo "is_a"), hiponimia (la inversa del "is_a") y meronimia (o relación "parte_de").
- Para los adjetivos, la relaciones principales son la antonimia y "similar a".
- Para los verbos, las principales relaciones son la "pseudo-hiperonimia" (relación "is_a" similar a la de los nombres, pero es "pseudo" porque la hiperonimia en sentido estricto solo es aplicable a relaciones nominales, no a acciones) y la troponima (la manera de realizar una acción. Por ejemplo "pasear" es una forma de "andar", por lo que entre "pasear" y "andar" se establece una relación de troponimia).

En las últimas versiones se pueden encontrar otros tipos de relaciones. Dado que los sentidos de nombres se relacionan sobre todo con relaciones tipo "is_a", en WordNet se han determinado unos nodos raíz con sentidos nominales muy abstractos (como "entidad") de las cuales van derivando por relación léxica de hiperonimia/hiponima el resto de sentidos hasta los sentidos más concretos.

En su concepción original, WordNet pretendía ser una representación computacional del lexicón mental humano. Finalmente se ha convertido en quizá el principal recurso para el análisis léxico-semántico. Hasta el desarrollo de los *word embeddings*, WordNet era (y aún es) el estándar *de facto* para la representación del significado de las palabras de un corpus.

### Algoritmos de desambiguación léxico-semántica.

En al tarea de WSD se asume que los posibles significados de una palabra son únicamente aquellos establecidos en un diccionario (WordNet en este caso). No se plantean otras formas de significación como la metáfora o sentido novedosos. El objetivo de un sistema de WSD es, así, determinar, de los posibles *synsets* asociados a una palabra (solo nombres, verbos o adjetivos), cuál es el apropiado en un contexto dado.

La heurística básica es seleccionar siempre el sentido más frecuente. Esto ya da buenos resutlados. Pero no es suficiente. En los últimos 30 años se han propuesto diferentes algoritmos para mejorar este *baseline*. Las diferentes propuestas se pueden agrupar, en general, en dos aproximaciones básicas: algoritmos basados en conocimiento y algoritmos basados en aprendizaje supervisado.

#### Estrategias basadas en conocimiento

Las estrategias basadas en conocimiento (*knowledge-based*) se caracterizan por explotar al máximo la información del recurso léxico (WordNet). Esta se compara con el contexto donde aparece la palabra ambigua hasta hallar el significado más coherente.

El algoritmo de Lesk (Lesk 1986) es el método estándar de desambiguación basando en conocimiento. Para determinar el sentido apropiado de una palabra ambigua, compara las palabras del contexto donde aparece con la definición de cada sentido (la “glosa” en WordNet). Finalmente selecciona como sentido apropiado aquél cuya definición tiene más coincidencias con el contexto.

Por ejemplo, en la siguiente oración, la glosa 1 sería la más apropiada para "banco":

> "Ingresé el _dinero_ en el *banco* ayer tarde"
>1. Entidad financiera que acepta _dinero_ en depósito y ofrece préstamos con intereses.
>2. Asiento largo y estrecho para varias personas

Siempre y cuando se disponga de una buena definición, este algoritmo funciona bien para casos de homonimia. Para casos de polisemia, en los que las diferencias semánticas entre significados son más sutiles, no suele funcionar tan bien.

Existen diferentes implementaciones de este algoritmo, como por ejemplo la disponible en el [*Natural Language Toolkit*](https://www.nltk.org/howto/wordnet.html) (NLTK) (Bird et al. 2009), pero solo funciona para inglés.

En esta línea, el algoritmo UKB (Agirre y Soroa 2009, Padró et al. 2010) es un aproximación mucho más avanzada. El algoritmo es una adaptación del algoritmo Page Rank de Google. La idea principal de éste es que no todos los nodos de un grafo son iguales, sino que unos tienen más importancia que otros. Un nodo es importante si otros nodos apuntan a él, y si un nodo importante apunta a otro, este también se considera relativamente importante. Sin entrar en detalles técnicos, este algoritmo determina la pertinencia de un sentido en un contexto mediante las relaciones léxicas de cada palabra dentro de WordNet. Dada una palabra ambigua, aquel *synset* cuyas relaciones de hiperonimia, etc. mejor encaje con el resto de sentidos del contexto, será el apropiado (Agirre y Soroa 2009). Este es el algoritmo implementado en [Freeling](http://nlp.lsi.upc.edu/freeling/).

#### Estrategias basadas en aprendizaje supervisado

Estas estrategias (*features-based algorithms*) se caracterizan por aprender diferentes rasgos del contexto de las palabras con técnicas de *machine learning* y utilizarlos para clasificar usos ambiguos.

Por ejemplo, una estrategia óptima sería entrenar un clasificador _Support Vector Machines_ (que ha dado buenos resultados en WSD) con rasgos de aprendizaje como pudieran ser las categorías gramaticales de las tres palabras anteriores, n-gramas de las palabras alrededor de la palabra ambigua, o un vector contextual a partir de los vectores incrustados (*embedings*) de cada palabra del contexto (Ver Jurafki y Martin (2023), cap. 23, pág. 12).

Existen diferentes corpus anotados con sentidos desambiguados. El primero corpus anotado con sentido, que estableció el modelo a partir del cual se han desarrollado otros, fue SemCor, con texto en inglés. Este corpus se creó al mismo tiempo que WordNet y por los mismos desarrolladores. En SemCor, cada palabra tiene asignado el *synset* específico en WordNet. Y muchos sentidos de WordNet se han determinado a partir de los textos de SemCor. SemCor está disponible en diferentes páginas (como [esta](http://www.gabormelli.com/RKB/SemCor_Corpus) y [esta](http://web.eecs.umich.edu/~mihalcea/downloads.html#semcor)), así como en [Kaggle](https://www.kaggle.com/nltkdata/semcor-corpus) o [NLTK](https://www.nltk.org/_modules/nltk/corpus/reader/semcor.html).

A partir de SemCor se crearon corpus similares para otros idiomas. Para español se creó el corpus Cast3LB, hoy enriquecido con más información y renombrado como [Ancora Corpus](http://clic.ub.edu/corpus/es/ancora).

La línea de trabajo actual es aplicar *word embeddings* a la tarea de WSD. Un recurso muy utilizado es [Nasari](http://lcl.uniroma1.it/nasari/), que incluye representaciones vectoriales de los *synsets* de WordNet y de la Wikipedia (ambos integrados en el recurso BabelNet).

#### Inducción de sentidos

Junto a estas dos estrategias, hay una tercera basada en técnicas no supervisadas. En este caso, sin embargo, como no hay un recursos léxico de referencia con los sentidos, los sistemas no determinan significados sino que agrupan oraciones. Así, dado un conjunto de oraciones con una palabra ambigua en común, agrupan las oraciones en las que esa palabra se utiliza con un sentido determinado. Lo que no pueden determinar es cuál es ese sentido. Por ello se considera una tarea de inducción de sentidos, más que de desambiguación propiamente dicha.

En esta tareas se suelen aplicar modelos de semántica vectorial que se verán en la próxima sección.

### Situación actual

La desambiguación de sentido sigue siendo hoy una tarea abierta en PLN, ya que determinar el sentido exacto puede llegar a ser muy complejo. Además de la propia selección del sentido, entran en juego otros factores como la denotación o la metaforización. Algunos de las últimas propuestas se pueden ver aquí:

- [http://nlpprogress.com/english/word_sense_disambiguation.html](http://nlpprogress.com/english/word_sense_disambiguation.html)

```{admonition} Actividad
:class: note
Para probar la anotación de sentidos con WordNet, puedes utilizar la herramienta [NLTK](https://www.nltk.org/). Haz ahora la ampliación 2 de la práctica 1, donde verás cómo acceder a WordNet a través de SpaCy y desambiguar así el significado de las palabras.
```

## Semántica oracional. Roles semánticos y semántica eventiva.

Los sistemas de WSD se centran únicamente en determinar el significado de las palabras. Sin embargo, el significado global de un texto no solo depende del significado de las palabras que lo forma, sino también de las relaciones que se establecen entre ellas tanto en la oración como en la globalidad del texto. De aquí se establece el __principio de composicionalidad__, según el cual el significado global de una oración esta en función del significado de sus partes (las palabras) y las relaciones (sintácticas y semánticas) que se establecen entre ellas.

Así, la semántica oracional se centra en estudiar el significado de la oración en su conjunto. Dentro del PLN hay diferentes aproximaciones a la semántica oracional, de las que destaca sobre todo el análisis de __roles semánticos__ (Gildea y Jurafsky 2002). Ésta se enmarcan dentro de la __semántica eventiva__ (o semántica de eventos), cuyo objetivo es determinar los eventos (hechos que se producen en el mundo real) y estados expresados en un texto junto con sus participantes y las relaciones entre ellos. Dada, por ejemplo, una oración, el evento suele venir expresado por el verbo y los participantes por sus argumentos. Los roles semánticos representan la relación semántica de esos argumentos con el sentido verbal dentro del marco eventivo (Levin et al. 2005).

Por ejemplo, la oración:

> “Las fuerzas de seguridad persiguieron a los agresores”

expresa el evento “perseguir” que tiene una estructura argumental formada por la persona que persigue (“las fuerzas de seguridad”) y la persona perseguida (“los agresores”). El primer argumento se podría considerar como rol “agente” y el segundo como rol “tema”.

El evento puede estar expresado por verbo ("luchar") pero también por un nombre ("la guerra"). Los argumentos son los sintagmas que completan el significado del evento. La función semántica que pueden asumir los argumento es lo que se denomina "roles semánticos": agente, tema, paciente, instrumentante, etc.

### Representación formal de los roles semánticos.

La teoría de los roles semánticos proviene de la Teoría de Casos de Ch. Fillmore y ha tenido diferentes desarrollos en lingüística teórica. El problema principal que tienen estas teorías es que, por un lado, no se ha podido consensuar una única lista de roles semánticos y, por otro, no hay una clara distinción entre los roles. Así, al hablar de roles semánticos nos podemos encontrar roles como _agente_ (el argumento que realiza el evento), _paciente_ o _tema_ (el argumento sobre el que actúa el evento), experimentante, proto-agente, proto-paciente (ambos generalizaciones de agente y paciente), etc.

Esta falta de definición ha propiciado el desarrollo de dos modelos de representación de roles semántico en lingüística computacional: el modelo de FrameNet y el modelo de PropBank.

#### FrameNet

[FrameNet](https://framenet.icsi.berkeley.edu/fndrupal/) (Baker et al. 1998, Ruppenhofer et al. 2016) propone una representación de roles semánticos muy fina: indica roles específicos para unidades léxicas concretas. Estas unidades pueden ser verbos, nombres o adjetivos. Cada uno de sus sentidos se agrupa en un marco semántico, entendido como un marco estructural conceptual (*frame*) que describe una situación, un objeto o un evento concreto más sus participantes: los roles semánticos asociados a ese marco (*frame elements*).

Por ejemplo, la unidad léxica “comer” pertenece al marco semántico *Ingestion*. En este marco semántico se han definido hasta siete elementos o roles, entre los que se encuentran:

- *ingestor* (“comensal”),
- *ingestibles* (“comida” u “objetos digeribles”),
- *place* (“lugar” donde se come),
- *manner* (“manera” de comer)
- o *degree* (“cantidad”).

> [_Ingestor Alba] aprendió a COMER_Target [_Ingestibles verduras hervidas y arroz quemado]

En general, hay tres tipos de *frame elements*:

1. *core*: aquellos que son específicos del evento y conceptualmente necesarios para que el marco tenga sentido completo;
2. *peripherical*: aquellos que aportan información importante para completar el marco semántico pero que no son centrales para que éste tenga sentido completo; y
3. *extra-thematic*: aquellos que amplían el contexto semántico del marco.

En el caso del marco *Ingestion*, los dos elementos *core* son *ingestor* e *ingestibles*; elementos periféricos son *instrument* o *source*, y el resto actuarían como extra-temáticos.

```{admonition} Actividad
:class: note
Consulta este y otros *frame elements* en la base de datos de FrameNET:

[https://framenet.icsi.berkeley.edu/fndrupal/luIndex](https://framenet.icsi.berkeley.edu/fndrupal/luIndex)

```

#### PropBank

La propuesta de PropBank (acrónimo de *Proposition Bank* (Palmer et al. 2005)) es justo la contraria. En vez de definir roles semánticos muy específicos según el evento, ProBank determina poco roles y muy generales, de tal manera que sean aplicable a cualquier evento. Y en vez de dar a los roles un nombre significativo, representa cada rol con un simple identificador. Así, de manera general se establece que puede haber hasta cinco roles semánticos asociados a un evento:

    Arg0 | Arg1 | Arg2 | Arg3 | Arg4

y además se establece un número indefinido de adjuntos:

    ArgM

Cada rol se define por su relación con el verbo. Los dos argumentos que tienen una relación más estrecha con el sentido del verbo son _Arg0_ y _Arg1_. Para verbos transitivos, por ejemplo, el primero se suele identificar con el rol Agente y el segundo con el rol Tema/Paciente, pero esta relación no siempre se cumple.

Lo importante es que la alternancia de diátesis no afecte a los roles. Así, independientemente de que la estructura verbal se exprese en activa o en pasiva, los roles Arg0 y Arg1 serán los mismos, como en el siguiente ejemplo:

> [Arg0 La policía militar] arrestó [Arg1 a tres personas]
> [Arg1 Tres personas] fueron arrestadas [Arg0 por la policía militar]

En este caso es la misma oración, una en forma activa y la otra en forma pasiva. Independientemente del sintagma y la función sintáctica de cada argumento en cada oración, su rol semántico es el mismo. Así, en el primer caso Arg0 es el sujeto, mientras que en el segundo caso Arg0 es un complemento agente y Arg1 el sujeto.

Este modelo ha sido adaptado al español en el [corpus AnCora](http://clic.ub.edu/corpus/es/ancora) (Taulé et al. 2008), que también incluye anotación de textos en catalán (AnCora-Es y AnCora-Cat respectivamente).

De ambas propuestas de representación de roles semánticos, la más utilizada hoy día en PLN es la propuesta de PropBank.

```{admonition} Actividad
:class: note
Consulta los roles de PropBank en su bas de datos unificada (*Unified Verb Index*):

[https://verbs.colorado.edu/verb-index/vn3.3/](https://verbs.colorado.edu/verb-index/vn3.3/)

```

Puedes obtener más información sobre PropBank desde la [página del proyecto](https://propbank.github.io/). Está ademas disponible para su descarga aquí: [https://github.com/propbank/propbank-frames/](https://github.com/propbank/propbank-frames/).
 

### Algoritmos

Los sistema de análisis de roles semánticos (*semantic role labeling*) toman como entrada un corpus anotado con categorías gramaticales y (en algunos casos, pero no siempre) con relaciones sintácticas. La salida es la especificación de qué elemento de la oración expresa el evento, qué palabras se agrupan en cada argumento y el tipo de argumento.

Los principales algoritmos de *semantic roles labeling* (SRL) suelen estar basados en __técnicas de aprendizaje supervisado__. A partir de corpus anotados con roles (como el propio corpus [PropBank](https://propbank.github.io/)), se establecen una serie de rasgos de aprendizaje que se utilizan luego para clasificar por tipos de roles semánticos.

El algoritmo estándar de SRL es el de Gildea y Jurafsky (2002). Este sistema primero aprende de un corpus anotado qué elementos son los roles semánticos y de qué tipo son, junto a una serie de rasgos lingüísticos. Entre los rasgos utilizados está el verbo que rige la estructura argumental, los tipos de sintagma de los argumentos, la categoría gramatical de las palabras de cada argumento, los lemas de las palabras, etc. Es decir, tanto información categorial como sintáctica. Durante el proceso de análisis de un nuevo corpus, el algoritmo tratará de determinar los roles semánticos de una oración a partir de estos rasgos.

La herramienta Freeling cuenta con un sistema de SRL similar a este para español y otros idiomas. En el caso del español está entrenado con el [corpus AnCora](http://clic.ub.edu/corpus/es/ancora) y entre los rasgos de aprendizaje utiliza, además de los establecidos en Gildea y Jurafsky (2002), otros como las relaciones de dependencia o la voz verbal (Lluís et al. 2013).

### Situación actual

Los sistemas actuales, como en el resto de tareas, están basados en vectores y *word embeddings*:

[http://nlpprogress.com/english/semantic_role_labeling.html](http://nlpprogress.com/english/semantic_role_labeling.html)

También hay interés en sistemas multi- y cross-lingües:

[https://www.aclweb.org/anthology/2020.acl-main.627/](https://www.aclweb.org/anthology/2020.acl-main.627/)

## Otros tipos de análisis.

El análisis semántico oracional no se agota con los roles semánticos. Hay más propuestas, como el *Abstract Meaning Representation* o las dependencias semánticas:

[http://nlpprogress.com/english/semantic_parsing.html](http://nlpprogress.com/english/semantic_parsing.html)

En la base de todas ellas está la semántica léxica y los roles semánticos aquí expuestos. Puede completar esta sección con la lectura (**opcional**) del [capítulo 24](https://web.stanford.edu/~jurafsky/slp3/24.pdf) del libro de Jurafsky y Martin (2023).

## Bibliografía

Fellbau, C. (ed) 1998. *WordNet: An Electronic Lexical Database*. Cambridge, MA: MIT Press.

Juravsky y Martin (2020) *Speech and Language Processing*. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/) (Caps 18-19)

Miller, G. A. 1995. “WordNet: A Lexical Database for English”. *Communications of the ACM*, 38(11), 39-41.

Navarro Colorado, Borja (2021) "Sistemas de anotación semántica para corpus de español" en Giovanni Parodi, Pascual Cantos & Lewis Howe (Editores) *The Routledge Handbook of Spanish Corpus Linguistics* Routledge.

[^1]: Ver <http://www.wikilengua.org/index.php/Homonimia>

[^2]: Ver [GlobalWordNet](http://globalwordnet.org/) y el [Open Multilingual Wordnet](http://compling.hss.ntu.edu.sg/omw/).
