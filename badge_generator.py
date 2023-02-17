import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw
import argparse


def export_string_badge(left_text: str, 
                        right_text: str, 
                        font_path: str,
                        font_size: int,
                        save_name: str,
                        horizontal_padding: int,
                        vertical_padding: int,
                        text_color: tuple,
                        left_background_color: tuple,
                        right_background_color: tuple):
    """ 
    Exports a badge image to the current directory, constructed using the provided parameters.

    :param left_string: the string for the left of the badge
    :param right_string: the string for the right of the badge
    :param font_path: the path to the true-type font to use for the painted strings
    :param font_size: the size for the font
    :param save_name: the name to save the png as
    :param horizontal_padding: the left/right padding between the image borders and words
    :param vertical_padding: the top/bottom padding between the image borders and words
    :param text_color: the color for the text painted by left_string and right_string as a bgr tuple
    :param left_background_color: the color used for the badge's left background as a bgr tuple
    :param right_background_color: the color used for the badge's right background as a bgr tuple
    """

    local_font = ImageFont.truetype(font_path, font_size)

    left_width = get_text_size(left_text, font_size, font_path)[0]
    right_width_height = get_text_size(right_text, font_size, font_path)
    beta_width = right_width_height[0]
    text_height = right_width_height[1]

    full_width = (horizontal_padding + left_width
                  + 2 * horizontal_padding + beta_width + horizontal_padding)
    full_height = vertical_padding + text_height + vertical_padding

    blank_image = np.zeros((full_height, full_width, 3), np.uint8)
    alpha_color_drawn = cv2.rectangle(blank_image, (0, 0),
                                      (left_width + 2 *
                                       horizontal_padding, full_height),
                                      left_background_color, -1)
    beta_color_drawn = cv2.rectangle(alpha_color_drawn, (left_width + horizontal_padding, 0),
                                     (full_width, full_height), right_background_color, -1)

    base_colors_done = Image.fromarray(beta_color_drawn)

    draw = ImageDraw.Draw(base_colors_done)
    left_anchor = (horizontal_padding / 2, vertical_padding)
    draw.text(left_anchor, left_text, font=local_font, fill=text_color)

    draw = ImageDraw.Draw(base_colors_done)
    left_anchor = (left_width + horizontal_padding * 2 + horizontal_padding / 2, vertical_padding)
    draw.text(left_anchor, right_text, font=local_font, fill=text_color)

    cv2.imwrite(save_name + '.png', np.array(base_colors_done))


def get_text_size(text: str, font_size: int, font_name: str) -> tuple:
    """ 
    Returns a tuple of the size (width, height) required to hold the provided 
    string with the provided font and point size.
    """
    font = ImageFont.truetype(font_name, font_size)
    bounding_box = font.getbbox(text)
    return bounding_box[2], bounding_box[3]

def parse_tuple_color_from_bgr_string(rgb_string: str) -> tuple:
    """
    Parses an rgb tuple from the provided bgr string of the format: "b,g,r".
    """
    parts = [int(part.strip()) for part in rgb_string.split(",")]

    if len(parts) != 3:
        raise Exception(f"Invalid color parts length: {len(parts)}, provided string: \"{rgb_string}\"")
    
    return parts[2], parts[1], parts[0]

def main():
    parser = argparse.ArgumentParser(prog='Badge Generator', description="Generates colorful and pretty badges with text")
    parser.add_argument('-lt', '--left_text', 
                        required=True,
                        help='the left text of the badge')
    parser.add_argument('-rt', '--right_text', 
                        required=True,
                        help='the right text of the badge')
    parser.add_argument('-fp', '--font_path',
                        required=True,
                        help='the relative or absolute path to the true-type font to use for the badge text')
    parser.add_argument('-ts', '--text_size',
                        required=True,
                        help='the size of the text')
    parser.add_argument('-sn', '--save_name',
                        required=True,
                        help='the name to save the png badge as')
    parser.add_argument('-hp', '--horizontal_padding',
                        default=15,
                        help='the horizontal padding of the text and badge edges')
    parser.add_argument('-vp', '--vertical_padding',
                        default=10,
                        help='the vertical padding of the text and badge edges')
    parser.add_argument('-tc', '--text_color',
                        default='245,245,245',
                        help='the color of the text to use in the format "r,g,b"')
    parser.add_argument('-lbc', '--left_background_color',
                        default='5,83,131',
                        help='the color of the text to use in the format "r,g,b"')
    parser.add_argument('-rbc', '--right_background_color',
                        default='85,147,199',
                        help='the color of the text to use in the format "r,g,b"')

    args = parser.parse_args()

    text_color = parse_tuple_color_from_bgr_string(args.text_color)
    left_background_color = parse_tuple_color_from_bgr_string(args.left_background_color)
    right_background_color = parse_tuple_color_from_bgr_string(args.right_background_color)
    
    export_string_badge(left_text=args.left_text, 
                        right_text=args.right_text, 
                        font_path=args.font_path, 
                        font_size=int(args.text_size), 
                        save_name=args.save_name,
                        horizontal_padding=int(args.horizontal_padding),
                        vertical_padding=int(args.vertical_padding),
                        text_color=text_color,
                        left_background_color=left_background_color,
                        right_background_color=right_background_color)

if __name__ == '__main__':
    main()