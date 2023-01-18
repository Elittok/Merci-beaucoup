def func (t,i):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new('RGB', (350,270), color=('#00FF00'))
    # Создаем объект со шрифтом
    font = ImageFont.truetype('C:/Windows/Fonts/Calibri.ttf', size=45)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100, 100),
        t,
        # Добавляем шрифт к изображению
        font=font,
        fill='#F0FFF0')
    im.show()
    im.save(f'C:/Users/user/Documents/142 группа/Могильный/image{i}.jpg')
t=['Никита',
   'Морозов',
   'Молодес']
for i in range(3):
    func(t[i],i)



