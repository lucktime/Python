#_*_coding:utf8_*_
#！/usr/local/bin/python    MAC
# Filename: pdftopng
#intend: 用于将pdf文件转换成png
#web:http://garmoncheg.blogspot.com.au/2013/07/python-converting-pdf-to-image.html


from wand.image import Image
# Converting first page into JPG
with Image(filename="/Users/liujian/Documents/python/12.pdf") as img:
    img.save(filename="temp.jpg")
# Resizing this image
#with Image(filename="/temp.jpg") as img:
#    img.resize(200, 150)
#        img.save(filename="/thumbnail_resize.jpg")
