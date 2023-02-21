
Materiales de Minería de Textos
===============================

Universitat d'Alacant, curso 2022–2023
--------------------------------------

*«This is an exciting time to be working in speech and language processing», Daniel Jurafsky, James H. Martin, 2009*

*«You shall know a word by the company it keeps», John Rupert Firth, 1957*


% comentario
 
Novedades
---------

`````{list-table}
:header-rows: 0
:widths: 10 90
:class: tablita

* - 10 Feb 
  - Ya tenéis disponibles en la sección "{ref}`label_actividades_previas`" las actividades a realizar esta semana antes de la siguiente clase presencial.
* - 01 Feb 
  - En la sección "{ref}`label_actividades_previas`" podrás ir encontrando cada semana las actividades a realizar antes de la siguiente clase presencial. Habrá también un enlace a un pequeño cuestionario que tienes que rellenar antes de las 23.59 del día anterior con tu cuenta *gcloud.ua.es*. Recuerda que estos cuestionarios contribuyen a la nota final. Ya tienes disponible las actividades y el cuestionario a realizar antes de la clase del 8 de febrero de 2023.
* - 25 Ene 
  - Se ha publicado la primera versión de los materiales de la asignatura. Estos materiales pueden pueden ir cambiando antes de la clase en la que se impartan.

`````

(label_actividades_previas)=
Actividades previas
-------------------

