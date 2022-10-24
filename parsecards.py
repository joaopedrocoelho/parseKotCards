from cmath import nan
from statistics import quantiles
import pandas as pd
from PIL import Image, ImageDraw, ImageFont;
import textwrap



cards = pd.read_excel('KingOfTokyo_CardList_xls.xlsx')

cardsList = []

for index, row in cards.iterrows():
    if str(row["Name"]) != 'nan':
        cardsList.append({
            "name": str(row['Name']),
            "type": row['Type'],
            "ability": row['Ability']
        })


fontMedium = ImageFont.truetype("Roboto-Bold.ttf", 17) 
fontItalic = ImageFont.truetype("Roboto-Italic.ttf", 12)
fontRegular = ImageFont.truetype("Merge3.ttf", 15)
width = 375
height = 130

def draw_multiple_line_text(image, draw, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=50)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color, align="left")
        y_text += line_height

def renderCard(card, index):
    print(str(card['name']) + " " + str(index))
    img = Image.new('RGB', (width, height), color = 'white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([width -1 , 0, 0, height ], outline="black", width=2)
    draw.text([5, 0, 2, 0 ], card['name'], font=fontMedium, fill="black", align="center")
    draw.text([330, 0, 2, 0 ], card['type'], font=fontItalic, fill="black", align="center")
    
    draw_multiple_line_text(img, draw, card['ability'], fontRegular, "black", 25)  

    img.save(card['name'] + '.png', dpi=(150,150), quality=100)
    
for i, card in enumerate(cardsList):
    renderCard(card, i)
