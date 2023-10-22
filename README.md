![Author](./logo.png)

![Author](./badges/author_badge.png)

![Inspired](./badges/inspired_badge.png)

![Author](./badges/made_badge.png)

![Author](./badges/for_badge.png)

## Getting Started

First you'll want to setup a virtual environment:

`python -m venv venv` or `python3 -m venv venv`

Note you can replace the second venv with whatever you want ot name your virtual environment.
Now that we have our environment, we need to enter it. If you're on Windows simply:

`.\venv\Scripts\activate`

If you're on Mac OSX, you'll need to source it:

`source ./venv/bin/activate`

Now you can install the requirements once inside of the virtual environment:

`pip install -r requirements.txt`

Now you can run the script with the following arguments:

Required:
- -lt (--left_text) - the text for the left of the badge
- -rt (--right_text) - the text for the right of the badge
- -fp (--font_path) - the path to the true-type font to use for the badge text
- -ts (--text_size) - the size of the text
- -sn (--save_name) - the name to save the resulting PNG as

Optional:
- -hp (--horizontal_padding) - the padding between the text and the horizontal borders
- -vp (--vertical_padding) - the padding between the text and the vertical borders
- -tc (--text_color) - the color for the text in the format "red,green,blue"
- -lbc (--left_background_color) - the color for the left side of the badge in the format "red,green,blue"
- -rbc (--right_background_color) - the color for the right side of the badge in the format "red,green,blue"
