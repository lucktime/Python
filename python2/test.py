#!/usr/bin/env python  # -*- coding: utf-8 -*-
import  sys
import argparse
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing, Image
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm , cm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import  Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
#from svglib.svglib import svg2rlg
import  sys
#from PIL import Image
from reportlab.lib.utils import ImageReader

#----------------------------------------------------------------------
import argparse

class RotatedImage(Image):

    def wrap(self,availWidth,availHeight):
        h, w = Image.wrap(self,availHeight,availWidth)
        return w, h
    def draw(self):
        self.canv.rotate(90)
        Image.draw(self)


def createBarCodes(from_address , to_address, code ,file_type,  way):
    """
    way = 1 :  syd -> pvg
    way = 2 :  pvg -> syd
    """
    file_path = '/Users/liujian/Documents/bntake-website-api/bntake2/web/python'
    web_path = '/Users/liujian/Documents/bntake-website-api/bntake2/web/python'
    pdfmetrics.registerFont(TTFont('RegularFont', file_path + '/Fonts/OpenSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('BoldFont', file_path+'/Fonts/OpenSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('msjhFont', file_path+'/Fonts/msjh.ttf'))

    filename = web_path + '/pdf/'+code+".pdf"

    c = canvas.Canvas(filename, pagesize=A4)

    #if from_address.len() == 0

    #from_address = "Jonathan Chak<br/>Bntake Pty Ltd<br/>Level 9, 17-19 Bridge Street<br/>Sydney NSW 2000 Australia"

    #to_address = "刘先生<br/>Bntake控股<br/>中国 上海 浦东新区 ＡＡ路11弄11号101室<br/>"


    #barcode_value = "N2S300000034SYAU"
    barcode_value = code

    barcode128 = code128.Code128(barcode_value, barHeight=4*cm, barWidth=1.5)
    # the multiwidth barcode appears to be broken
    #barcode128Multi = code128.MultiWidthBarcode(barcode_value)

    width, height = A4 #keep for later
    #print width, height

    #draw code
    c.drawString(9*cm, 15.8*cm, barcode_value)

    barcode128.drawOn(c,5*cm,16.3*cm);  #draw barcode on c

    qr_code = qr.QrCodeWidget(barcode_value)
    bounds = qr_code.getBounds()
    b_width = bounds[2] - bounds[0]
    b_height = bounds[3] - bounds[1]
    d = Drawing(158, 158, transform=[158./b_width,0,0,158./b_height,0,0])
    d.add(qr_code)
    renderPDF.draw(d, c, 0.3*cm, 15.5*cm)  #draw qrcode on c

    # #draw right side
    if way == '1' :
        fly = file_path + "/syd_pvg.jpg"
    else:
        fly = file_path + "/pvg_syd.jpg"
    c.drawImage(fly, 17.5*cm, 15.5*cm,2.5*cm,13*cm)

    #draw contact name
    c.setFont("BoldFont", 20)
    text = "From"
    c.drawString(1*cm, 27.8*cm, text)
    c.setFont("msjhFont", 20)
    text = "发件人"
    c.drawString(3*cm, 27.8*cm, text)

    c.setFont("BoldFont", 20)
    text = "To"
    c.drawString(10*cm, 27.8*cm, text)
    c.setFont("msjhFont", 20)
    text = "收件人"
    c.drawString(11.2*cm, 27.8*cm, text)

    #text = from_address
    #c.drawString(1*cm, 21.3*cm, text)
    ps = ParagraphStyle('test')
    ps.fontName = "msjhFont"
    ps.fontSize = 12
    ps.textColor = 'black'
    ps.leading = 18

    p = Paragraph(from_address,ps)
    p.wrapOn(c,7.5*cm,100)
    p.drawOn(c,1*cm,24.2*cm)

    p = Paragraph(to_address,ps)
    p.wrapOn(c,7.5*cm,100)
    p.drawOn(c,10*cm,24.2*cm)

    #draw content
    c.setFont("msjhFont", 14)
    text = file_type
    c.drawString(1*cm, 21.3*cm, text)

    text = "包装内容"
    c.setFont("msjhFont", 20)
    c.drawString(7.2*cm, 22.2*cm, text)

    text = "Package Content"
    c.setFont("BoldFont", 20)
    c.drawString(1*cm, 22.2*cm, text)

    #draw dash line
    c.setDash(6,3)
    c.line(0,14.6*cm,width,14.6*cm) #x1 , y1 , x2, y2

    #draw bntake
    c.setFont("RegularFont", 12)
    text = "www.bntake.com"
    c.drawString(1.4*cm, 15.7*cm, text)

    c.setFont("BoldFont", 18)
    text = "FOLD HERE"
    c.drawString(16.5*cm, 13.8*cm, text)

    #draw Delaration text
    c.setFont("BoldFont", 20)
    text = "Delaration to Assign"
    c.drawString(1*cm, 12.7*cm, text)

    text = "客户声明"
    c.setFont("msjhFont", 20)
    c.drawString(8.5*cm, 12.7*cm, text)
    #draw signature
    signature = file_path + "/img_signature.jpg"
    c.drawImage(signature, 1*cm, (1.3)*cm ,19*cm, 2*cm)

    #draw declaration
    signature = file_path + "/img_declaration_eng.jpg"
    c.drawImage(signature, 1*cm, (3.9)*cm , 18.7*cm , 8.25*cm)

    # c.setFont("Helvetica", 20)
    # text = "Signature:"
    # c.drawString(1*cm, 1*cm, text)
    #
    # c.line(4.5*cm,1*cm,10*cm,1*cm) #x1 , y1 , x2, y2

    #origin
    #text = "a"
    #c.drawString(0*cm, 0*cm, text)
    #c.drawString(width-1*cm, height-1*cm, text)
    #c.drawString(0*cm, height-1*cm, text)
    #c.drawString(width-1*cm, 0*cm, text)


    c.save()  #write file
    print filename


parser = argparse.ArgumentParser()
parser.add_argument("--getfile", help="increase output verbosity",
                    action="store_true")
parser.add_argument("from_address",type=str, help="from address")
parser.add_argument("to_address",type=str, help="to address")
parser.add_argument("code",type=str, help="code")
parser.add_argument("file_type",type=str, help="file_type")
parser.add_argument("way",type=str, help="way")
args = parser.parse_args()
if args.getfile:
   print "verbosity turned on"
   #print 'Number of arguments:', len(sys.argv), 'arguments.'
   #print 'Argument List:', str(sys.argv)
   #print args.from_address
   #print args.to_address
   #print args.code
   #print args.way
   filename = createBarCodes(args.from_address, args.to_address, args.code, args.file_type, args.way )

   print filename
