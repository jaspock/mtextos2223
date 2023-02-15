Práctica 1b : _Topic modeling_.
==============================

Borja Navarro Colorado

## Objeto

El objetivo de este ejercicio es practicar la conversión de un corpus en una representación semántica vectorial. Para ello se utilizará el modelo LDA _topic modeling_. Este modelo extrae temas recurrentes de un corpus a partir de su representación vectorial de las palabras. La herramienta para realizar la práctica es [Gensim](https://radimrehurek.com/gensim/index.html), y el corpus el corpus de noticias LexEsp. De nuevo se utilizará COLAB para facilitar el trabajo.

Breve explicación de LDA-Topic Modeling: [explicación inicial](https://docs.google.com/presentation/d/e/2PACX-1vRhjksmebwfZ8CfMNCqp7ucPr0i--fPNCa6dqb0NH3jiMOQV1lSvnlnF7qptbtqEsA5O4IzpcJa-F9r/pub?start=false&loop=false&delayms=60000)

## Proceso y entrega

La tarea es encontrar los temas comunes en un corpus de noticias. Para ello:

1. Cargar el corpus LexEsp en COLAB (fichero comprimido en la UA-Nube)
2. Pre-procesar el corpus. Como mínimo debe ser tokenizado. Además se puede lematizar y/o filtrar "stopwords" o seleccionar categorías gramaticales. Para ello se puede utilizar [SpaCy](https://spacy.io/) como en la práctica anterior, u otras herramientas de PLN como [NLTK](https://www.nltk.org/).
3. Crear el modelo LDA con [Gensim](https://radimrehurek.com/gensim/index.html).
4. Visualizar los _topics_ del corpus con [pyLDAvis](https://pyldavis.readthedocs.io/en/latest/index.html)

Una vez creado todo, analiza los _topics_ resultantes y cambia la configuración del experimento hasta hallar la lista de _topics_ más clara. Parámetros que se pueden modificar:
- Preproceso del corpus: ¿tokens o lemas?, ¿con o sin filtro _stopwords_?, ¿todas las categorías gramaticales o solo unas determinadas (por ejemplo, solo nombres)?, etc.
- Cantidad de _topics_.
- Cantidad de iteraciones.
- Los hiperparámetros _alpha_ y _beta_ (_eta_ en gensim) no hace falta modificarlos. Si quieres profundizar en este aspectos, ver: 
    - [https://www.thoughtvector.io/blog/lda-alpha-and-beta-parameters-the-intuition/](https://www.thoughtvector.io/blog/lda-alpha-and-beta-parameters-the-intuition/)
    - [https://datascience.stackexchange.com/questions/199/what-does-the-alpha-and-beta-hyperparameters-contribute-to-in-latent-dirichlet-a](https://datascience.stackexchange.com/questions/199/what-does-the-alpha-and-beta-hyperparameters-contribute-to-in-latent-dirichlet-a)
- Otros parámetros...

Con la configuración óptima, entrega el enlace del cuaderno COLAB (modo lectura) mediante la opción de entrega de prácticas de UA-CLOUD.

## Documentación.

Para realizar la práctica, sigue este tutorial (oficial) de LDA con Gensim:

- [https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html#sphx-glr-auto-examples-tutorials-run-lda-py](https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html#sphx-glr-auto-examples-tutorials-run-lda-py)

Otras páginas útiles:

- Introducción a Gensim: 
    + [https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html#sphx-glr-auto-examples-core-run-core-concepts-py](https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html#sphx-glr-auto-examples-core-run-core-concepts-py)
    + Otros modelos en Gensim: [https://radimrehurek.com/gensim/auto_examples/index.html#documentation](https://radimrehurek.com/gensim/auto_examples/index.html#documentation)

- Sobre _Topic modeling_:
    + [http://www.cs.columbia.edu/~blei/papers/Blei2012.pdf](http://www.cs.columbia.edu/~blei/papers/Blei2012.pdf)
    + [http://www.cs.columbia.edu/~blei/papers/Blei2011.pdf](http://www.cs.columbia.edu/~blei/papers/Blei2011.pdf)
    + [http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/)

- Visualizador pyLDSvis:
    + [https://pyldavis.readthedocs.io/en/latest/index.html](https://pyldavis.readthedocs.io/en/latest/index.html)
    + Ejemplo de uso y conexión con Gensim: [https://nbviewer.org/github/bmabey/pyLDAvis/blob/master/notebooks/pyLDAvis_overview.ipynb#topic=0&lambda=1&term=](https://nbviewer.org/github/bmabey/pyLDAvis/blob/master/notebooks/pyLDAvis_overview.ipynb#topic=0&lambda=1&term=)
    + En la página anterior hay un módulo obsoleto. Si os da error, probad esto:
    
            import pyLDAvis
            import pyLDAvis.gensim_models as gensimvis  
            pyLDAvis.enable_notebook()

            gensimvis.prepare(model, corpus, dictionary)

   [Fuente](https://stackoverflow.com/questions/66759852/no-module-named-pyldavis)

- Un trabajo mío (Borja Navarro Colorado) donde aplico *Topic Modeling* a poesía :-) :
    + [On poetic topic modeling](https://www.frontiersin.org/articles/10.3389/fdigh.2018.00015/full)

## Otras herramientas

Para realizar Topic Modeling, existen otras herramientas como:

- [MALLET](https://mimno.github.io/Mallet/topics.html)
- [Topic Modeling Tool](https://senderle.github.io/topic-modeling-tool/documentation/2017/01/06/quickstart.html), (que en realidad es solo una interfaz gráfica para MALLET).

