
(label_historia)=
Revisión histórica
==================

*«If I have seen further it is by standing on the shoulders of Giants.», Isaac Newton, 1675.*

A continuación se presenta una revisión histórica de la evolución del procesamiento del lenguaje natural desde sus inicios hasta nuestro días que sirve para hilvanar los contenidos de la asignatura. En los siguientes apartados de este bloque se entrará en detalles técnicos sobre el funcionamiento de los modelos neuronales, que son los que actualmente proporcionan los mejores resultados en las principales aplicaciones.

```{admonition} Nota
:class: note
Hacia final de curso deberías ser capaz de leer esta revisión histórica entendiendo cada aspecto explicado.
```

```{admonition} Nota
:class: tip
El análisis "[10 things][things] you need to know about BERT and the transformer architecture that are reshaping the AI landscape", más centrado en el panorama reciente del procesamiento del lenguaje natural, también te puede servir para repasar todo este bloque a final de curso y asegurarte de que has entendido todos sus conceptos.

[things]: https://neptune.ai/blog/bert-and-the-transformer-architecture-reshaping-the-ai-landscape
```

## Algo de historia

### Los inicios y la traducción automática

El procesamiento del lenguaje natural ha tenido en la tarea de la traducción automática uno de sus principales catalizadores, por lo que la evolución de esta tarea concreta es un buen reflejo de la evolución de la disciplina entera. En el año 1947, el matemático e informático Warren Weaver planteaba en una carta a un colega la posibilidad de usar los computadores que comenzaban a aparecer en la época para traducir la documentación de la Unesco: «Recognizing fully, even though necessarily vaguely, the semantic difficulties because of multiple meanings, etc., I have wondered if it were unthinkable to design a computer which would translate.» Cinco años más tarde se celebraba una reunión de expertos en traducción automática en el MIT de los EUA, y en 1954 se presentó un sistema desarrollado conjuntamente por la Universidad de Georgetown e IBM que traducía unas 60 frases del ruso al inglés utilizando un pequeño diccionario y seis reglas de reordenamiento y selección léxica. Pese a la euforia inicial, la mejora en la calidad de estos sistemas fue tan lenta que en 1966 un comité de expertos recomendó al gobierno de los EUA recortar el presupuesto de investigación invertido en ellos.

### Los primeros sistemas conversacionales

