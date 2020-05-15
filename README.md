[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO 
<br />
<p align="center">
  <a href="">
    <img src="data/images/logo.png" alt="Logo" width="80" height="80">
  </a>-->

  <h3 align="center">Minicode</h3>

  <p align="center">
    Generate minimalist code art
    <br />
    <a href="https://github.com/Gokender/minicode/issues">Report Bug</a>
    ·
    <a href="https://github.com/Gokender/minicode/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
  - [default](#default)
  - [fruity](#fruity)
  - [monokai](#monokai)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

![Screenshot][product-screenshot]


Minicode is a minimalist code image generator. It allows you to create PNG or SVG images from existing code. It is based on the Pygments library which allows to detect color syntax information specific to each programming language. 

This project is inspired by the work of [erdavids](https://github.com/erdavids/Simulated-Code).


Most of the variables used to generate the SVG file can be overload (more information in the [Usage](#usage) section).-->


### Built With

* [Python 3]()
* [Pygments](https://pygments.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Installation

1. Clone the repo
```sh
git clone https://github.com/Gokender/minicode.git
```
2. Install PIP packages
```sh
pip install -r requirements.txt
```

## Usage

To generate a new minimal code :

```shell
>> python minicode\cli.py
Saving file : minicode.svg

>> python minicode\cli.py --input this\is\an\example.py --output exemples\myfile
Saving file : exemples\myfile.svg
```

If you want to choose another language from Python (HTML for example):

```shell
>> python minicode\cli.py --lexer html
Saving file : minicode.svg
```

To choose a different theme :

```shell
>> python minicode\cli.py --theme monokai
Saving file : minicode.svg
```

The currently available themes are :
- default
- dracula
- fruity
- monokai 

You can generate an image from an url. This option will override the input file variable. The `--auto_size` arg choose for you the best width and height.

```shell
>> python minicode\cli.py --url https://raw.githubusercontent.com/dead-beef/markovchain/master/markovchain/parser.py -a
Saving file : minicode.svg
```

If `--png` is set the output will be PNG image instead of SVG.

```shell
>> python minicode\cli.py --url https://raw.githubusercontent.com/dead-beef/markovchain/master/markovchain/parser.py -a --png
Saving file : minicode.png
```

If you don't want to change the variable one by one you can update the default configuration file `config.ini`

Below the list of all variables you can change :

```shell
python minicode\cli.py --help
usage: cli.py [-h] [--width WIDTH] [--height HEIGHT] [--theme THEME]
              [--input INPUT] [--output OUTPUT] [--code_width CODE_WIDTH]
              [--code_height CODE_HEIGHT] [--start_position START_POSITION]
              [--radius_rect RADIUS_RECT] [--line_spacing LINE_SPACING] [-a]
              [--lexer LEXER] [--url URL] [--png]

optional arguments:
  -h, --help            show this help message and exit
  --width WIDTH         SVG width
  --height HEIGHT       SVG height
  --theme THEME         Syntax highlighting theme
  --input INPUT         Input filepath
  --output OUTPUT       Output filepath
  --code_width CODE_WIDTH
                        Width in pixel of character
  --code_height CODE_HEIGHT
                        Height in pixel of character
  --start_position START_POSITION
                        Starting pixel position
  --radius_rect RADIUS_RECT
                        Radius for rounded corner
  --line_spacing LINE_SPACING
                        Line spacing
  -a, --auto_size       Choose width & height for you
  --lexer LEXER         Code parser
  --url URL             Url to download
  --png                 Saving image in PNG
```

## Examples

### default

![default][screenshot-default]

### fruity

![fruity][screenshot-fruity]

### monokai

![monokai][screenshot-monokai]


## Roadmap

See the [open issues](https://github.com/Gokender/minicode/issues) for a list of proposed features (and known issues).


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Gauthier Chaty - [@gokender](https://twitter.com/gokender)

Project Link: [Minicode](https://github.com/Gokender/minicode.git)


## Acknowledgements

* [erdavids](https://github.com/erdavids) for the inspiration


[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: LICENSE.txt
[product-screenshot]: /docs/examples/screenshot.png
[screenshot-default]: /docs/examples/default.png
[screenshot-fruity]: /docs/examples/fruity.png
[screenshot-monokai]: /docs/examples/monokai.png
