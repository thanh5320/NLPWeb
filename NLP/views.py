
from django.shortcuts import render
from django.http import HttpResponse
from . import m_translate, m_text_recognition, m_summary, m_word_tokenize, m_sentiment_analysis
from django.db import models
from PIL import Image
from .forms import Img
import docx
from fpdf import FPDF
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from array import array

# tạo trang chủ
def index(request):
    return render(request, 'pages/home.html')

# tạo trang dịch văn bản
def translate(request):
    text1= request.POST.get('Text')
    submitbutton= request.POST.get('Submit')
    src=request.POST.get('ddselect1')
    dest=request.POST.get('ddselect2')
    text2 =''
    if (text1!=None):
        text2=m_translate.googletran(text1, src, dest)
    context= {'text1': text1, 'text2': text2,
              'submitbutton': submitbutton}
    return render(request, 'pages/translate.html', context)

# tạo trang dịch tài liệu
def translate2(request):
    text1= request.POST.get('text')
    submitbutton= request.POST.get('Submit')
    src=request.POST.get('ddselect1')
    dest=request.POST.get('ddselect2')
    text2 =''

    if text1!=None:
        text2=m_translate.googletran(text1, src, dest)

    context= {'text1': text1, 'text2': text2,
              'submitbutton': submitbutton}
        
    return render(request, 'pages/translate2.html', context)


#tạo trang nhận dạng chữ viết
def text_recognition(request):
    text=''
    img = request.FILES.get('img')
    fo = request.POST.get('format')
    submitbutton= request.POST.get('submit')
    
    if request.method == 'POST' and img!=None:
        im = Image.open(img) 
        text=m_text_recognition.chay(im)
        print(fo)
        if fo=='txt':
            print("mo txt")
            f = open(r'C:\Users\NGUYEN VAN THANH\Desktop\NLPWeb\NLP\static\download\txt.txt', 'w')
            f.write(text)
        if fo=='docx':
            mydoc = docx.Document()
            l=len(text)
            t1=text[0:l-1]
            mydoc.add_paragraph(t1)
            mydoc.save(r'C:\Users\NGUYEN VAN THANH\Desktop\NLPWeb\NLP\static\download\docx.docx')
        if fo =='pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_xy(10, 10)
            pdf.set_font('arial', 'B', 13.0)
            pdf.multi_cell (h = 5.0, align = 'L', w = 0, txt = text, border = 0)
            pdf.output(r'C:\Users\NGUYEN VAN THANH\Desktop\NLPWeb\NLP\static\download\pdf.pdf', 'F')
            
    context= {'fo': fo, 'submitbutton': submitbutton,'text' : text}

    return render(request, 'pages/text_recognition.html', context )

# tóm tắt văn bản
def summary(request):
    return render(request, 'pages/summary.html')

#tóm tắt trang web
def summary_web(request):
    text= request.POST.get('Text')
    submitbutton= request.POST.get('Submit')
    x=''
    if (text!=None):
        x=m_summary.Summary_web(text)

    context= {'text': x, 'text2': text, 'submitbutton': submitbutton}
        
    return render(request, 'pages/summary_web.html', context)

# tóm tắt tài liệu
def summary_text(request):
    text= request.POST.get('text')
    submitbutton= request.POST.get('Submit')
    x=''
    if (text!=None):
        x=m_summary.Summary_text(text)
    context= {'text': x, 'submitbutton': submitbutton}
        
    return render(request, 'pages/summary_text.html', context)

#phân tách từ phân tách câu
def word_tokennize(request):
    lang=request.POST.get('lang')
    text= request.POST.get('Text')
    submitbutton= request.POST.get('Submit')
    x=''
    if (text!=None and lang=='en'):
        x=m_word_tokenize.posstaggingEn(text)
    if (text!=None and lang=='vi'):
        x=m_word_tokenize.posstaggingVi(text)
    context= {'text': x, 'text2': text, 'submitbutton': submitbutton}
        
    return render(request, 'pages/word_tokenize.html', context)

# trang help
def help(request):
    return render(request, 'pages/help.html')

#phân tích cảm xúc
def sent_analysis(request):
    text= request.POST.get('Text')
    submitbutton= request.POST.get('Submit')
    out0=0.0
    out1=0.0
    out2=0.0
    out3=0.0
    if (text!=None):
        x=m_sentiment_analysis.analysis(text)
        out0=x[0]
        out1=x[1]
        out2=x[2]
        out3=x[3]

    context= {'out0': str(out0),'out1': str(out1),'out2': str(out2),'out3': str(out3), 'text2': text, 'submitbutton': submitbutton}
    return render(request, 'pages/sentiment_analysis.html', context)