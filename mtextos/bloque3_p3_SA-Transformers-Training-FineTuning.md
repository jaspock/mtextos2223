P2. Reajustar modelos Transformers
====================================

```{admonition} Nota
:class: note
Lee con atención la práctica 2 del bloque 2. Realiza los ejercicios y una entrega unificada (práctica 2, 3 y 4), la cual se anunciará en la introducción de la asignatura y a través del uaCloud.

Tiempo de dedicación: 3 horas (asíncrona) + 3 horas trabajo independiente
```

## **Clase práctica.**

### Reajustar modelos Transformers: Caso de estudio de Análisis de Sentimientos

<!-- **Autores:**

- [Yoan Gutiérrez Vázquez][yoan]
- [José Ignacio Abreu Salas][abreu] -->

### Descripción

En esta clase práctica estudiaremos cómo ajustar modelos de Transformers a problemas concretos, en este caso uno de análisis de sentimientos. Los modelos utilizados contienen un vocabulario muy amplio y han sido entrenados sin ajustar los pesos internos a problemas concretos. Lo que estudiaremos será cómo realizar ajustes al problema.
Se orientarán ejercicios a resolver en los que el estudiante deberá reajustar modelos existentes BERTs, mostrados en los ejemplos estudiados, para adaptarlos a la resolución de los ejercicios.

Las entregas de ejercicios se han de hacer a través del UAcloud>Evaluación>[Nombre de la práctica].

### Ejemplo demostrativo

Transformers Training Fine Tuning:

- [03-SA-Transformers-Training-FineTuning]

### Ejercicios

#### Ejercicio 1

Basándose en el ejemplo anterior haga uso del siguiente dataset y diseñe su propio sistema para el análisis de sentimientos. Se disponibilizan unas funciones python para la limpieza y carga de dataset.

- sample_data/ejercicio_tripadvisor.csv
- tripadvisor_Utils.py

#### Ejercicio 2

Basándose en el ejemplo anterior haga uso del siguiente dataset y diseñe su propio sistema para el análisis de sentimientos. Se disponibilizan unas funciones python para la limpieza y carga de dataset.

- sample_data/ejercicio_bbc_train.csv
- sample_data/ejercicio_bbc_test.csv

#### Ejercicios adicionales

Elige alguno de los siguientes datasets y conforma tu propio sistema de sentiment analysis.

- [SA Kaggle todos][kaggle]
- [Product review][product] (recomendado)
- [SA huggingface][huggingface]

### Criterios a tener en cuenta para la práctica:

- El cuaderno a entregar no debe tener errores de ejecución.
- Cada modificación de autor incorporada en cuaderno debe ser señalada con comentario. Por ejemplo ####Codigo NOMBRE_DEL_AUTOR ....#####.
- Se deben comentar y describir los aportes realizados por el autor, y explicar los motivos
- Se deben evaluar varias opciones de experimentación (i.e. preprocesamiento, configuraciones, tecnologías, modelos) y explicarlas.
- Se deben describir discusiones y conclusiones del estudio.


[huggingface]: https://huggingface.co/datasets?search=sentiment
[product]: https://www.kaggle.com/arbazkhan971/product-sentiment-analysis
[kaggle]: https://www.kaggle.com/search?q=sentiment+analysis+in%3Adatasets

[03-SA-Transformers-Training-FineTuning]: https://github.com/TeachingTextMining/TextClassification/tree/main/03-SA-Transformers-Training-FineTuning

[yoan]: https://orcid.org/0000-0002-4052-7427
[abreu]: https://orcid.org/0000-0002-4637-4206
