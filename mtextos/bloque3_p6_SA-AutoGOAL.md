P5. Auto Machine Learning
====================================

## **Clase práctica.**

### Auto Machine Learning- Descubrimiento automático de Pipelines: Caso de estudio de Análisis de Sentimientos

<!-- **Autores:**

- [Yoan Gutiérrez Vázquez][yoan]
- [José Ignacio Abreu Salas][abreu] -->

### Descripción

En esta clase práctica estudiaremos cómo descubrir pipelines óptimos para un problema determinado utilizando la librería [AutoGOAL].
Se orientarán ejercicios a resolver en los que el estudiante deberá ser capaz de según el ejemplo visto en esta práctica de diseñar la exploración de pipelines para resolver problemas de procesamiento del lenguaje natural.

Las entregas de ejercicios se han de hacer a través del UAcloud>Evaluación>[Nombre de la práctica].

### Ejemplo demostrativo

AutoGOAL :

- [06.1-SA-AutoGOAL]: AutoML a partir características
- [06.2-SA-AutoGOAL]: (End2End)AutoML a partir de problemas

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

[yoan]: https://orcid.org/0000-0002-4052-7427
[abreu]: https://orcid.org/0000-0002-4637-4206

[06.1-SA-AutoGOAL]: https://github.com/TeachingTextMining/TextClassification/blob/main/06-SA-AutoGOAL/06.1.0-TextClassification-with-AutoGOAL.ipynb
[06.2-SA-AutoGOAL]: https://github.com/TeachingTextMining/TextClassification/blob/main/06-SA-AutoGOAL/06.2.0-TextClassification-with-AutoGOAL-End2End.ipynb
[AutoGOAL]: https://autogoal.github.io/
