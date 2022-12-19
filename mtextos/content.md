
Content in Jupyter Book
=======================

There are many ways to write content in Jupyter Book. This short section
covers a few tips for how to do so.

## Jupiter Book

This book contains information about the planet Jupiter - the fifth planet from the sun and the largest planet in the solar system! {numref}`jupiter-figure` below shows an image of Jupiter captured by the Hubble Space Telescope on June 27, 2019.

```{figure} https://solarsystem.nasa.gov/system/resources/detail_files/2486_stsci-h-p1936a_1800.jpg
---
height: 300px
name: jupiter-figure
---
The beautiful planet Jupiter! Source: [NASA](https://solarsystem.nasa.gov/resources/2486/hubbles-new-portrait-of-jupiter/?category=planets_jupiter).
```


## The Mass of Jupiter

We can estimate the mass of Jupiter from the period and size of an object orbiting it. For example, we can use Jupiter's moon Callisto to estimate it's mass.

Callisto's period: $p_{c}=16.7 days$

Callisto's orbit radius: $r_{c}=1,900,000 km$

Now, using [Kepler's Law](https://solarsystem.nasa.gov/resources/310/orbits-and-keplers-laws/) we can work out the mass of Jupiter.

```{math}
:label: eq1
m_{j} \approx \frac{r_{c}}{p_{c}} \times 7.9 \times 10^{10}
```

```{math}
:label: eq2
m_{j} \approx 1.9 \times 10^{27} kg
```

$$
  m_{j} \approx 1.9 \times 10^{27} kg
$$

```{margin} Did you know?
Jupiter is 11.0x larger than Earth!
```

```{note}
I am a useful note!
```

```{hint}
NASA provides a lot more information about the physical characteristics of Jupiter [here](https://solarsystem.nasa.gov/planets/jupiter/by-the-numbers/).
```