- P.Ev1. [Evaluación 1 (común)](https://jaspock.github.io/mtextos2223/bloque3_ev.html#entrega-1-comun). Apertura el 22/02/2023 - Cierre 23:59 del 01/03/2023 - Fuera de plazo hasta 08/03/23.

- Antes de la clase del 22/02/2023: lee el [Tema  1 del bloque 2](https://jaspock.github.io/mtextos2223/bloque3_t1_aplicaciones.html); a continuación, contesta este [test][test03] (plazo límite: 23:59 horas del 21/02/2023). **IMPORTANTE:** PARA ESTA SESION SE HARÁ UNA EXCEPCIÓN Y EL PLAZO LÍMITE SERÁ: 23:59 horas del 27/02/2023

- Antes de la clase del 15/02/2023: lee los [apartados 5 y 6 del bloque 1](https://jaspock.github.io/mtextos2223/bloque1_3AnalisisSemantico.html), y luego contesta el siguiente [cuestionario][test02] (plazo límite: 23:59 horas del 14/02/2023).

- Antes de la clase del 08/02/2023: lee los [apartados 1, 2 y 3 del bloque 1](https://jaspock.github.io/mtextos2223/bloque1.html); a continuación, contesta este [test][test01] (plazo límite: 23:59 horas del 07/02/2023).



[test03]: https://docs.google.com/forms/d/e/1FAIpQLSdJOREB0q6HP95Ny9GkNiKpouKESLt5aZRNDzhjezqVfIBhHA/viewform

[test02]: https://docs.google.com/forms/d/e/1FAIpQLSec_eQ4ZecmSKNrPhNbuMkfhLko149ckC2qQzFxdmOapHvp8A/viewform?usp=sf_link
[test01]: https://forms.gle/ncbWkFGCjSqXSTiX9


Guía docente y normas del curso
-------------------------------

Estos son los materiales de clase de la asignatura Minería de Textos, coordinada por el profesor [Juan Antonio Pérez Ortiz][japerez_url] ([@japer3z][japerez_twitter]) de la Universitat d'Alacant e impartida también por los profesores [Francisco de Borja Navarro Colorado][borja url] y [Yoan Gutiérrez Vázquez][yoan url]. 

Para obtener información sobre la evaluación de la asignatura puedes consultar la [guía docente][guía]. Algunos aspectos adicionales que no están recogidos en la guía son los siguientes:

[japerez_url]: https://cvnet.cpd.ua.es/curriculum-breve/es/perez-ortiz-juan-antonio/15404
[borja url]: https://cvnet.cpd.ua.es/curriculum-breve/es/navarro-colorado-francisco-de-borja/9307
[yoan url]: https://cvnet.cpd.ua.es/curriculum-breve/es/gutierrez-vazquez-yoan/49618
[japerez_twitter]: https://twitter.com/japer3z
[guía]: https://cvnet.cpd.ua.es/Guia-Docente/GuiaDocente/Index?wlengua=es&wcodasi=43459&scaca=2022-23

- Las prácticas se realizan individualmente o en parejas, según se indique en el enunciado de cada una de ellas. Cada uno de los tres bloques de la asignatura tendrá uno o más trabajos prácticos. Los trabajos del primer bloque contarán un 15% en la nota final de las prácticas, los del segundo un 50% y un 35% los del tercero.
- La asistencia a prácticas es obligatoria. Se pasará lista en cada sesión presencial. Se puede tener un máximo de 3 faltas sin justificar. Si se acumulan más faltas no justificadas, no se podrá superar la parte de prácticas en la primera convocatoria, pero sí en la segunda (si se realizan las entregas correspondientes antes del día del examen) o en las otras convocatorias extraordinarias.

El [código fuente][fuente] de estas páginas, escrito en MyST para Jupyter Book, está disponible en Github.

[fuente]: https://github.com/jaspock/mtextos2223

Puedes obtener una copia local de estas páginas (por ejemplo, para poder consultarlas sin conexión) ejecutando::

```
  wget --mirror --no-parent --convert-links --page-requisites https://jaspock.github.io/mtextos2223/
```
Pero ten en cuenta que su contenido irá cambiando a lo largo del curso.

Presentación de la asignatura
-----------------------------

La diferencia entre los términos *minería de textos* y *procesamiento del lenguaje natural* es un tanto difusa. Podríamos decir que la minería de textos es el proceso de descubrimiento de patrones y obtención de información relevante de grandes colecciones de textos. Al igual que en el concepto más amplio de minería de datos, el énfasis no es en la extracción (minado) de los datos en sí, sino en la extracción de patrones y conocimiento relevante. En el caso de la minería de textos, las fuentes de información son textos digitalizados, que no incluyen otras fuentes de información más estructurada como las bases de datos. El procesamiento del lenguaje natural, por otro lado, aplica técnicas lingüísticas, computacionales y de aprendizaje automático a datos en lenguaje natural, habitualmente en forma de texto o voz, para resolver tareas que requieren que el ordenador adquiera cierta *comprensión* sobre su contenido. El procesamiento de voz no se suele considerar parte de la minería de textos, pero esta se vale en la mayor parte de las situaciones de las técnicas de procesamiento del lenguaje natural para conseguir sus objetivos.

La asignatura se centra en presentar los fundamentos, características y aplicaciones de las técnicas actuales para el procesamiento del lenguaje natural, pero no pretende entrar en excesivos detalles sobre modelos muy recientes ni estar completamente a la última, ya que el ritmo de aparición de sistemas que mejoran los resultados de los anteriores es extremadamente rápido (podríamos decir que semanal en muchos casos y mensual en otros). Como ejemplo, el conjunto de *benchmarks* llamado [SuperGLUE][tareas] quedó prácticamente [obsoleto en menos de dos años][superglue] por la sucesiva aparición de arquitecturas que conseguían cada vez mejores resultados en los problemas que incluía.

[tareas]: https://super.gluebenchmark.com/tasks/
[superglue]: https://www.microsoft.com/en-us/research/blog/microsoft-deberta-surpasses-human-performance-on-the-superglue-benchmark/

La asignatura tiene tres bloques: el primero ("{ref}`label_introduccion`") introduce los fundamentos de la lingüística computacional; en el segundo ("{ref}`label_aplicaciones`") se discuten algunas de las aplicaciones más importantes del procesamiento del lenguaje natural; por último, el tercer bloque ("{ref}`label_tecnicas`") estudia con cierto nivel de detalle las arquitecturas neuronales más empleadas en el área. 

### Para saber más 

Para ampliar lo aprendido en la asignatura puedes consultar algunas de estas fuentes en línea:

- "[Speech and language processing][jurafsky]" (borrador de la tercera edición).
- "[Dive into deep learning][dive]".
- "The [mathematical][mathematical] engineering of deep learning"
- Materiales del curso "[Natural language processing with deep learning][stanford]" de Stanford.
- Materiales del curso "[Neural nets for NLP][neubig]" de la Universidad Carnegie Mellon.

[jurafsky]: https://web.stanford.edu/~jurafsky/slp3/
[dive]: http://d2l.ai/
[mathematical]: https://deeplearningmath.org/
[stanford]: http://web.stanford.edu/class/cs224n/
[neubig]: https://www.youtube.com/playlist?list=PL8PYTP1V4I8AkaHEJ7lOOrlex-pcxS-XV


```{image} images/tower_of_babel_xkcd_2421.png
:alt: comic xkcd 2421
:width: 600px
:align: center
```
%:class: bg-primary mb-1
