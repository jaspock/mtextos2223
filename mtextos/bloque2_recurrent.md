
Redes neuronales recurrentes
============================

Hasta hace pocos años, las redes neuronales recurrentes (RNR) eran el modelo neuronal más usado para el procesamiento de las secuencias (principalmente textos) implicadas en el procesamiento del lenguaje natural. Aunque las redes convolucionales se han venido usando también en ciertos contextos, la arquitectura transformer, aparecida en 2017, es la que verdaderamente explica la pérdida de protagonismo de las RNR. Esta situación, no obstante, puede cambiar en el futuro.

En este apartado veremos los fundamentos de las RNR y dejaremos el transformer para más adelante. 

```{admonition} Nota
:class: note
Una discusión introductoria y menos detallada de buena parte de lo aquí comentado puede seguirse en "A beginner's [guide][guide] to LSTMs and recurrent neural networks".
```

[guide]: https://wiki.pathmind.com/lstm

Las RNR o el transformer no son la única manera de incorporar información sobre la historia de una secuencia a una red neuronal. Una red no recurrente puede ser ampliada con la incorporación a sus entradas de una memoria explícita a corto plazo mediante una *ventana temporal* de tokens. De esta forma, la entrada a la red consistirá en el token actual $u[t]$ (para simplificar, podemos asumir por ahora que un token es una palabra) concatenado con los $p-1$ tokens anteriores $u[t-1],\ldots,u[t-p+1]$ o con una ventana de valores en torno a $u[t]$. En este caso, sin embargo, el contexto disponible es mucho más limitado, el alcance de las representaciones más reducido y el número de parámetros mayor.

## Procesamiento simbólico con redes recurrentes

Consideremos que tenemos un *vocabulario* (un conjunto de símbolos conocidos como *tokens*) $V = \{\sigma_1, \ldots, \sigma_{|V|}\}$ a partir del cual se obtienen secuencias temporales de la forma $s[1],\ldots,s[t],\ldots,s[L]$. Aunque las redes recurrentes pueden ser entrenadas para múltiples tareas como clasificar la temática de una frase de entrada o generar una traducción a otro idioma, aquí nos centraremos en la tarea de predecir el siguiente token de una secuencia. Los aspectos relevantes son los mismos independientemente de la tarea concreta para la que se utilice la RNR: la entrada se procesa token a token, se generan unas representaciones intermedias en un *espacio de estados* y a partir de estas representaciones se obtiene la salida de la red, que se interpretará de una forma u otra en función de la tarea.

```{admonition} Nota
:class: note
En las tareas de procesamiento del lenguaje natural, normalmente se reserva un token del vocabulario al que suele llamarse `UNK` (por el inglés *unknown*) para representar cualquier token desconocido que no pertenezca al vocabulario (OOV, por *out-of-vocabulary*), bien durante el entrenamiento, bien durante el uso en producción del modelo. El criterio para decidir si un token forma parte o no del vocabulario suele ser su frecuencia de aparición en el corpus de entrenamiento. El criterio para decidir el tamaño del vocabulario suele basarse en el tamaño deseado de la arquitectura resultante (a mayor vocabulario, mayor tamaño de la red neuronal).
```

Para predecir el siguiente símbolo de  la secuencia con una RNR debemos determinar varias cosas: cómo se representa cada uno de los símbolos de $V$ y cómo se realiza el entrenamiento de la red para esta tarea. La forma más habitual de codificar los distintos símbolos $\sigma_i \in V$ para su procesamiento por una RNR es la denominada  codificación *exclusiva*, más comúnmente conocida como representación *one-hot*. En ella, todos los símbolos se codifican mediante vectores unitarios de tamaño $|V|$, de forma que la representación del símbolo $\sigma_i$ en un espacio $[0,1]^{|V|}$ se obtiene a través de la función de codificación:

$$
C_{V}: V \longrightarrow [0,1]^{|V|}
$$

en la que el $j$-ésimo componente del vector resultante es:

$$
  (C_V(\sigma_i))_j = \delta_{i,j} \quad\quad 
  \sigma_i \in V, \,\,
j=1,\ldots,|V| 
$$

donde $\delta$ es la función *delta de Kronecker*, definida como:

