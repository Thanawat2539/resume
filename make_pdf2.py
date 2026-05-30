# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---- Thai fonts ----
pdfmetrics.registerFont(TTFont("Thai", r"C:\Windows\Fonts\leelawad.ttf"))
pdfmetrics.registerFont(TTFont("ThaiB", r"C:\Windows\Fonts\leelawdb.ttf"))
pdfmetrics.registerFont(TTFont("Sym", r"C:\Windows\Fonts\seguisym.ttf"))
pdfmetrics.registerFontFamily("Thai", normal="Thai", bold="ThaiB", italic="Thai", boldItalic="ThaiB")
SY = '<font name="Sym">%s</font>'  # wrap symbol glyphs

# ---- Palette ----
INK    = colors.HexColor("#1f2937")
ACCENT = colors.HexColor("#2563eb")
GREEN  = colors.HexColor("#16a34a")
RED    = colors.HexColor("#dc2626")
GOLD   = colors.HexColor("#d97706")
SILVER = colors.HexColor("#64748b")
PURPLE = colors.HexColor("#7c3aed")
LIGHT  = colors.HexColor("#eff6ff")
GREY   = colors.HexColor("#6b7280")
LINEG  = colors.HexColor("#e5e7eb")

# ---- Styles ----
title   = ParagraphStyle("title", fontName="ThaiB", fontSize=21, textColor=INK, leading=26)
subtitle= ParagraphStyle("subtitle", fontName="Thai", fontSize=11.5, textColor=GREY, leading=16)
h2      = ParagraphStyle("h2", fontName="ThaiB", fontSize=14, textColor=ACCENT, leading=18, spaceBefore=6, spaceAfter=4)
body    = ParagraphStyle("body", fontName="Thai", fontSize=10.5, textColor=INK, leading=16)
cell    = ParagraphStyle("cell", fontName="Thai", fontSize=9.5, textColor=INK, leading=13)
cellb   = ParagraphStyle("cellb", fontName="ThaiB", fontSize=9.5, textColor=INK, leading=13)
cellw   = ParagraphStyle("cellw", fontName="ThaiB", fontSize=10, textColor=colors.white, leading=13)
cellc   = ParagraphStyle("cellc", fontName="Thai", fontSize=11, textColor=INK, leading=14, alignment=1)
note    = ParagraphStyle("note", fontName="Thai", fontSize=9, textColor=GREY, leading=13)

def P(t, s=cell): return Paragraph(t, s)

story = []

# ================= HEADER =================
story.append(Paragraph("เปรียบเทียบธุรกิจที่เหมาะกับเครื่องปริ้น 3D", title))
story.append(Spacer(1, 3))
story.append(Paragraph("สำหรับมือใหม่ &bull; ทุน ~20,000 บาท &bull; เน้นไลฟ์ขาย TikTok &bull; 30 พ.ค. 2569", subtitle))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=2, color=ACCENT))
story.append(Spacer(1, 12))

# ================= 0. PRINCIPLE =================
story.append(Paragraph("หลักคิด: 3D ปริ้น ชนะตรงไหน &mdash; แพ้ตรงไหน", h2))
princ = [
    [P((SY % "✔") + " เหมาะ เมื่อสินค้า...", cellw), P((SY % "✘") + " ไม่เหมาะ เมื่อสินค้า...", cellw)],
    [P("คัสตอม / ทำเฉพาะบุคคล", cell), P("ผลิตจำนวนมากราคาถูก (เคสจีน)", cell)],
    [P("Niche หายาก ของในร้านไม่มี", cell), P("ต้องผิวเนียนระดับฉีดพลาสติก", cell)],
    [P("ดีไซน์มีมูลค่า คนยอมจ่ายเพิ่ม", cell), P("ต้องผลิตเร็ว วันละหลายร้อยชิ้น", cell)],
    [P("ชิ้นเล็ก กำไรต่อกรัมสูง", cell), P("ชิ้นใหญ่ กินเวลา/ฟิลาเมนต์เยอะ", cell)],
]
t = Table(princ, colWidths=[81*mm, 81*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,0), GREEN),
    ("BACKGROUND", (1,0), (1,0), RED),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(Spacer(1, 14))

