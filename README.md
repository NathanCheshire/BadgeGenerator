# BadgeGenerator

![Author](./badges/author_badge.png)

![InspiredBy](./badges/inspired_badge.png)

![MadeWith](./badges/made_badge.png)

![ForTheBadge](./badges/for_badge.png)

## Getting Started

First, you'll want to set up a virtual Python environment from which to execute the script:

`python -m venv badge-generator-venv` or `python3 -m venv badge-generator-venv`

Now that we have our environment we need to enter it. If you're on Windows simply:

`.\badge-generator-venv\Scripts\activate`

If you're on Mac OSX, you'll need to source it:

`source ./badge-generator-venv/bin/activate`

Now you can install the requirements once inside of the virtual environment:

`pip install -r requirements.txt`

Now you can run the script with the following arguments:

Required:

- -lt (--left_text): the text for the left of the badge
- -rt (--right_text): the text for the right of the badge

Optional:

- -sn (--save_name): the name to save the resulting PNG as, defaults to `left_text`_`right_text`
- -fp (--font_path): the path to the [true-type](https://en.wikipedia.org/wiki/TrueType) font to use for the badge left and right text, defaults to `./fonts/oswald-semi-bold.ttf`
- -ts (--text_size): the size of the text, defaults to `26`
- -hp (--horizontal_padding): the padding between the text and the horizontal borders, defaults to `15`
- -vp (--vertical_padding): the padding between the text and the vertical borders, defaults to `10`
- -tc (--text_color): the color for the text in the format "red,green,blue", defaults to `245,245,245`
- -lbc (--left_background_color): the color for the left side of the badge in the format "red,green,blue", defaults to `5,83,131`
- -rbc (--right_background_color): the color for the right side of the badge in the format "red,green,blue", defaults to `85,147,199`

You can use `deactivate` to leave the virtual environment.

## Quick start

`python -m venv badge-generator-venv && source ./badge-generator-venv/bin/activate && pip install -r requirements.txt`
