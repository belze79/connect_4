from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import PhotoImage
from game_data_handler import game_data
import f4_session_store as store

def create_table_image(color : str) -> tuple[PhotoImage, PhotoImage]:
    base = Image.new('RGBA', (store.canvas_width * 8, store.canvas_height * 8), color)
    mask = Image.new('L', base.size, 255)
    draw = ImageDraw.Draw(mask)
    for coordinate in game_data.cells.keys():
        maggiorato = [x * 8 for x in game_data.cells[coordinate].square_points]
        draw.ellipse(tuple(maggiorato), fill=0)
    base.putalpha(mask)
    enabled = base.resize((store.canvas_width, store.canvas_height))
    alpha = enabled.split()[3].point(lambda p : int(p * 0.1))
    disabled = enabled.copy()
    disabled.putalpha(alpha)
    return ImageTk.PhotoImage(enabled), ImageTk.PhotoImage(disabled)


def get_state_image_button(text : str, width : int, height : int, bg_color : str, fg_color : str) -> tuple[PhotoImage, PhotoImage, PhotoImage]:
    w, h = width * 8, height * 8
    upper_text = text.upper()
    font = ImageFont.truetype('/home/belzebu/Fonts/Roboto_Condensed/RobotoCondensed-Bold.ttf', int(h * 0.7))
    image = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    tx1, ty1, tx2, ty2 = draw.textbbox((0, 0), upper_text, font=font)
    text_w, text_h = tx2 - tx1, ty2 - ty1
    draw.rounded_rectangle((0, 0, w, h), radius=25 * 8, fill=bg_color)
    text_position = (w - text_w) // 2, (h - text_h) // 2 - ty1
    draw.text(text_position, upper_text, font=font, fill=fg_color)
    hover = image.resize((width, height))
    normal_alpha = hover.split()[3].point(lambda p : int(p * 0.8))
    disabled_alpha = hover.split()[3].point(lambda pixel : int(pixel * 0.1))
    normal = hover.copy()
    normal.putalpha(normal_alpha)
    disabled = hover.copy()
    disabled.putalpha(disabled_alpha)
    return ImageTk.PhotoImage(normal), ImageTk.PhotoImage(hover), ImageTk.PhotoImage(disabled)

def get_text_image(text : str, font_size : int, text_color : str | tuple[int, int, int]) -> PhotoImage:
    h = font_size * 8
    upper_text = text.upper()
    font = ImageFont.truetype('/home/belzebu/Fonts/Roboto_Condensed/RobotoCondensed-Bold.ttf', int(h * 1.2))
    temp_img = Image.new('RGB', (1, 1))
    draw_temp = ImageDraw.Draw(temp_img)
    tx1, ty1, tx2, ty2 = draw_temp.textbbox((0, 0), upper_text, font=font)
    text_w, text_h = tx2 - tx1, ty2 - ty1
    img = Image.new('RGBA', (int(text_w), h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    text_position = 0, (h - text_h) // 2 - ty1
    draw.text(text_position, upper_text, font=font, fill=text_color)
    resized = img.resize((text_w // 8, font_size))
    final = resized.crop(resized.getbbox())
    return ImageTk.PhotoImage(final)