Una de las grandes pretensiones de la humanidad ha sido desde hace siglos la de disponer de ingenios parlantes. Ramón Llull en el siglo XII concibió un artilugio mecánico con el que pretendía que se pudiera probar o refutar cualquier proposición. En el capítulo 63 del segundo libro del Quijote, el Caballero de la Triste Figura queda sorprendido al entablar diálogo con una cabeza parlante, de la que nunca supo que se trataba de un engaño. Pero realmente los primeros sistemas conversacionales (*bots*) no aparecen hasta mediados de los 60, siendo ELIZA, que incluso podía adoptar diferentes personalidades o roles, o SHRDLU, que permitía interactuar con un mundo de bloques en lenguaje natural, los ejemplos más conocidos. Para construir un sistema de este tipo es necesario desarrollar técnicas de procesamiento del lenguaje natural y estas técnicas han tenido siempre un lugar privilegiado dentro del campo de la inteligencia artificial, hasta el punto de que cuando Alan Turing planteó en los años 40 su famosa prueba (*Turing's test*) consideró la capacidad de diálogo como la demostración última de que una máquina pudiera pensar.

### Técnicas simbólicas y estadísticas

Los años comprendidos entre la década de los 50 y la década de los 80 vieron toda una serie de avances en el campo, la mayoría de ellos dentro del terreno simbólico con sistemas que integraban reglas escritas por lingüistas. Las teorías acerca del lenguaje humano introducidas por Chomsky en los años 60 tuvieron una gran influencia en el desarrollo de estos formalismos. Sin embargo, hacia finales de la década de los 80 comienzan a aparecer sistemas competitivos basados en estadística y aprendizaje automático. En 1988 el investigador Frederik Jelinek enuncia su famosa frase, luego [matizada][jelineck], en relación a su sistema de reconocimiento de voz: «Every time I fire a linguist, my performance goes up». Además de contextualizar su afirmación, el mismo Jelinek reconoció posteriormente que las técnicas estadísticas pueden aplicarse en contextos híbridos en los que también tenga cabida el conocimiento lingüístico.

[jelineck]: http://www.lrec-conf.org/lrec2004/doc/jelinek.pdf

Las técnicas estadísticas (árboles de decisión, modelos ocultos de Markov, etc.) basadas en la explotación de grandes corpus de texto se ven propiciadas por la llegada de la web, que incrementa notablemente la cantidad de datos disponibles, y por el incremento en la capacidad de cómputo de los ordenadores. Pese a la predominancia de enfoques neuronales, las técnicas basadas en reglas o las estadísticas aún se usan hoy día en numerosos escenarios, como, por ejemplo, con lenguas con muy pocos recursos o para el pre o postprocesamiento de los textos usados en sistemas neuronales.

### Los primeros modelos neuronales

Los primeros modelos neuronales que procesaban el lenguaje humano en la década de los 90 se centraron en tareas relativamente sencillas como predecir el siguiente elemento de una secuencia (por ejemplo, el siguiente carácter dado el prefijo de una frase). Aunque en la década de los 90 ya aparecieron trabajos que usaban redes neuronales con lenguaje natural, no es hasta unos años después cuando empiezan a obtenerse resultados significativos. Un artículo de Bengio presentó un modelo neuronal que aprende a la vez representaciones distribuidas de las palabras de la entrada (lo que luego se conocería como *word embedding*) y un modelo probabilístico de la siguiente palabra a la salida. Este [trabajo][bengio] de 2003 ya tiene tamaños de vocabulario aceptables (probablemente inviables unos años antes) de en torno a las 16000 palabras. El entrenamiento de este modelo con millones de parámetros llevó varias semanas en un sistema con 40 CPUs y la perplejidad total del modelo resultante demostró ser más baja que la de modelos estadísticos consolidados tal como los basados en trigramas suavizados.

[bengio]: https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf


Ya en aquel trabajo se plantea que "polysemous words are probably not well served by the model presented here, which assigns to each word a single point in a continuous semantic space" y se anticipa la necesidad de que una palabra pueda tener más de una representación en base a su contexto. También se menciona la conveniencia de utilizar redes neuronales recurrentes en lugar de redes *feedforward*. Las arquitecturas recurrentes se habían usado intensamente en la década anterior para tareas sencillas. De hecho, las unidades LSTM, que sustituyen a las neuronas tradicionales en estos modelos para mitigar el problema del gradiente evanescente, se propusieron en el año 1997 por Hochreiter y Schmidhuber.

### El entrenamiento no supervisado

El tipo de entrenamiento del trabajo de Bengio se conoce como no supervisado, en el sentido de que no se necesitan etiquetar datos o asignar categorías durante el entrenamiento. Este tipo de aprendizaje fue defendido por Yann LeCun [en 2016][lecun] como una tarea muy importante en el camino hacia una inteligencia artificial de propósito general que pueda trabajar con el "sentido común", que él define como la capacidad de predecir el pasado, presente o futuro de cualquier información disponible.

[lecun]: https://ruder.io/highlights-nips-2016/#generalartificialintelligence

El entrenamiento no supervisado es una piedra angular en desarrollos como los word embeddings, los modelos preetrenados o los modelos de traducción de secuencias (por ejemplo, los usados en sistemas de traducción automática que no requieren corpus paralelo para su entrenamiento al explotar el concepto de *back-translation*).

### Aprendizaje multitarea

Otro elemento fundamental en los modelos de procesamiento del lenguaje natural es el de aprendizaje multitarea (*multi-task learning*) que ya propuso Caruana en la década de los 90. En el contexto actual de las redes neuronales, esto significa que parte o la totalidad de los parámetros es compartida entre redes que resuelven problemas diferentes, pero relacionados: como caso límite, una red puede entrenarse para clasificar textos entre diferentes idiomas o para búsqueda de respuestas, resumen automático y traducción automática a la vez de manera que se aprovechen los efectos sinérgicos de combinbar todas las tareas.

### Word embeddings

Aunque las representaciones distribuidas de palabras ya existían desde varios años antes, en 2013 Mikolov et al. muestran un método eficiente para su cálculo que dispara su uso. Los embeddings pueden calcularse mediante modelos complejos con grandes corpus de texto y luego emplearse en otras tareas. Existen colecciones como [fastText][fasttext], que incluyen embeddings para dos millones de palabras en inglés (obtenidos procesando un corpus de 16.000 millones de palabras) o embeddings multilingües para más de cien idiomas. También cabe aprender los embeddings para una tarea concreta, lo que consiste en aprender los valores de la tabla de *embeddings* como cualquier otro parámetro de la red (usualmente mediante descenso por gradiente estocástico). Los embeddings suelen tener propiedades geométricas interesantes (*Londres es a Reino Unido como París es a Francia*), pero también reflejan los sesgos de los textos en los que son entrenados (el embedding de *nurse* suele estar cerca del de *woman* y el *doctor* cerca de *man*).

[fasttext]: https://fasttext.cc/

### El inicio del auge de las redes neuronales

A partir de 2013 aproximadamente los modelos neuronales empiezan a ser considerados como una opción seria para ciertas tareas de procesamiento del lenguaje natural, pero las técnicas tradicionales todavía tienen mayor peso. En esos momentos, en el terreno del procesamiento de imagen, los modelos neuronales ya superan competición tras competición a los más tradicionales. Las redes neuronales convolucionales DanNet en 2011 y AlexNet en 2013, por poner dos ejemplos, superaron en varios puntos a modelos hasta entonces consolidados y obtuvieron resultados *superhumanos*  en múltiples tareas de procesamiento de imágenes. Un equivalente en el área del procesamiento del lenguaje natural no llegaría hasta aproximadamente 2018 con la aparición de ELMo y BERT.

Una de las principales ventajas de los modelos neuronales respecto a los estadísticos es que se elimina en la mayor parte de los casos la necesidad de explicitar, diseñar y extraer las características relevantes de los textos en base al problema a resolver. La extracción de características (*feature engineering*) implica el conocimiento de expertos. Las redes neuronales profundas, sin embargo, son capaces de trabajar con los textos en bruto sin apenas ningún preprocesamiento previo. 

### Modelos recurrentes sequence-to-sequence

En 2014, Sutskever et al. presentan el modelo neuronal *sequence-to-sequence* que incluye dos redes neuronales (de una o más capas cada una; a más capas, más profunda se considera la representación aprendida) en un modelo conocido como codificador-descodificador (*encoder-decoder*), que es capaz de obtener una representación intermedia de la secuencia completa de entrada y "desenrollarla" a continuación en una nueva secuencia  de longitud no necesariamente igual a la de la de entrada. Aunque hay muchas tareas que se pueden especificar de esta forma (por ejemplo, el resumen de textos o la descripción textual automática de imágenes), el sistema es aplicado inicialmente a la traducción automática. En ciertos casos, el modelo supera la calidad de la traducción de los sistemas estadísticos (basados en encontrar las traducciones más probables para segmentos de varias palabras y combinarlas y reordenarlas teniendo en cuenta un modelo de lengua), que eran los dominantes hasta ese momento. 

### El mecanismo de atención

Si bien el modelo *sequence-to-sequence* supuso un gran avance, su principal limitación es que comprime toda la secuencia de entrada en un único vector a partir del cuál se va generando toda la secuencia de salida. En el año siguiente, Bahdanau et al. perfeccionan el modelo introduciendo el mecanismo de *atención*: en lugar de obtener un vector único para la frase de entrada combinando los vectores de cada palabra, el descodificador es capaz de utilizar las representaciones individuales de todas las palabras de la secuencia de entrada; cuando el descodificador va a generar la predicción de la siguiente palabra de la secuencia de salida, decide el grado o porcentaje de influencia de cada representación de la entrada y de las representaciones de la salida generadas hasta ese momento. La atención supuso otro salto cuantitativo en el rendimiento de los modelos que lleva a los grandes proveedores de sistemas de traducción automática a migrar rápidamente en los meses siguientes a tecnologías neuronales.

### Redes neuronales con memoria explícita

A partir de 2014 comienzan a aparecer modelos neuronales avanzados (aunque los modelos simples datan de unas décadas antes) que integran de forma explícita una memoria de lectura/escritura en la que la red puede decidir almacenar ciertos vectores para su uso posterior. Los *computadores diferenciables neuronales* son ejemplo de este tipo de sistemas y son capaces de aprender algoritmos sencillos (ordenación o enrutamiento, por ejemplo) o trabajar en tareas en las que cierta información debe almacenarse durante largos periodos de tiempo.

### La arquitectura transformer

El mecanismo de atención no solo se puede aplicar a la situación de un modelo recurrente en el que el descodificador tiene que integrar con diferentes grados de atención la información aportada por el codificador. En 2017, de nuevo con un enfoque inicial en la traducción automática, aparece la arquitectura conocida como *transformer*, que elimina la necesidad de utilizar redes recurrentes (que arrastran el problema del gradiente evanescente que dificulta la detección de dependencias a largo plazo, como cuando un adjetivo al final de una frase larga concuerda con un sustantivo que aparece al principio de esta, y que, además, son difíciles de paralelizar ya que cada paso depende del anterior) al aplicar el concepto de *autoatención*: la representación de cada palabra en el codificador se obtiene integrando mediante mecanismos de atención las representaciones en la capa anterior de todas las palabras de la frase de entrada; del mismo modo, el descodificador usa la atención para determinar la influencia de las representaciones de la entrada y del prefijo de la salida generado hasta el momento en la representación de la palabra a generar y, por ende, en las probabilidades emitidas para la siguiente palabra de la salida.

### Modelos preentrenados

Aunque ya habían sido propuestos con anterioridad, en el año 2018 comienza la *revolución* de los llamados *modelos preentrenados*. Las representaciones vectoriales obtenidas por un codificador en sus diferentes capas pueden considerarse como *embeddings* contextuales de cada palabra. Si estos embeddings son representativos (es decir, sin son entrenados con suficientes cantidades de texto) pueden usarse para codificar la frase de entrada en redes neuronales que resuelvan tareas como detección de sentimiento, búsqueda de respuestas o inferencia en lenguaje natural. Pero los embeddings aprendidos por el codificador de un sistema de traducción automática tienen un par de inconvenientes: 

1. están condicionados por la lengua meta, ya que se entrenan para generar buenas traducciones por lo que no son monolingües; por ejemplo, el codificador de español aprendido para un traductor español-inglés puede representar con embeddings similares la palabra *canal* de una oración que habla sobre televisión y la palabra *canal* en una oración que habla sobre cauces de agua, simplemente porque en ambos casos la traducción es *channel*;
2. para obtener estos embeddings es necesario entrenar un sistema de traducción automática con grandes cantidades de corpus bilingües y hay muchas lenguas para las que no existe este tipo de información supervisada en cantidad suficiente. 

Por ello, los sistemas preentrenados se obtienen mediante tareas no supervisadas. Los primeros de estos modelos como ELMo entrenaban el sistema para que predijera la siguiente palabra, pero los sistemas posteriores como BERT plantean una tarea no supervisada más difícil que permite obtener representaciones más complejas y elaboradas; esta tarea, conocida como *mask filling* consiste en sustituir aleatoriamente algunas palabras de la entrada por una marca especial (*mask*) y enseñar a la red a maximizar la probabilidad de las palabras originales a la salida. Existen múltiples variaciones de esta estrategia no supervisada de entrenamiento, pero su planteamiento básico es similar a este.

El uso de un modelo preentrenado en una tarea concreta de procesamiento del lenguaje natural pasa por añadir una o más capas a la salida del modelo preentrenado y entrenar la salida del modelo ampliado para la tarea en cuestión, lo que se denomina *ajuste fino* (*fine-tuning*). Los pesos de la parte correspondiente al modelo preetrenado suelen dejarse congelados, pero también podrían ajustarse o incorporar entre las capas los llamados *adaptadores*. La arquitectura de un modelo preentrenado (por ejemplo, BERT) es como la del codificador de un transformer cuando el modelo resultante se va a usar para tareas de clasificación de secuencias; la arquitectura es como la de un transformer completo (por ejemplo, BART o T5, o sus versiones multilingües mBART o mT5) cuando el modelo resultante se va a usar para tareas que generan secuencias a partir de secuencias. Hay también modelos preentrenados para tareas específicas: así, para la continuación de secuencias la arquitectura de GPT-3 usa el descodificador de un transformer; y M2M es un transformer entrenado sobre decenas de corpus bilingües de múltiples pares de idiomas.

### El modelo GPT-3

El modelo comercial [GPT-3][gpt3] aparecido a mediados de 2020 es la evolución de GPT-2 publicado apenas un año antes y que ya mostraba [resultados][gpt2] sorprendentes para ese momento. GPT-3 fue entrenado con 400.000 millones de *tokens*; para un cálculo aproximado podemos asumir que un *token* equivale a una palabra y tener en cuenta que los tres volúmenes de «El Señor de los Anillos» tienen en torno a medio millón de palabras y que toda la serie de Harry Potter tiene aproximadamente un millón de palabras. Se trata de un modelo autoregresivo similar al descodificador de un transformer, entrenado para predecir el siguiente token de la secuencia y generar representaciones profundas en los cerca de 175.000 millones de parámetros del modelo más grande (existen versiones del sistema de tamaños inferiores; en cualquier caso, en pocos meses aparecieron otros modelos con un número de parámetros un orden de magnitud superior). El consumo necesario para entrenar el modelo grande se estima en unos 350 años de una GPU V100, lo que, al precio actual en plataformas en la nube supondría unos 5 millones de dólares. El sistema GPT-3 obtiene resultados interesantes en tareas para las que no ha sido explícitamente entrenado (el trabajo original no presentaba resultados tras hacer *fine-tuning*) como traducir textos, jugar al ajedrez, responder a preguntas de sentido común o escribir código, simplemente dándole algo de contexto previo (los primeros movimientos de una partida o algunos ejemplos de traducciones, por ejemplo) y obteniendo la continuación dada por el modelo. Esta situación en la que un sistema se somete a tareas para las que no ha sido entrenado se conoce como evaluación *zero-shot*. Los autores de GPT-3, en cualquier caso, reservan *zero-shot* para el caso en el que al sistema no se le da ningún contexto previo, *one-shot* cuando este incluye un único elemento (un movimiento de ajedrez o un ejemplo de traducción) y *few-shot* cuando el contexto previo es mayor. Una variación del modelo GPT-3 bautizada como [Dall·e][dalle] es capaz de generar imágenes a partir de descripciones textuales.

[gpt2]: https://openai.com/blog/better-language-models/#samples
[gpt3]: https://arxiv.org/abs/2005.14165
[dalle]: https://openai.com/blog/dall-e/

### Corpus disponibles

En los últimos años han ido apareciendo corpus monolingües o multilingües de tamaño cada vez mayor. Una tarea importante es la de filtrar su contenido para eliminar textos con ruido o en idiomas no deseados. Las lenguas con pocos recursos, no obstante, siguen padeciendo una falta importante de recursos lingüísticos y textuales, aunque diferentes iniciativas intentan paliar este problema. Los modelos multilingües (como mBART o mT5) son entrenados con textos de decenas de idiomas usando vocabularios compartidos y submuestreando los datos de los idiomas con más recursos. Aunque para el caso de los idiomas con más recursos el sistema multilingüe resultante suele presentar un rendimiento inferior al de sistemas monolingües específicos, las lenguas con pocos recursos se benefician de cierta *universalidad* en los patrones lingüísticos. En este sentido son también destacables proyectos como *universal dependencies* que pretende definir etiquetarios universales y elaborar colecciones de textos anotados para todas las lenguas de la Tierra.

Los modelos multilingües de traducción automática son incluso capaces de conseguir cierto grado de comportamiento *zero-shot* al permitir la traducción básica entre idiomas con los que no han sido entrenados si el corpus de entrenamiento contiene textos de lenguas similares.

### Modelos de subpalabras

Un cuello de botella de los modelos neuronales es el elevado tamaño de la matriz de embeddings o el cálculo de la función softmax en la capa de salida. Ambos están en función del tamaño del vocabulario. Para aligerarlo, se propuso el uso de unidades más pequeñas que la palabra, denominadas habitualmente *tokens*. Por ejemplo, si en lugar de tener un embedding para cada forma del presente de indicativo de los *cantar*, *bailar*, *danzar* y *pintar*, usamos representaciones para *cant*, *bail*, *danz* *pint*, *o*, *as*, *a*, *amos* *áis* y *an* habremos reducido el tamaño del vocabulario de 24 a 10. Estos tokens que representan unidades conocidas como subpalabras se obtienen mediante sencillas técnicas estadísticas de conteo como BPE o SentencePiece.

### Aplicaciones

Algunas tareas de bajo nivel típicas del procesamiento del lenguaje natural son la lematización, la segmentación morfológica, el etiquetado de partes de la oración, la inducción de gramáticas, el análisis sintáctico, la separación de un texto en oraciones, el reconocimiento de entidades nombradas, la extracción terminológica, la desambiguación del sentido de las palabras, la extracción de relaciones, el análisis semántico o la resolución de coreferencias. Aplicaciones de más alto nivel incluyen la obtención automática de resúmenes, el análisis de sentimiento u opinión, la generación de textos, los agentes conversacionales, los correctores ortográficos o de estilo, la traducción automática, la búsqueda de respuestas o la modelización del sentido común, entre otros.