# ================= GROUP A =================
story.append(Paragraph("กลุ่ม A &mdash; เหมาะสุด (คอนเทนต์ปัง + กำไรดี + คู่แข่งไทยยังน้อย)", h2))
gA = [
    [P("สินค้า", cellw), P("ต้นทุน/ชิ้น", cellw), P("ราคาขาย", cellw), P("จุดเด่น", cellw)],
    [P("ของเล่นขยับได้ (มังกร/งู/ปลาหมึก)", cellb), P("10&ndash;25 ฿", cellc), P("79&ndash;199 ฿", cellc),
     P("ไวรัลที่สุดบน TikTok ปริ้นทีเดียวเสร็จทั้งตัว", cell)],
    [P("ฟิดเจ็ตคลายเครียด", cellb), P("5&ndash;15 ฿", cellc), P("49&ndash;149 ฿", cellc),
     P("ราคาเข้าถึงง่าย เด็ก/วัยรุ่นซื้อซ้ำ ถ่าย ASMR ดี", cell)],
    [P("ของขวัญคัสตอมใส่ชื่อ", cellb), P("10&ndash;30 ฿", cellc), P("99&ndash;299 ฿", cellc),
     P("กำไรสูง เกาะเทศกาล วาเลนไทน์/รับปริญญา", cell)],
]
t = Table(gA, colWidths=[52*mm, 24*mm, 24*mm, 62*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GOLD),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#fffbeb")]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
]))
story.append(t)
story.append(Spacer(1, 12))

# ================= GROUP B =================
story.append(Paragraph("กลุ่ม B &mdash; ดี (ดีมานด์นิ่ง ขายยาว แต่คอนเทนต์ธรรมดากว่า)", h2))
gB = [
    [P("สินค้า", cellw), P("จุดเด่น", cellw)],
    [P("ที่จัดระเบียบโต๊ะ (ที่วางมือถือ/เก็บสายชาร์จ/รีโมท)", cellb), P("ดีมานด์สม่ำเสมอ ปริ้นง่าย ขาย Shopee ได้ด้วย", cell)],
    [P("ของแต่งบ้าน/ต้นไม้ (กระถาง/แจกัน/โคมไฟ)", cellb), P("กำไรต่อชิ้นสูง สาย minimal/ต้นไม้ชอบ", cell)],
    [P("ของสะสม/งานอดิเรก (โมเดลอนิเมะ/มินิเกม/กันพลา)", cellb), P("กลุ่มลูกค้า passion จ่ายหนัก ตั้งราคาได้สูง", cell)],
]
t = Table(gB, colWidths=[88*mm, 74*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), SILVER),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
]))
story.append(t)
story.append(Spacer(1, 12))

# ================= GROUP C =================
story.append(Paragraph("กลุ่ม C &mdash; กำไรสูงแต่ต้องมีความรู้เฉพาะ (เน้น Shopee/รับสั่งทำ)", h2))
gC = [
    [P("สินค้า", cellw), P("จุดเด่น / ข้อควรรู้", cellw)],
    [P("อะไหล่ทดแทน/ชิ้นส่วนหายาก (ลูกบิด/คลิป/ขายึด)", cellb), P("กำไรโหด คู่แข่งแทบไม่มี แต่ไม่เหมาะไลฟ์ TikTok", cell)],
    [P("ป้าย/โลโก้/ของพรีเมียมให้ร้านค้า (B2B)", cellb), P("ออเดอร์ใหญ่ ลูกค้าประจำ แต่ต้องวิ่งหาลูกค้าเอง", cell)],
]
t = Table(gC, colWidths=[88*mm, 74*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PURPLE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f3ff")]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
]))
story.append(t)
story.append(Spacer(1, 14))

