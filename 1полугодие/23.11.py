from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (300,200), color=('#FAACAC'))
# Создаем объект со шрифтом
font = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', size=18)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (100, 100),
    'Текст 18px',
    # Добавляем шрифт к изображению
    font=font,
    fill='#1C0606')
im.show()
