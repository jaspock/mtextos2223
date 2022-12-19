(label_Semantica)=
Análisis semántico
==================

```{admonition} Nota
:class: note
Para preparar este tema, consulta los capítulos 18 y 19 de Juravsky y Martin (2020) *Speech and Language Processing*. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/).
```


## La semántica. Tipos de significados.

La semántica estudia significado de los textos. El propio concepto de significado es, sin embargo, bastante vago. En este tema se presenta modelos de representación y procesamiento del significado lingüístico según el estándar actual en PLN: por un lado el significado léxico y el significado oracional por otro.

## Semántica léxica. *Word Sense Disambiguation*.

La semántica léxica se refiere al significado de las palabras.

En PLN hay actualmente dos modelos para tratar la semántica léxica:

- La consideración del sentido de la palabra como una representación discreta, es decir, un conjunto de definiciones (una o más) en un diccionario.
- La consideración del sentido a partir de las relaciones contextuales (distribucionales) entre las palabras en su uso real (en un corpus, por ejemplo). Este modelo es la base de la semántica vectorial, de la cual surgen los *word embeddings* que se verán en el próximo tema.

Este capítulo se centra en el primer modelo.

### Significado léxico como unidad discreta

Según este modelo, por tanto, una palabra puede tener uno o más significados que además podemos especificar en un diccionario. Las palabras que tienen dos o más significados son palabras ambiguas. Se calcula que más del 60% de las palabras de un idioma son ambiguas: basta echar un vistazo a un diccionario para comprobarlo. En un contexto determinado, esa ambigüedad se reduce, de tal manera que un ser humano al interpretar el texto es capaz de determinar, a partir del conjunto de significado de una palabra, el sentido apropiado para ese contexto.

> mouse1:  .... a mouse controlling a computer system in 1968.

> mouse2:  .... a quiet animal like a mouse