# ================= SCORE TABLE =================
story.append(Paragraph("ตารางสรุป: อันไหนเหมาะกับ &ldquo;ไลฟ์ TikTok ทุน 20,000&rdquo;", h2))
def stars(n): return SY % ("★"*n + "☆"*(5-n))
sc = [
    [P("ธุรกิจ", cellw), P("คอนเทนต์ไลฟ์", cellw), P("กำไร/ชิ้น", cellw), P("คู่แข่งไทย", cellw), P("เหมาะกับคุณ", cellw)],
    [P("ของเล่นขยับได้", cellb), P("สูงมาก", cellc), P("สูง", cellc), P("ปานกลาง", cellc), P(stars(5), cellc)],
    [P("ฟิดเจ็ต", cellb), P("สูงมาก", cellc), P("ปานกลาง", cellc), P("ปานกลาง", cellc), P(stars(4), cellc)],
    [P("ของขวัญใส่ชื่อ", cellb), P("สูง", cellc), P("สูงมาก", cellc), P("ปานกลาง", cellc), P(stars(4), cellc)],
    [P("เคสมือถือ Hybrid", cellb), P("สูง", cellc), P("สูง", cellc), P("สูง (ดุ)", cellc), P(stars(3), cellc)],
    [P("ของจัดระเบียบ", cellb), P("ปานกลาง", cellc), P("ปานกลาง", cellc), P("สูง (ดุ)", cellc), P(stars(3), cellc)],
    [P("อะไหล่ทดแทน", cellb), P("ต่ำ", cellc), P("สูงมาก", cellc), P("น้อย", cellc), P(stars(2)+" (Shopee)", cellc)],
]
t = Table(sc, colWidths=[40*mm, 30*mm, 26*mm, 28*mm, 38*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("BACKGROUND", (0,1), (-1,1), colors.HexColor("#fef9c3")),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 14))

# ================= RECOMMENDATION =================
story.append(Paragraph("คำแนะนำสำหรับคุณ (Bambu Lab A1 + ไลฟ์ TikTok)", h2))
rec = [
    [P("กลยุทธ์", cellw), P("รายละเอียด", cellw)],
    [P("1. ตัวเรียกคนดู (Traffic)", cellb), P("เปิดด้วยของเล่นขยับได้/ฟิดเจ็ต โชว์ปริ้นสด ดึงยอดวิว", cell)],
    [P("2. ตัวทำกำไร (Margin)", cellb), P("ขายของขวัญคัสตอมใส่ชื่อ คนยอมจ่ายแพง กำไรดี", cell)],
    [P("3. ไม่ผูกกับสินค้าเดียว", cellb), P("เครื่องเดียวปริ้นได้หลายอย่าง: ของเล่น + ชาร์มเคส + ของขวัญ", cell)],
    [P("4. วางตำแหน่งแบรนด์", cellb), P("มองตัวเองเป็น &ldquo;ครีเอเตอร์ที่ขายของ&rdquo; ไม่ใช่ &ldquo;ร้านที่ลงคลิป&rdquo;", cell)],
]
t = Table(rec, colWidths=[52*mm, 110*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GREEN),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f0fdf4")]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1, color=LINEG))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "บรรทัดสุดท้าย: อย่าผูกตัวเองกับสินค้าเดียว &mdash; มองเป็น &ldquo;ร้านของเล่น/ของขวัญ 3D ที่เล่าเรื่องผ่านการปริ้นสด&rdquo; "
    "จะกว้างและรอดกว่า &bull; ตัวเลขเป็นค่าประมาณการเพื่อวางแผน", note))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Thai", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(20*mm, 12*mm, "เปรียบเทียบธุรกิจ 3D Printing")
    canvas.drawRightString(190*mm, 12*mm, "หน้า %d" % doc.page)
    canvas.restoreState()


doc = SimpleDocTemplate(
    r"D:\Antigravity3\resume\3D_Printing_Business_Comparison.pdf",
    pagesize=A4,
    topMargin=18*mm, bottomMargin=18*mm, leftMargin=20*mm, rightMargin=20*mm,
    title="เปรียบเทียบธุรกิจ 3D Printing",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("PDF2 created OK")
