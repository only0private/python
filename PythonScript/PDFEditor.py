# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm

pdfFile = canvas.Canvas('./python1.pdf') #作成ファイル名
pdfFile.saveState()

#ファイル情報設定(省略可)
pdfFile.setAuthor('hamaguchi')  #作者名
pdfFile.setTitle('論文')        #タイトル
pdfFile.setSubject('サンプル')    #サブタイトル
 
# A4
pdfFile.setPageSize((21.0*cm, 29.7*cm))
# B5
#pdfFile.setPageSize((18.2*cm, 25.7*cm))
 
pdfFile.setFillColorRGB(0, 0, 100)  #塗りつぶし色設定
pdfFile.rect(2*cm, 2*cm, 12*cm, 24*cm, stroke=1, fill=1)  #(開始位置(左からの距離，下からの距離),終了位置(左からの距離，下からの距離)，他は変更しない)
pdfFile.setFillColorRGB(0, 0, 0)    #色の初期化
 
pdfFile.setLineWidth(1) #描写する線の太さ決定
pdfFile.line(10*cm, 20*cm, 10*cm, 10*cm)    #(開始位置(左からの距離，下からの距離),終了位置(左からの距離，下からの距離))
 
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))  #フォント
pdfFile.setFont('HeiseiKakuGo-W5', 10.5)  #文字サイズ
pdfFile.drawString(15*cm, 5*cm, 'あいうえおー')   #文章記述(左からの距離，下からの距離，文章)
 
pdfFile.restoreState()
pdfFile.save()