(Ejemplo tomado de [Juravsky y Martin 2020, cap. 18, pág. 2](https://web.stanford.edu/~jurafsky/slp3/18.pdf))

Este es el modelo de semántica léxica que conocemos desde el colegio, en el que nos pedían buscar palabras en un diccionario y determinar cuál era el significado apropiado según el texto.

Que una palabra tenga dos o más significados puede parecer en un principio ilógico. Este hecho se debe a dos fenómenos lingüísticos: la homonimia y la polisemia.

La _homonimia_ se produce cuando dos palabras, en un principio diferentes en significante y significado, han evolucionado de tal manera que sus significantes (es decir, la forma de la palabra, cómo se pronuncia o escribe) se han hecho iguales.

Así ocurre por ejemplo con palabras como "bota", que puede ser el odre para beber (la bota de vino), procedente del latín "buttis"; o la bota de calzado, procedente del francés ("botte") (Ejemplo tomado de la [Wikilengua](http://www.wikilengua.org/index.php/Homonimia)).

Son por tanto dos palabras distintas que, por evolución, ahora se pronuncian igual. Las diferencias semánticas en los casos de homonimia son muy grandes por ser palabras diferentes.

La _polisemia_ se produce por la evolución del propio significado de una palabra. Dado una palabra, el uso diario puede producir que genere un nuevo significado por procesos de metaforización ("ratón"), metonimia ("pluma"), especificación ("banco entidad" vs. "banco edificio"), etc.

Desde un punto de vista computacional, la polisemia es más compleja de procesar, pues esto significados nuevos siempre están relacionados con el significado original. Hay casos que la diferencia en la polisemia es muy sutil.

### *Word Sense Disambiguation*

En PLN, este proceso de seleccionar el significado apropiado para un contexto a partir de los significados establecidos en un diccionario se denomina *Word Sense Disambiguation* (WSD). Es una de las tareas del PLN con más tradición, junto al análisis categorial o el análisis sintáctico que vimos en temas anteriores.

Los sistemas de WSD están formados por dos componentes fundamentales: un diccionario en el que se representan todos los significados de las palabras y un algoritmo de desambiguación.

### Representación del significado léxico: WordNet.

[WordNet](https://wordnet.princeton.edu/) (Miller 1995,
Fellbau 1998) es el principal recurso léxico (diccionario) utilizado hoy día en PLN. En su origen fue un diccionario para el inglés, pero luego fue ampliado a lenguas europeas (EuroWordNet) y otras familias lingüísticas (balkanet, arabic wordnet, etc.) y más tarde a todas las lenguas del mundo ([GlobalWordNet](http://globalwordnet.org/)) Ver también el [Open Multilingual Wordnet](http://compling.hss.ntu.edu.sg/omw/).

WordNet en inglés se puede consultar desde la [página oficial](http://wordnetweb.princeton.edu/perl/webwn).

WordNet en otros idiomas se puede consultar desde el [proyecto Open Multilingual WordNet](http://compling.hss.ntu.edu.sg/omw/cgi-bin/wn-gridx.cgi?gridmode=grid).

Las características principales de WordNet, que están presentes en el resto de proyectos, son:

- WordNet es una red de sentidos. La unidad básica (cada nodo) es el sentido (y no la palabra como los diccionarios manuales).
- Cada sentido se representa mediante el conjunto de palabras sinónimas en un idioma, denominado "*synset*".
- Cada *synset*, además del conjunto de sinónimos, dispon de de información léxica como un ID único de sentido, ejemplos, glosas (definiciones), conceptos de dominio, etc. Excepto el ID, el resto de información es opcional.
- La red se forma a partir de relaciones léxicas. La principal relación léxia es la sinonimia.
- Entre nombres, las relaciones principales son hiperonimia ("is_a"), hiponimia (inversa de "is_a") y meronimia ("parte_de").
- Para los adjetivos, la relaciones principales son la antonimia y "similar a".
- Para los verbos, las principales relaciones son la "pseudo-hiperonimia" (en sentido estricto, esta relación solo es aplicable a nombres) y la troponima (manera).

En las últimas versiones se pueden encontrar otros tipos de relaciones.

Así, WordNet tiene unos nodos raíz con sentidos muy abstractos ("entidad") de las cuales van derivando por relación léxica el resto de sentidos hasta los más concretos.

En su concepción original, WordNet pretendía ser una representación computacional del lexicón humano. Finalmente se ha convertido en quizá el principal recurso para el análisis léxico-semántico. WordNet es el estándar *de facto* para la representación semántica léxica de un corpus.

### Algoritmos de desambiguación léxico-semántica.

WSD asume que los significados de una palabra son únicamente aquellos establecidos en un diccionario (WordNet en este caso). No se plantean otras formas de significación como la metáfora.

La complejidad es WSD es determinar, de los posibles synsets asociados a una palabra (nombre, verbo o adjetivo), cuál es el apropiado en un contexto dado. La heurística básica es seleccionar el sentido más frecuente.

En los últimos 30 años se han propuesto diferentes algoritmos. En general, hay dos aproximaciones básicas: algoritmos basados en conocimiento y algoritmos basados en aprendizaje supervisado.

#### Estrategias basadas en conocimiento

Las estrategias basadas en conocimiento (*knowledge-based*) se caracterizan por explotar al máximo la información del recurso léxico (normalmente WordNet) y su comparación con el contexto donde aparece la palabra ambigua.

El algoritmo de Lesk (Lesk 1986) es el método estándar de desambiguación basando en conocimiento. Para determinar el sentido apropiado de una palabra ambigua, compara las palabras del contexto donde aparece con la definición de cada sentido (la “glosa” en WordNet). Finalmente selecciona como sentido apropiado aquél cuya definición tiene más coincidencias con el contexto.

Por ejemplo, según este uso de "banco", quedaría claro que el sentido apropiado es el primero:

> "Ingresé el _dinero_ en el *banco* ayer tarde"
>1. Entidad financiera que acepta _dinero_ en depósito y
ofrece préstamos con intereses.
>2. Asiento largo y estrecho para varias personas

Así, siempre y cuando se disponga de una buena definición, este algoritmo funciona bien para casos de homonimia, pero no tanto para casos de polisemia.

Existen diferentes implementaciones de este algoritmo, como por ejemplo
la disponible en el [*Natural Language Toolkit*](https://www.nltk.org/howto/wordnet.html) (NLTK) (Bird et al. 2009), pero solo funciona para inglés.

En esta línea, el algoritmo UKB (Agirre y Soroa 2009, Padró et al. 2010) es un aproximación mucho más avanzada. El algoritmo es una adaptación del algoritmo Page Rank de Google. La idea principal de éste es que no todos los nodos de un grafo son iguales, sino que unos tienen más importancia que otros. Un nodo es importante si otros nodos apuntan a él, y si un nodo importante apunta a otro, este también se considera relativamente importante. Sin entrar en detalles técnicos, este algoritmo determina la pertinencia de un sentido en un contexto mediante las relaciones léxicas de cada palabra dentro de WordNet. Dada una palabra ambigua, aquel synset cuyas relaciones de hiperonimia, etc. mejor encaje con el resto de sentidos del contexto, será el apropiado (Agirre y Soroa 2009). Este es el algoritmo implementado en [Freeling](http://nlp.lsi.upc.edu/freeling/).

#### Estrategias basadas en aprendizaje supervisado

Estas estrategias (*features-based algorithms*) se caracterizan por aprender diferentes rasgos del contexto de las palabras y utilizarlos para clasificar usos ambiguos.

Por ejemplo, una estrategia óptima sería crear un clasificador basado en SVM con rasgos de aprendizaje como pudieran ser las categorías gramaticales de las tres palabras anteriores, n-gramas de las palabras alrededor de la palabra ambigua, o un vector contextual a partir de los vectores incrustados (*embedings*) de cada palabra del contexto (Juravki y Martin, cap. 18, pág. 12).

Existen diferentes corpus anotados con sentidos desambiguados. El primero en ser desarrollado fue SemCor, con texto en inglés. Este corpus es el modelo a partir del cual se han desarrollado otros. El corpus se creó al mismo tiempo que WordNet y por las mismas personas. En SemCor, cada palabra tiene asignado el *synset* específico en WordNet. Y muchos sentidos de WordNet se han determinado a partir de los textos de SemCor. SemCor está disponible en diferentes páginas (como [esta](http://www.gabormelli.com/RKB/SemCor_Corpus) y [esta](http://web.eecs.umich.edu/~mihalcea/downloads.html#semcor)), así como en [Kaggle](https://www.kaggle.com/nltkdata/semcor-corpus) o [NLTK](https://www.nltk.org/_modules/nltk/corpus/reader/semcor.html).

Corpus similares a SemCor para otros idiomas. Para español se creó el corpus Cast3LB, hoy enriquecido con más información y renombrado como [Ancora Corpus](http://clic.ub.edu/corpus/es/ancora).

La línea de trabajo acutal es aplicar *word embeddings* a la tarea de WSD. Un recurso muy utilizado es [Nasari](http://lcl.uniroma1.it/nasari/), que incluye representaciones vectoriales de los *synsets* de WordNet y de la Wikipedia (ambos integrados en el recurso BabelNet).

#### Inducción de sentidos

Junto a estas dos estrategias, hay una tercera basada en técnicas no supervisadas. En este caso, sin embargo, como no hay un recursos léxico de referencia con los sentidos, los sistemas no determinan significados sino que agrupan oraciones. Así, dado un conjunto de oraciones con una palabra ambigua en común, agrupan las oraciones en las que esa palabra se utiliza con un sentido determinado. Lo que no pueden determinar es cuál es ese sentido.

En esta tareas se suelen aplicar modelos de semántica vectorial que se verán en la próxima sesión.


La desambiguación de sentido sigue siendo hoy una tarea abierta en PLN. Algunos de las últimas propuestas se pueden ver aquí:

- [http://nlpprogress.com/english/word_sense_disambiguation.html](http://nlpprogress.com/english/word_sense_disambiguation.html)

```{admonition} Actividad
:class: note
Para probar la anotación de sentidos con WordNet, puedes utilizar NLTK. Prueba a hacer la ampliación 2 de la práctica 1.
```

## Semántica oracional. Roles semánticos y semántica eventiva.

Los sistemas de WSD se centran únicamente en determinar el significado de las palabras. Sin embargo, el significado global de un texto no solo depende del significado de las palabras que lo forma, sino también de las relaciones que se establecen entre ellas tanto en la oración como en la globalidad del texto (__principio de composicionalidad__).

Así, la semántica oracional se centra en estudiar el significado de la oración en su conjunto. Dentro del PLN hay diferentes aproximaciones a la semántica oracional, de las que destaca sobre todo el análisis de __roles semánticos__ (Gildea y Jurafsky 2002).

Los roles semánticos se enmarcan dentro de la __semántica eventiva__ (o semántica de eventos). El objeto de esta aproximación semántica es determinar los eventos y estados expresados en un texto junto con sus participantes y las relaciones entre ellos.

Dada, por ejemplo, una oración, el evento suele venir expresado por el verbo y los participantes por sus argumentos. Los roles semánticos representan la relación semántica de esos argumentos con el sentido verbal dentro del marco eventivo (Levin et al. 2005).

Por ejemplo, la oración

>“Las fuerzas de seguridad persiguieron a los agresores”

expresa el evento “perseguir” que tiene una estructura argumental formada por la persona que persigue (“las fuerzas de seguridad”) y la persona perseguida (“los agresores”). El primer argumento se podría considerar como rol “agente” y el segundo como rol “tema”.

El evento puede estar expresado por verbo ("luchar") pero también por un nombre ("la guerra"). Los argumentos son los sintagmas que completan el significado del evento. La función semántica que pueden asumir los argumento es lo que se denomina "roles semánticos".

### Representación formal de los roles semánticos.

La teoría de los roles semánticos proviene de la Teoría de Casos de Ch. Fillmore y ha tenido diferentes desarrollos en lingüística teórica. El problema principal que tienen estas teorías es que, por un lado, no se ha podido consensuar una única lista de roles semánticos y, por otro, no hay una clara distinción entre los roles. Así, al hablar de roles semánticos nos podemos encontrar roles como _agente_ (el argumento que realiza el evento), _paciente_ o _tema_ (el argumento sobre el que actúa el evento), experimentante, proto-agente, proto-paciente (ambos generalizaciones de agente y paciente), etc.

Esta falta de definición ha propiciado el desarrollo de dos modelos de representación de roles semántico en lingüística computacional: el modelo de FrameNet y el modelo de PropBank.

#### FrameNet

FrameNet (Baker et al. 1998, Ruppenhofer et al. 2016) propone una representación de roles semánticos muy fina: indica roles específicos para unidades léxicas concretas. Estas unidades pueden ser verbos, nombres o adjetivos. Cada uno de sus sentidos se agrupa en un marco semántico, entendido como un marco estructural conceptual (*frame*) que describe una situación, un objeto o un evento concreto más sus participantes: los roles semánticos asociados a ese marco (*frame elements*).

Por ejemplo, la unidad léxica “comer” pertenece al marco semántico *Ingestion*. En este marco semántico se han definido hasta siete elementos, entre los que se encuentran:

- *ingestor* (“comensal”),
- *ingestibles* (“comida” o “digeribles”),
- *place* (“lugar” donde se come),
- *manner* (“manera” de comer)
- o *degree* (“cantidad”).

    [_Ingestor Alba] aprendió a COMER_Target [_Ingestibles verduras hervidas y arroz quemado]

En general, hay tres tipos de *frame elements*:

1. *core*: aquellos que son específicos del evento y conceptualmente necesarios para que el marco tenga sentido completo;
2. *peripherical*: aquellos que aportan información importante para completar el marco semántico pero que no son centrales para que éste tenga sentido completo; y
3. *extra-thematic*: aquellos que amplían el contexto semántico del marco.

En el caso del marco *Ingestion*, los dos elementos *core* son *ingestor* e *ingestibles*; elementos periféricos son *instrument* o *source*, y el resto actuarían como extra-temáticos.

```{admonition} Actividad
:class: note
Consulta este y otros *frame elements* en la BD de FrameNET:

[https://framenet.icsi.berkeley.edu/fndrupal/](https://framenet.icsi.berkeley.edu/fndrupal/)

```


#### PropBank

La propuesta de PropBank (acrónimo de *Proposition Bank* (Palmer et al. 2005)) es justo la contraria. En vez de definir roles semánticos muy específicos según el evento, ProBank determina poco roles y muy generales, de tal manera que sean aplicable a cualquier evento. En vez de dar a los roles un nombre significativo, representa cada rol con un identificador. Así, de manera general se establece que puede haber hasta cinco roles semánticos asociados a un evento:

    Arg0 | Arg1 | Arg2 | Arg3 | Arg4

y además se establece un número indefinido de adjuntos:

    ArgM

Cada rol se define por su relación con el verbo. Los dos argumentos que tienen una relación más estrecha con el sentido del verbo son _Arg0_ y _Arg1_. Para verbos transitivos, por ejemplo, el primero se suele identificar con el rol Agente y el segundo con el rol Tema/Paciente, pero esta relación no siempre se cumple.

Lo importante es que la alternancia de diátesis no afecte a los roles. Así, independientemente de que la estructura verbal se exprese en activa o en pasiva, los roles Arg0 y Arg1 serán los mismos:

    [Arg0 La policía militar] arrestó [Arg1 a tres personas]
    [Arg1 Tres personas] fueron arrestadas [Arg0 por la policía militar]

Este modelo ha sido adaptado al español en el [corpus AnCora](http://clic.ub.edu/corpus/es/ancora) (Taulé et al. 2008), que también incluye anotación de textos en catalán (AnCora-Es y AnCora-Cat respectivamente).

De ambas propuestas de representación de roles semánticos, la más utilizada hoy día en PLN es la propuesta de PropBank.

```{admonition} Actividad
:class: note
Consulta los roles de PropBank en su BD unificada (*Unified Verb Index*):

[https://verbs.colorado.edu/verb-index/vn3.3/](https://verbs.colorado.edu/verb-index/vn3.3/)

```

- Para descargar PropBank: [https://github.com/propbank/propbank-frames/](https://github.com/propbank/propbank-frames/)
- Página del proyecto: [https://propbank.github.io/](https://propbank.github.io/)

### Algoritmos

Los sistema de análisis de roles semánticos (*semantic role labeling*) toman como entrada un corpus anotado con categorías gramaticales y (en algunos casos, pero no siempre) con relaciones sintácticas. La salida es la especificación de qué elemento expresa el evento, qué palabras se agrupan en cada argumento y el tipo de argumento.

Los principales algoritmos de *semantic roles labeling* suelen estar basados en __técnicas de aprendizaje supervisado__. A partir de corpus anotados con roles (como el propio corpus [PropBank](https://propbank.github.io/)), se establecen una serie de rasgos de aprendizaje que se utilizan luego para clasificar por tipos de roles semánticos.

El algoritmo estándar de SRL es el de Gildea y Jurafsky (2002). Este sistema primero aprende de un corpus anotado qué elementos son los roles semánticos y de qué tipo son, junto a una serie de rasgos lingüísticos. Entre los
rasgos utilizados está el verbo que rige la estructura argumental, los tipos de sintagma de los argumentos, la categoría gramatical de las palabras de cada argumento, los lemas de las palabras, etc. Es decir, tanto información categorial como sintáctica. Durante el proceso de análisis de un nuevo corpus, el algoritmo tratará de determinar los roles semánticos de una oración a
partir de estos rasgos.

El modelo de Freeling, para español y otros idiomas, es similar. En el caso del español está entrenado con el corpus AnCora y entre los rasgos de aprendizaje utiliza, además de los establecidos en Gildea y Jurafsky (2002) otros como las relaciones de dependencia o la voz verbal (Lluís et al. 2013).

Los sistemas actuales, como el resto de tareas, están basados en vectores y *word embeddings*:

[http://nlpprogress.com/english/semantic_role_labeling.html](http://nlpprogress.com/english/semantic_role_labeling.html)

También hay interés en sistemas multi- y cross-lingües:

[https://www.aclweb.org/anthology/2020.acl-main.627/](https://www.aclweb.org/anthology/2020.acl-main.627/)

## Otros tipos de análisis.

[http://nlpprogress.com/english/semantic_parsing.html](http://nlpprogress.com/english/semantic_parsing.html)

## Bibliografía

Fellbau, C. (ed) 1998. *WordNet: An Electronic Lexical Database*. Cambridge, MA: MIT Press.

Juravsky y Martin (2020) *Speech and Language Processing*. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/) (Caps 18-19)

Miller, G. A. 1995. “WordNet: A Lexical Database for English”. *Communications of the ACM*, 38(11), 39-41.

Navarro Colorado, Borja (2021) "Sistemas de anotación semántica para corpus de español" en Giovanni Parodi, Pascual Cantos & Lewis Howe (Editores) *The Routledge Handbook of Spanish Corpus Linguistics* Routledge.
