# Minería de Textos, curso 2022-2023

Este repositorio contiene el código fuente para Jupyter Book de los materiales de la asignatura _Minería de Textos_ de la Universidad de Alicante. Los materiales resultantes pueden consultarse [aquí](https://jaspock.github.io/mtextos2223).

## Usage

### Building the book

If you'd like to develop on and build the book, you should:

- Clone this repository
- Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
- (Recommended) Remove the existing `mtextos/_build/` directory
- Run `jupyter-book build mtextos/`

A fully-rendered HTML version of the book will be built in `mtextos/_build/html/`.

### Hosting the book

The html version of the book is hosted on the `gh-pages` branch of this repo. A GitHub actions workflow has been created that automatically builds and pushes the book to this branch on a push or pull request to main.

If you wish to disable this automation, you may remove the GitHub actions workflow and build the book manually by:

- Navigating to your local build; and running,
- `ghp-import -n -p -f mtextos/_build/html`

This will automatically push your build to the `gh-pages` branch. More information on this hosting process can be found [here](https://jupyterbook.org/publish/gh-pages.html#manually-host-your-book-with-github-pages).

## Contributors

We welcome and recognize all contributions.

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/).