$$
\delta_{i,j} = 
\left\{ \begin{array}{r@{\quad}l}
1 & \mbox{si $i=j$} \\[2ex]
0 & \mbox{en otro caso}
\end{array} \right.
$$ (ec:kronecker)

Es decir, el símbolo $\sigma_i$ se representa mediante un vector unitario en el que todos los componentes excepto el $i$-ésimo son cero. En principio, cada token se representa con el mismo vector durante todo el entrenamiento. 

Cuando se entrena una RNR para predecir las probabilidades del siguiente token de una secuencia, en el instante $t$ se alimenta la red con la entrada:

$$
\boldsymbol{u}[t]= C_V(s[t])
$$

y la salida obtenida $y_i[t]$ se puede interpretar (como veremos más adelante), después de normalizarla para que todos sus componentes sumen uno, como la probabilidad de que el siguiente símbolo de la secuencia sea $\sigma_i$. Para reajustar los pesos de la red, se considera como salida deseada para el algoritmo de entrenamiento la codificación *one-hot* del siguiente token:

$$
\boldsymbol{d}[t]= C_V(s[t+1])
$$

Cuando la codificación *one-hot* se aplica a las entradas, el número de estas es $n_U=|V|$, y puede considerarse que cada símbolo selecciona una determinada dinámica de la red. Al aplicar este tipo de codificación también a las salidas deseadas, el número de neuronas de salida es $n_Y=|V|$.

```{admonition} Nota
:class: note
A estas alturas del curso, ya sabes que hoy en día en el procesamiento de lenguaje natural las entradas se representan mediante vectores más ricos denominados *embeddings*. Los embeddings no son incompatibles con la codificación *one-hot*, en cualquier caso. Si los embeddings se almacenan en una matriz $W$ de tamaño $|V| \times n$ donde $n$ es la dimensión de los embeddings (el embedding de cada token ocupa, por tanto, una fila de la matriz) y consideramos la representación *one-hot* de la entrada como un vector fila, el producto matricial $C_V(s[t]) \, W$ devolverá el embedding correspondiente al token de la entrada. Esta matriz $W$ de embeddings puede rellenarse con los embeddings resultantes de aplicar un algoritmo como *word2vec* y mantenerse fija durante el aprendizaje, o bien cada uno de sus elementos puede considerarse como un parámetro a ajustar por el algoritmo de entrenamiento. Aunque matemáticamente el producto matricial anterior refleja la idea de seleccionar un embedding, a la hora de implementar esta operativa en un programa la multiplicación no es necesaria y basta con seleccionar como entrada a la red neuronal la fila de la matriz o *tabla de embeddings* $W$ correspondiente al token a procesar. La representación *one-hot* sí que se usa en cualquier caso a la salida de la red para representar la salida esperada en la función de pérdida.
```

## Red recurrente de Elman

Existen muchos tipos de arquitecturas neuronales recurrentes. Aquí nos centraremos en una de las más simples: la *red recurrente de Elman*, propuesta por Jeffrey L. Elman en 1990. Este modelo se acerca bastante a lo que un profesional tiene en su cabeza cuando piensa en términos generales en una red recurrente, aunque no la denomine como *red de Elman*. La arquitectura, que puede observarse en la {numref}`fig-rrs1`, nos permite presentar conceptos que luego pueden extrapolarse a modelos más complejos.


```{figure} images/rnr-elman.png
---
height: 320px
name: fig-rrs1
---
Esquema de la red recurrente de Elman.
```

La dinámica de la red de Elman viene determinada por las ecuaciones siguientes: 

$$
y_i [t] & = & g_Y (Y_i [t]) \quad\quad i=1,\ldots,n_Y \\[2ex]
Y_i [t] & = & \sum_{j=1}^{n_X} W^{y,x}_{i,j} x_j [t] + W^y_i \\[2ex]
x_i [t] & = & g_X (X_i [t]) \quad\quad i=1,\ldots,n_X \\[2ex]
X_i [t] & = &
  \sum_{j=1}^{n_U} W^{x,u}_{i,j} u_j [t] +
  \sum_{j=1}^{n_X} W^{x,x}_{i,j} x_{j} [t-1] + W^x_i
$$ (ec-rrs1y)

En las ecuaciones anteriores, los superíndices indican el cálculo en el que está implicado el peso: por ejemplo, $W^{y,u}_{i,j}$ indica que ese peso contribuye a determinar la salida $y$ a partir de la entrada $u$. Por otra parte, $W^{x}_{i}$ indica que este peso es un sesgo implicado en el cálculo del estado $\boldsymbol{x}$. Los subíndices muestran las unidades concretas que se ven afectadas (conectadas) y van paralelos a los superíndices. El vector $\boldsymbol{u}[t]$, como se ha comentado, es el embedding correspondiente al token actual o, en modelos más simples, la codificación *one-hot* de dicho token. A la representación $\boldsymbol{x}[t]$ se le llama *estado* de la red neuronal; estas representaciones pueden también considerarse en ciertos contextos como embeddings del token de entrada correspondiente. Las funciones $g_X$ y $g_Y$ son funciones de activación (por ejemplo, sigmoideas).

```{admonition} Nota
:class: note
Aunque el modelo aquí presentado es completamente válido y útil, en tareas complejas la red se suele ampliar con capas de estado adicionales. En este caso, la recurrencia sigue existiendo entre cada capa y ella misma, pero también son posibles esquemas más avanzados en los que la salida de una capa retroalimenta la entrada de capas anteriores.
```

El estado inicial $\boldsymbol{x}[0]$ se inicializa normalmente a $\boldsymbol{0}$.

```{admonition} Nota
:class: note
Este modelo solo considera el contexto anterior para determinar la historia de la secuencia. En muchas tareas de procesamiento del lenguaje natural, sin embargo, suele ser necesario (o como mínimo beneficioso) tener en cuenta también el contexto posterior a un token dado. Por ello, se emplean sistemas como las *RNR bidireccionales* que usan dos modelos recurrentes: uno que procesa la entrada de izquierda a derecha y otro que la procesa de derecha a izquierda. Dado un token, se considera como su vector de estado el resultante de alguna operación (la media, la suma o la concatenación, por ejemplo) que integre los vectores de estado de ambos modelos. Observa que podría darse el caso de sistemas que han de procesar la entrada en tiempo real a nivel de token sin esperar al final de la frase (como en la traducción simultánea), pero lo más habitual es disponer como mínimo de la frase completa desde el principio.
```

## Entrenamiento de redes neuronales recurrentes

Para entrenar la RNR de forma supervisada se necesita normalmente algún tipo de *función de pérdida* o *medida del error* $E[t]$ que describa la adecuación de la salida proporcionada por la red al valor deseado. Los parámetros se ajustan entonces intentando minimizar este error. Una posible función de error es la función de error cuadrático, definida para el instante $t$ como:

$$
  E[t] = \frac{1}{2} \sum_{i=1}^{n_Y} \left( d_i [t] - y_i[t] \right)^2
$$ (ec:error)

donde $d_i[t]$ es el *valor deseado* o *esperado* para la $i$-ésima componente de la salida en el instante $t$, e $y_i[t]$ es la salida correspondiente de la red.

```{admonition} Nota
:class: note
En el contexto del procesamiento del lenguaje natural y en el caso habitual de que la salida de la red se interprete como un vector de probabilidades, se utilizan funciones de pérdida más específicas como la entropia cruzada, que ya vimos. En este apartado, sin embargo, por motivos pedagógicos, nos centraremos en la función de error cuadrático ya que su derivada, que calcularemos a continuación, es ligeramente más sencilla. Lo que interesa es que entiendas cómo se calculan en general estas derivadas, porque, a efectos prácticos, las librerías como Pytorch o Tensorflow se encargan de obtenerlas automáticamente para una u otra función de pérdida.
```

### Descenso por gradiente

Los principales algoritmos de entrenamiento se basan en el cálculo del *gradiente* de la función de error, esto es, de la derivada de la función de error con respecto a los distintos parámetros ajustables de la red. Se trata de intentar encontrar el mínimo de la función de error mediante la búsqueda de un punto donde el gradiente se anule. Esta condición es necesaria, pero no suficiente debido a la existencia de mínimos locales, máximos o puntos de silla; de ahí el carácter heurístico del método.

Una de las variantes basadas en el gradiente más utilizadas es el *descenso por el gradiente*. En él los sucesivos ajustes realizados se hacen de forma individual para cada parámetro, digamos $W_i$, en sentido opuesto al vector de gradiente $\partial E[n] / \partial W_i[n]$:

$$
W_i[n+1] = W_i[n] - \alpha \: \frac{\partial E[n]}{\partial W_i[n]}
$$

donde $\alpha$ es un parámetro conocido como *tasa de aprendizaje*, que ha de tomar un valor convenientemente pequeño. Al pasar de la iteración $n$ a la $n+1$ (el momento preciso de la actualización de los parámetros depende del tipo concreto de entrenamiento, pero normalmente se realiza tras finalizar el procesamiento de un *mini-batch*), el algoritmo aplica la corrección:

$$
\Delta W_i[n] = W_i[n+1] - W_i[n] = 
                   - \alpha \: \frac{\partial E[n]}{\partial W_i[n]}
$$ (ec-introDelta)

```{admonition} Nota
:class: note
Observa que en la ecuación anterior hemos usado $n$ y no $t$ para referirnos a los momentos en que se atualizan los pesos de la red porque el procesamiento de cada nuevo token de la secuencia no tiene por qué coincidir con un nuevo paso en la actualización de los pesos. Si los pesos se actualizan tras cada token se habla de *actualización en línea*, si se hace tras cada frase de *actualización por patrones o secuencias* y si se hace tras procesar un conjunto de varias frases (lo más habitual para aprovechar el rendimiento de la GPUs) se habla de *actualización por lotes* o *minilotes*.   
```

La tasa de aprendizaje $\alpha$ tiene una enorme influencia en la convergencia del método de descenso por el gradiente. Si $\alpha$ es pequeña, el proceso de aprendizaje se desarrolla suavemente, pero la convergencia del sistema a una solución estable puede llevar un tiempo excesivo. Si $\alpha$ es grande, la velocidad de aprendizaje aumenta, pero existe el riesgo de que el proceso de aprendizaje diverja y el sistema se vuelva inestable.

Existen dos formas diferentes de calcular las derivadas parciales anteriores. La primera que veremos, el *aprendizaje recurrente en tiempo real* es conceptualmente más sencilla pero no se usa mucho actualmente. La segunda, conocida como *retropropagación a través del tiempo*, permite transformar el problema del entrenamiento de una RNR en uno equivalente de entrenamiento de una red no recurrente (*feedforward*) y aplicar las soluciones convencionales para este tipo de redes.

### Aprendizaje recurrente en tiempo real

El *aprendizaje recurrente en tiempo real* (RTRL, por el inglés *real-time recurrent learning*) es una forma de calcular las derivadas parciales de la función de error, aunque algunos autores se refieren a él como un algoritmo de entrenamiento *per se* al combinarlo con el ajuste de pesos realizado con el descenso por el gradiente. Veámoslo con un ejemplo, derivando las ecuaciones de una red recurrente de Elman, cuya dinámica viene definida por las ecuaciones del bloque {eq}`ec-rrs1y`. La derivación de las ecuaciones para otros tipos de redes recurrentes es muy similar a la de la red de Elman.

Consideremos una función de error cuadrático como la de {eq}`ec:error`. La regla de la cadena nos dice que:

$$
\left(f \circ g \right)'(x) = f'(g(x)) \cdot g'(x)
$$


Aplicando la regla de la cadena y considerando un parámetro ajustable cualquiera, se tiene que:

$$
\frac{\partial E[t]}{\partial \Box} = - \sum_{l=1}^{n_Y}
(d_l[t] - y_l[t]) 
\frac{\partial y_l[t]}{\partial \Box}
$$

En lo anterior, la derivada $\partial y_l[t] / \partial \Box$ depende del parámetro concreto considerado. A continuación se dan las expresiones de estas derivadas para todos los pesos y sesgos de la red. Comprueba que obtienes el mismo resultado.

$$
\begin{eqnarray}
\frac{\partial y_l[t]}{\partial W^y_i} & = &
  g_Y'(Y_l[t]) \, \delta_{l,i}  \\[2ex]
\frac{\partial y_l[t]}{\partial W^{y,x}_{i,j}} & = & 
  g_Y'(Y_l[t]) \, x_j[t] \delta_{l,i}  \\[2ex]
\frac{\partial y_l[t]}{\partial W^{x}_j} & = &
  g_Y'(Y_l[t]) \sum_{i=1}^{n_X} W^{y,x}_{l,i} 
  \frac{\partial x_i[t]}{\partial W^{x}_j}  \\[2ex]
\frac{\partial y_l[t]}{\partial W^{x,u}_{j,k}} & = &
  g_Y'(Y_l[t]) \sum_{i=1}^{n_X} W^{y,x}_{l,i} 
  \frac{\partial x_i[t]}{\partial W^{x,u}_{j,k}}  \\[2ex]
\frac{\partial y_l[t]}{\partial W^{x,x}_{j,k}} & = &
  g_Y'(Y_l[t]) \sum_{i=1}^{n_X} W^{y,x}_{l,i} 
  \frac{\partial x_i[t]}{\partial W^{x,x}_{j,k}} 
\end{eqnarray}
$$ (ec-apb1)

Para la derivación de las ecuaciones anteriores debe tenerse en cuenta las siguientes expresiones:

$$
\begin{eqnarray}
\frac{\partial W^y_i}{\partial W^y_j} & = & \delta_{i,j} \\[2ex]
\frac{\partial W^{y,x}_{i,j}}{\partial W^{y,x}_{k,l}} & = & \delta_{i,k}
 \,  \delta_{j,l} \\[2ex]
\frac{\partial W^x_i}{\partial W^x_j} & = & \delta_{i,j} \\[2ex]
\frac{\partial W^{x,u}_{i,j}}{\partial W^{x,u}_{k,l}} & = & \delta_{i,k}
 \,  \delta_{j,l} \\[2ex]
\frac{\partial W^{x,x}_{i,j}}{\partial W^{x,x}_{k,l}} & = & \delta_{i,k}
 \,  \delta_{j,l}
\end{eqnarray}
$$

donde la función $\delta_{i,j}$ es la *delta de Kronecker*, ya definida en {eq}`ec:kronecker`.

Las derivadas del estado $x_i[t]$ de las ecuaciones del bloque {eq}`ec-apb1` son recurrentes en RTRL como resultado de la propia recurrencia de la red:

$$
\begin{eqnarray}
\frac{\partial x_i[t]}{\partial W^{x}_j} & = &
  g_X'(X_i[t]) 
  \left( \delta_{i,j} + \sum_{k=1}^{n_X} W^{x,x}_{i,k} 
  \frac{\partial x_k[t-1]}{\partial W^{x}_j} \right)  \\[2ex]
\frac{\partial x_i[t]}{\partial W^{x,u}_{j,k}} & = &
  g_X'(X_i[t]) 
  \left( u_k[t] \delta_{i,j} + \sum_{m=1}^{n_X} W^{x,x}_{i,m} 
  \frac{\partial x_m[t-1]}{\partial W^{x,u}_{j,k}} \right) \\[2ex]
\frac{\partial x_i[t]}{\partial W^{x,x}_{j,k}} & = &
  g_X'(X_i[t])
  \left( x_k[t-1] \delta_{i,j} + \sum_{m=1}^{n_X} W^{x,x}_{i,m} 
  \frac{\partial x_m[t-1]}{\partial W^{x,x}_{j,k}} \right)
\end{eqnarray}
$$ (ec-ejrtrl)

La implementación de un algoritmo de descenso por el gradiente a partir de estas ecuaciones es sencilla. En cada paso es necesario tener guardadas las derivadas del estado anterior para poder calcular las del siguiente. La derivada de la función logística $g_L(x)$ es $g_L(x) (1 - g_L(x))$ y la derivada de la función tangente hiperbólica $g_T(x)$ es $1 - g_{T}^{2}(x)$.



### Retropropagación en el tiempo

Al igual que hicimos con RTRL, consideraremos la retropropagación en el tiempo (BPTT, por el inglés *backpropagation through time*) como una forma de calcular las derivadas parciales de la función de error con respecto a los parámetros ajustables de la red, aunque hay autores que denominan BPTT a la combinación de lo anterior con el descenso por el gradiente.

Al calcular las derivadas parciales en BPTT se asume que el comportamiento temporal de la RNR puede ser *desplegado* en el tiempo en forma de red hacia adelante. Es posible aplicar entonces el conocido algoritmo de retropropagación para calcular las derivadas parciales de este tipo de redes. El despliegue de la RNR hace que la red hacia adelante (*red extendida*) vaya creciendo una y otra vez tras consumir cada nuevo token. Así, suponiendo una red de Elman, las unidades de entrada y las unidades de estado del instante $t$ se convierten en dos nuevas capas en la red extendida; las unidades de entrada y las unidades ocultas del instante $t-1$ se convierten también en dos nuevas capas de la red extendida; y así sucesivamente hasta llegar al primer instante de tiempo correspondiente al primer token de la secuencia. En la {numref}`fig-bptt` se muestra la red de Elman desplegada en el instante $t$.


```{figure} images/rnr-bptt.png
---
height: 640px
name: fig-bptt
---
Una red de Elman desplegada en el instante $t$ según el algoritmo de retropropagación en el tiempo.
```

Como realmente solo existe un conjunto de unidades de entrada y de unidades ocultas, los pesos equivalentes en las distintas capas virtuales han de tener idéntico valor; el algoritmo de retropropagación permite obtener la contribución al error total de cada una de las versiones de los pesos, pero a la hora de actualizarlos debe considerarse las contribuciones de los pesos equivalentes. Habitualmente, para cada parámetro instanciado múltiples veces en la red desplegada se toma la media de las actualizaciones correspondientes para actualizarlo.

```{admonition} Nota
:class: note
Es fácil ver que el tamaño de cada secuencia determina el de la red extendida. En el caso de una secuencia de longitud relativamente extensa, las necesidades temporales y espaciales del algoritmo crecerían linealmente conforme la red fuera procesando los tokens. Por ello, en estos casos, la historia de la red se puede *truncar* y se considera irrelevante cualquier información anterior a $t_0$ instantes de tiempo. El valor $t_0$ se conoce como *umbral de truncamiento* y la técnica resultante como *retropropagación en el tiempo truncada*.
```

Vamos a derivar las ecuaciones de BPTT para una red recurrente de Elman con la dinámica definida por las ecuaciones del bloque {eq}`ec-rrs1y` y que desplegada en el tiempo tiene el aspecto de la {numref}`fig-bptt`. La red neuronal de esta figura es una red no recurrente con lo que las derivadas de la función de error serán las mismas que las calculadas con la técnica de *retropropagación*, de la que no mostraremos aquí los detalles. Si se utiliza el descenso por el gradiente, el algoritmo se limita a actualizar cada peso (no se muestran las ecuaciones de los sesgos) mediante la llamada *regla delta generalizada* como sigue:

$$
\begin{eqnarray}
\Delta W^{y,x}_{i,j}[t] & = & \alpha \, \delta^Y_i[t] \, x_j[t] \\[2ex]
\Delta W^{x,x}_{i,j}[t] & = & \alpha \sum_{\tau=1}^{t} \delta^X_i[\tau] \,
x_j[\tau-1] \\[2ex]
\Delta W^{x,u}_{i,j}[t] & = & \alpha \sum_{\tau=1}^{t} \delta^X_i[\tau] \,
u_j[\tau] 
\end{eqnarray}
$$

donde la *señal de error* $\delta^Y$ y la *señal de error retropropagada* $\delta^X$ se definen a partir de:

$$
\begin{eqnarray}
\delta^Y_i[t] & = & \frac{\partial E[t]}{\partial Y_i[t]} \\[2ex]
\delta^X_i[t] & = & g_X'(X_i[t]) \sum_{j=1}^{n_Y} \delta^Y_j[t] \, W^{y,x}_{j,i} 
\end{eqnarray}
$$

y para $1 \leq \tau < t$,

$$
\delta^X_i[\tau] = g_X'(X_i[\tau]) \sum_{j=1}^{n_X}
\delta^X_j[\tau+1]  W^{x,x}_{j,i} 
$$

Excepto en el caso, poco empleado en la práctica, de que los pesos se actualicen tras ver cada token, el valor de la derivada es el [mismo] tanto si se usa RTRL como si se usa BPTT para su cálculo. La complejidad temporal del [primero][rtrl] es $n_X^4$ (asumiendo que $n_X > n_U$) y la del [segundo][bptt] es $n_X^2$. La complejidad espacial de BPTT es mayor, por otro lado, y su implementación un poco más compleja.

[bptt]: https://www.dlsi.ua.es/~mlf/nnafmc/pbook/node28.html
[rtrl]: https://www.dlsi.ua.es/~mlf/nnafmc/pbook/node29.html

## El problema del gradiente evanescente

Aunque teóricamente el estado de una RNR puede almacenar toda la información relevante sobre la historia de una secuencia, la práctica totalidad de los algoritmos de entrenamiento encuentran grandes problemas (en ocasiones insalvables) para *mantener* esta información, especialmente cuando el intervalo de tiempo entre la presencia de una determinada entrada y la salida deseada correspondiente es relativamente largo. Esto hace que a la hora de la verdad muchas RNR tengan poca ventaja sobre las redes no recurrentes con ventana temporal.

Los algoritmos de entrenamiento de RNR suelen ser inacapaces de constatar las dependencias a largo plazo debido a que la salida actual de la red es muy poco sensible a una entrada antigua, esto es, $\partial y[t+k] / \partial W[t]$ tiende a cero cuando $k$ aumenta para cualquier peso $W$. 

```{admonition} Nota
:class: note
Aunque la demostración es más compleja, para comprender aproximadamente por qué ocurre esto, puedes pensar en el algoritmo BPTT y en el hecho de que la derivada parcial de la función de pérdida respecto a un peso que se encuentra en una capa muy inferior se obtiene mediante la regla de la cadena como el producto de diferentes derivadas parciales encadenadas; si los valores de estas derivadas parciales son menores de la unidad, se producirá el desvanecimiento exponencial de la información del gradiente; si son mayores que la unidad, se producirá el efecto contrario, conocido como explosión del gradiente, que producirá igualmente una inestabilidad excesiva en el entrenamiento al aumentar los pesos exageradamente y provocar la saturación de las neuronas. 
```

Las unidades LSTM que estudiaremos a continuación sustituyen a las neuronas convencionales en las capas de estado de la RNR para intentar mitigar el problema del gradiente evanescente en base a la idea, que no desarrollaremos aquí, de asegurar lo que se conoce como *flujo de error constante* a través de ellas. Las celdas de una unidad LSTM tienen un *carrusel* que asegura este flujo de error constante y pueden guardar un valor indefinidamente; las compuertas de entrada vetan las entradas indeseadas al carrusel o permiten que este se vea modificado cuando corresponda; las compuertas de salida impiden que el contenido de la celda influya en el resto de la red hasta que sea el momento oportuno. El algoritmo de entrenamiento aprenderá idealmente a abrir y cerrar estas compuertas cuendo corresponda. La gestión de las dependencias a muy largo plazo en los carruseles permite que la red LSTM pueda detectar adecuadamente eventos interdependientes separados por decenas o cientos de instantes de tiempo, mientras que las RNR tradicionales no suelen ser capaces de manejar correctamente intervalos superiores a unos pocos instantes de tiempo.

En el capítulo 7 de esta [tesis][tesis] se analiza las activaciones de las distintas compuertas de una red LSTM que ha aprendido a predecir el lenguaje $a^nb^nc^n$. Para una consulta rápida, la {numref}`fig-anbncn` muestra una de las gráficas más representativas de dicho capítulo.

[tesis]: https://www.dlsi.ua.es/~japerez/pub/pdf/tesi2002.pdf


```{figure} images/rnr-anbncn.png
---
height: 800px
name: fig-anbncn
---
Activaciones en una unidad LSTM con dos celdas que forma parte de una red neuronal recurrente que ha aprendido el lenguaje $a^nb^nc^n$.
```

## Unidades LSTM

Para comprender el modelo de memoria a corto y largo plazo (LSTM, por el inglés *long short-term memory*) es fundamental conocer el problema del gradiente evanescente que las motiva y que se ha presentado más arriba.

El componente básico del modelo LSTM propuesto en 1997 por Hochreiter y Schmidhuber es el *bloque de memoria*, que contiene una o más *celdas* de memoria, una *compuerta de entrada* y una *compuerta de salida*. Las compuertas son unidades multiplicativas con activación continua (normalmente dentro del intervalo unidad) y son compartidas por todas las celdas que pertenecen a un mismo bloque de memoria. Cada celda contiene una unidad lineal con una conexión recurrente local llamada *carrusel de error constante* (CEC); la activación del CEC se conoce como el *estado* de la celda.

La {numref}`fig-basecell` muestra uno de estos bloques de memoria con una única celda; esta figura es útil también para introducir la notación utilizada.

```{figure} images/rnr-basecell.png
---
height: 280px
name: fig-basecell
---
Un bloque de memoria con una única celda. La entrada de la celda se representa con $Z$, la activación de la compuerta de entrada con $\phi$, la activación de la compuerta de salida con $\gamma$, la activación del CEC con $x$ y la activación global de la celda con $z$.
```

 La {numref}`fig-basetwocell` muestra un bloque de memoria con dos celdas que comparten las compuertas del bloque, aunque esta configuración ha caído en desuso. Cuando alguien habla de una *red recurrente LSTM* la mayoría de las veces se está refiriendo a una RNR similar a la red de Elman (probablemente con más de una capa de estado) en la que cada neurona convencional de la capa de estado se ha sustituido por un bloque de memoria LSTM con una única celda.

```{figure} images/rnr-basetwocell.png
---
height: 380px
name: fig-basetwocell
---
El bloque de memoria $i$-ésimo de una capa de una red LSTM con dos celdas por bloque.
```

Cada celda recibe como entrada una colección de valores (ponderados mediante los pesos correspondientes) provenientes de la entrada de la red y de las salidas de todas las celdas del modelo en el instante anterior. La compuerta de entrada se encarga de permitir o impedir el acceso de estos valores al CEC del interior de la celda. La compuerta de salida realiza una acción similar sobre la salida de la celda, tolerando o reprimiendo la difusión del estado del CEC al resto de la red. 

Los bloques de memoria configuran una red LSTM como puede verse en la {numref}`fig-lstm`, donde no se indican los sesgos de las distintas neuronas del modelo y solo hay una capa de estado.

```{margin} Valores no acotados.
Nótese cómo los valores de algunos componentes del estado, en especial la activación de los CEC, no están acotados.
```

```{figure} images/rnr-wholelstm.png
---
height: 560px
name: fig-lstm
---
Una red LSTM con una única capa oculta dos bloques de memoria de dos celdas cada uno. Solo se muestran algunas conexiones y no se muestran los sesgos. En este diagrama, a diferencia de la red de Elman, hay una conexión directa (con los pesos correspondientes) entre la entrada y la salida.
```

### Ecuaciones del modelo LSTM

Sean $n_U$, $n_Y$, $n_M$ y $n_C$ el número de neuronas de entrada, salida, bloques de memoria y celdas por bloque, respectivamente, de una configuración LSTM de tipo red de Elman con una capa de estado. La entrada en el instante $t$ se denota con $\boldsymbol{u}[t]$ y la salida correspondiente con $\boldsymbol{y}[t]$. La salida de la $j$-ésima celda del bloque $i$-ésimo se representa con $z_{ij}[t]$.

Como ya se vio antes, al representar los pesos los superíndices indican el cálculo en el que está involucrado el peso en cuestión: el "$\phi,z$" en $W^{\phi,z}$ indica que el peso se usa para calcular la activación de una compuerta de entrada ($\phi$) a partir de la de una celda ($z$); el "$\gamma$" en $W^{\gamma}$ indica que el sesgo se usa para calcular la activación de
una compuerta de salida. Los subíndices indican las unidades particulares afectadas por el peso y van paralelos a los superíndices.

La activación de la compuerta de entrada del $i$-ésimo bloque de memoria $\phi_i$ se calcula como:

$$
\Phi_i[t] & = & \sum_{j=1}^{n_M} \sum_{k=1}^{n_C}
   W^{\phi,z}_{i,jk} \, z_{jk} [t-1] +
   \sum_{j=1}^{n_U} W^{\phi,u}_{i,j} \, u_j[t] 
   + W^{\phi}_i \\[2ex]
\phi_i [t] & = & g_C( \Phi_i[t] )
$$

donde $g_C$ es la función de activación de todas las compuertas de la red (la función logística que devuelve valores en $[0,1]$, por ejemplo).

La activación de la compuerta de salida se calcula como sigue:

$$
\Gamma_i[t] & = & \sum_{j=1}^{n_M} \sum_{k=1}^{n_C}
   W^{\gamma,z}_{i,jk} \, z_{jk} [t-1] +
   \sum_{j=1}^{n_U} W^{\gamma,u}_{i,j} \, u_j[t] 
   + W^{\gamma}_i \\[2ex]
\gamma_i [t] & = & g_C( \Gamma_i[t] )
$$

El estado interno de la celda de memoria se calcula sumando la entrada modificada por la compuerta correspondiente con el estado en el instante anterior $t-1$:

$$
x_{ij}[t] = x_{ij}[t-1] + \phi_i[t] \, g_Z(Z_{ij}[t])
$$ (xsinforget)

donde $g_Z$ es una función de activación (normalmente sigmoidea y acotada) y:

$$
Z_{ij}[t] = \sum_{k=1}^{n_M} \sum_{l=1}^{n_C}
   W^{z,z}_{ij,kl} z_{kl} [t-1] +
   \sum_{k=1}^{n_U} W^{z,u}_{ij,k} \, u_k[t] + W^z_{ij}
$$

con $x_{ij} [0] = 0$ para todo $ij$. La salida de la celda se calcula ajustando el estado del CEC mediante una nueva función de activación $g_M$ y multiplicando el valor resultante por la activación de la compuerta de salida:

$$
z_{ij}[t] = \gamma_i[t] \, g_M(x_{ij}[t])
$$

Finalmente, si permitimos la conexión directa entre la entrada y las neuronas de salida, la salida global de la red se calcula mediante:

$$
\begin{eqnarray}
Y_i[t] & = & \sum_{j=1}^{n_M} \sum_{k=1}^{n_C}
   W^{y,z}_{i,jk} \, z_{jk} [t] +
   \sum_{j=1}^{n_U} W^{y,u}_{i,j} \, u_j[t] + W^y_i \\[2ex]
y_i[t] & = & g_Y( Y_i[t] )
\end{eqnarray}
$$

donde $g_Y$ es, otra vez, una función de activación adecuada.

Los pesos que inciden en las compuertas de entrada y salida se suelen iniciar de forma que $\phi_i[0]$ y $\gamma_i[0]$ estén cerca de $0$; de esta manera los bloques de memoria están desactivados inicialmente y el entrenamiento se centra en las conexiones directas entre la entrada y las neuronas de salida. Así, el protagonismo de los bloques de memoria va aumentando paulatinamente conforme el algoritmo de aprendizaje determina su rol.


### Limitación de la red LSTM original: reticencia a olvidar

El modelo inicial de la red LSTM ha sido aumentado desde su concepción original para superar algunos problemas detectados. Una de las principales modificaciones consistió en añadir las compuertas de olvido como se explica a continuación.

Cuando la red LSTM presentada hasta ahora se aplica a tareas de procesamiento de secuencias de longitud arbitrariamente larga, el modelo se vuelve inestable debido a que bajo determinadas circunstancias el estado de los CEC crece indefinidamente. Para paliar este problema, se incorpora una tercera compuerta a los bloques de memoria: la *compuerta de olvido*.

La compuerta de olvido puede rebajar e incluso anular el estado interno de la celda, esto es, la activación del CEC, cuando sus contenidos caducan. Estas compuertas permiten que la red LSTM pueda procesar establemente secuencias de longitud arbitrariamente larga.

La {numref}`fig-cell` muestra la nueva imagen de los bloques de memoria con la adición de la compuerta de olvido. Como ocurría con las compuertas de entrada y de salida, la compuerta de olvido es compartida por todas las celdas del bloque.

```{figure} images/rnr-cell.png
---
height: 400px
name: fig-cell
---
Un bloque de memoria con una compuerta de olvido con activación $\lambda$.
```

La activación de las compuertas de olvido $\lambda_i$ se obtiene calculando:

$$
\Lambda_i[t] & = & \sum_{j=1}^{n_M} \sum_{k=1}^{n_C}
   W^{\lambda,z}_{i,jk} \, z_{jk} [t-1] +
   \sum_{j=1}^{n_U} W^{\lambda,u}_{i,j} \, u_j[t] 
   + W^{\lambda}_i \\[2ex]
\lambda_i [t] & = & g_C( \Lambda_i[t] )
$$

Al considerar las compuertas de olvido, la ecuación {eq}`xsinforget` cambia su forma. El estado interno de la celda de memoria se calcula ahora sumando la entrada modificada por la compuerta correspondiente y el estado en el instante anterior $t-1$ multiplicado por la correspondiente compuerta de olvido:

$$
x_{ij}[t] = \lambda_i[t] \, x_{ij}[t-1] + \phi_i[t] \, g_Z(Z_{ij}[t])
$$

Los pesos de las compuertas de olvido se inicializan normalmente de manera que $\lambda_i[0]$ esté cerca de $1$; con esta inicialización, las celdas no olvidan nada hasta que aprendan cómo olvidar.

```{admonition} Nota
:class: note
Aunque las unidades LSTM siguen siendo ampliamente utilizadas en las RNR, con el paso de los años han aparecido variaciones del modelo inicial que mantienen su esencia, pero simplifican las ecuaciones para reducir el número de parámetros a entrenar. Una de las alternativas más conocidas son las *unidades recurrentes con compuertas* (GRU, por el inglés *gated recurrent unit*).
```

## Convergencia

Como apéndice final, a continuación se demuestra que con una RNR de Elman en el caso de que el entorno sea estacionario (es decir, que la distribución de los datos no cambie dinámicamente durante el aprendizaje), el entrenamiento se haga por épocas (es decir, se consideren todos los datos disponibles antes de reestimar los parámetros) y se utilice una función de error cuadrático, el mínimo de esta se produce cuando la salida $y_i[t]$ de la red es la probabilidad condicionada de obtener $\sigma_i$ después de haber
visto todos los tokens de la secuencia hasta el instante $t$.

En efecto, la contribución al error total debida al símbolo $s[t]$ de una de las secuencias viene dada, si consideramos la función de error cuadrático {eq}`ec:error`, por:

$$
\frac{1}{2} \sum_{i=1}^{n_Y} (d_i[t] - y_i[t])^2
$$ (ec-errorquad)

donde la salida deseada $\boldsymbol{d}[t]$ es la codificación *one-hot* del token $s[t+1]$. El error asociado al componente $i$-ésimo de la salida es, por tanto, $(1-y_i)^2$ si $s[t+1]=\sigma_i$, e $y_i^2$ en caso contrario.

Supongamos que $N$ secuencias de la muestra de entrenamiento tienen el prefijo $v=s[1],s[2],\ldots,s[t]$ en común y que de ellas $n$ continúan con el token $\sigma_i$ y $N-n$ con un símbolo distinto de $V - \{ \sigma_i \}$. Si estas $N$ secuencias comparten el mismo prefijo $v$, significa que el mismo estado $\boldsymbol{x}[t]$ y, por tanto, la misma salida $\boldsymbol{y}[t]$ serán obtenidos exactamente $N$ veces durante una época en el contexto de $v$. Entonces, puede considerarse el error acumulado debido al prefijo $v$ como:

$$
n (1- y_i[t])^2 + (N-n) (y_i[t])^2
$$

Derivando la ecuación anterior con respecto a $y_i[t]$, obtenemos:

$$
-2n (1 - y_i[t]) + 2(N- n) y_i[t]
$$

La segunda derivada es $2N > 0$. Luego el mínimo de la función de pérdida se obtiene cuando $y_i[t]= n/N$, es decir, cuando el valor predicho por la red neuronal para el token $\sigma_i$ tras leer el prefijo $v$ coincide con la frecuencia relativa con que $\sigma_i$ sigue a $v$. Un buen algoritmo de entrenamiento debería descubrir este mínimo.
