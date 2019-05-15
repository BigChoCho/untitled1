import pytesseract as pt

from PIL import Image
#獲取圖片
image = Image.open(r"C:\Users\a3858\PycharmProjects\untitled1\py-re-56-80\image\a1.png")
#把圖片轉換成文字
text = pt.image_to_string(image)
print(text)