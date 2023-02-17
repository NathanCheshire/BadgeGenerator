![Author](./logo.png)

![Author](./badges/author_badge.png)

![Inspired](./badges/inspired_badge.png)

![Author](./badges/made_badge.png)

![Author](./badges/for_badge.png)

## Getting Started

First you'll want to setup a virtual environemnt and install the required packages:

- `python -m venv venv`
- `.\venv\Scripts\activate`

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
