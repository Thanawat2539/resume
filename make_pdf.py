# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---- Thai fonts ----
pdfmetrics.registerFont(TTFont("Thai", r"C:\Windows\Fonts\leelawad.ttf"))
pdfmetrics.registerFont(TTFont("ThaiB", r"C:\Windows\Fonts\leelawdb.ttf"))
pdfmetrics.registerFontFamily("Thai", normal="Thai", bold="ThaiB", italic="Thai", boldItalic="ThaiB")

# ---- Palette ----
INK      = colors.HexColor("#1f2937")
ACCENT   = colors.HexColor("#2563eb")
ACCENT2  = colors.HexColor("#0ea5e9")
GREEN    = colors.HexColor("#16a34a")
RED      = colors.HexColor("#dc2626")
LIGHT    = colors.HexColor("#eff6ff")
LIGHTG   = colors.HexColor("#f0fdf4")
GREY     = colors.HexColor("#6b7280")
LINEG    = colors.HexColor("#e5e7eb")

# ---- Styles ----
title = ParagraphStyle("title", fontName="ThaiB", fontSize=22, textColor=INK, leading=27)
subtitle = ParagraphStyle("subtitle", fontName="Thai", fontSize=11.5, textColor=GREY, leading=16)
h2 = ParagraphStyle("h2", fontName="ThaiB", fontSize=14.5, textColor=ACCENT, leading=19, spaceBefore=6, spaceAfter=4)
body = ParagraphStyle("body", fontName="Thai", fontSize=10.5, textColor=INK, leading=16)
bodys = ParagraphStyle("bodys", fontName="Thai", fontSize=9.5, textColor=INK, leading=14)
cell = ParagraphStyle("cell", fontName="Thai", fontSize=9.5, textColor=INK, leading=13)
cellb = ParagraphStyle("cellb", fontName="ThaiB", fontSize=9.5, textColor=INK, leading=13)
cellw = ParagraphStyle("cellw", fontName="ThaiB", fontSize=10, textColor=colors.white, leading=13)
cellr = ParagraphStyle("cellr", fontName="Thai", fontSize=9.5, textColor=INK, leading=13, alignment=2)
note = ParagraphStyle("note", fontName="Thai", fontSize=9, textColor=GREY, leading=13)

story = []

# ================= HEADER =================
story.append(Paragraph("โมเดลธุรกิจ &ldquo;Hybrid&rdquo; — เครื่องปริ้น 3D เคสมือถือ", title))
story.append(Spacer(1, 3))
story.append(Paragraph("ขายไลฟ์ TikTok &bull; ทุนตั้งต้น 20,000 บาท &bull; จัดทำ 30 พ.ค. 2569", subtitle))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=2, color=ACCENT))
story.append(Spacer(1, 12))

# ================= 1. HYBRID CONCEPT =================
story.append(Paragraph("1. แนวคิดโมเดล &ldquo;Hybrid&rdquo; (ได้ผลกว่าปริ้นเคสล้วน)", h2))
story.append(Paragraph(
    "แทนที่จะปริ้นทั้งเคส (ช้า 1.5&ndash;3 ชม./ชิ้น และผิวงานมีเส้นเลเยอร์ไม่เนียน) "
    "ให้ <b>ผสมเคสสำเร็จรูปกับชิ้นปริ้น 3D เฉพาะจุดที่เป็นจุดขาย</b> "
    "เพื่อให้ผลิตเร็วขึ้น ผิวสวยขึ้น ต้นทุนต่อชิ้นต่ำลง และมี &ldquo;สตอรี่&rdquo; ให้ไลฟ์สนุก", body))
story.append(Spacer(1, 8))

hybrid_data = [
    [Paragraph("ขั้น", cellw), Paragraph("ทำอะไร", cellw), Paragraph("รายละเอียด", cellw)],
    [Paragraph("1", cellb), Paragraph("ฐานเคส", cellb),
     Paragraph("ซื้อเคสใส/เคสเปล่าสำเร็จรูปจากโรงงาน (15&ndash;25 บาท/ชิ้น) ผิวเนียน", cell)],
    [Paragraph("2", cellb), Paragraph("ปริ้น 3D เฉพาะจุด", cellb),
     Paragraph("ชาร์ม/ตัวการ์ตูนติดเคส &bull; กริปแหวนจับ &bull; ขาตั้ง MagSafe &bull; ป้ายชื่อคัสตอม", cell)],
    [Paragraph("3", cellb), Paragraph("จุดขายไลฟ์", cellb),
     Paragraph("&ldquo;พิมพ์ชื่อคุณสดๆ&rdquo; &mdash; ลูกค้าคอมเมนต์ชื่อ โชว์การปริ้น แล้วส่งตามหลัง", cell)],
]
t = Table(hybrid_data, colWidths=[18*mm, 38*mm, 110*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(Spacer(1, 6))
story.append(Paragraph(
    "<b>ข้อดี:</b> ผลิตเร็วขึ้นหลายเท่า &bull; ผิวงานสวยระดับโรงงาน &bull; ต้นทุนต่ำลง &bull; "
    "คนชอบดู &ldquo;ของถูกสร้าง&rdquo; สดๆ อัลกอริทึม TikTok ดันคลิปแนวนี้ดี", note))
story.append(Spacer(1, 14))

# ================= 2. INVESTMENT =================
story.append(Paragraph("2. เงินลงทุนตั้งต้น (ทุน 20,000 บาท)", h2))
inv_data = [
    [Paragraph("รายการ", cellw), Paragraph("ราคา (บาท)", cellw), Paragraph("หมายเหตุ", cellw)],
    [Paragraph("เครื่องปริ้น 3D (Bambu Lab A1 / A1 Mini)", cell), Paragraph("8,500&ndash;13,000", cellr), Paragraph("แนะนำ A1 ปริ้นง่าย มือใหม่ใช้ได้", cell)],
    [Paragraph("ฟิลาเมนต์ TPU (เคส/ชิ้นนิ่ม) 2 กก.", cell), Paragraph("2,000", cellr), Paragraph("~1,000/กก.", cell)],
    [Paragraph("ฟิลาเมนต์ PLA หลายสี 2&ndash;3 กก.", cell), Paragraph("1,500", cellr), Paragraph("ชิ้นตกแต่ง/กริป", cell)],
    [Paragraph("ไฟวงแหวน + ขาตั้งมือถือไลฟ์", cell), Paragraph("1,500", cellr), Paragraph("สำหรับไลฟ์", cell)],
    [Paragraph("แพ็กเกจจิ้ง (ซอง/กล่อง/สติกเกอร์แบรนด์)", cell), Paragraph("1,000", cellr), Paragraph("สร้างแบรนด์", cell)],
    [Paragraph("งบบูสต์โฆษณา / ค่าส่งทดลอง", cell), Paragraph("2,000", cellr), Paragraph("ดันยอดช่วงแรก", cell)],
    [Paragraph("เงินสำรองฉุกเฉิน", cell), Paragraph("1,500&ndash;3,000", cellr), Paragraph("อะไหล่ หัวพ่นตัน งานเสีย", cell)],
    [Paragraph("รวมประมาณ", cellb), Paragraph("~17,500&ndash;20,000", ParagraphStyle("x", parent=cellr, fontName="ThaiB")), Paragraph("อยู่ในงบ", cellb)],
]
t = Table(inv_data, colWidths=[78*mm, 32*mm, 56*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-2), [colors.white, LIGHT]),
    ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#dbeafe")),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(Spacer(1, 14))

# ================= 3. PAYBACK =================
story.append(Paragraph("3. ต้นทุนต่อชิ้น &amp; การคืนทุน", h2))

# two columns: cost per unit + profit
cost_left = [
    [Paragraph("ต้นทุนผันแปร / เคส", cellw), Paragraph("บาท", cellw)],
    [Paragraph("เคสเปล่าสำเร็จรูป", cell), Paragraph("20", cellr)],
    [Paragraph("ฟิลาเมนต์ชิ้นปริ้น (~15 ก.)", cell), Paragraph("15", cellr)],
    [Paragraph("ค่าไฟ + สึกหรอ", cell), Paragraph("5", cellr)],
    [Paragraph("เผื่องานเสีย 15%", cell), Paragraph("5", cellr)],
    [Paragraph("แพ็กเกจจิ้ง", cell), Paragraph("10", cellr)],
    [Paragraph("รวมต้นทุน/ชิ้น", cellb), Paragraph("~55", ParagraphStyle("x", parent=cellr, fontName="ThaiB"))],
]
tL = Table(cost_left, colWidths=[52*mm, 22*mm])
tL.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT2),
    ("ROWBACKGROUNDS", (0,1), (-1,-2), [colors.white, LIGHT]),
    ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#e0f2fe")),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
]))

profit_right = [
    [Paragraph("ตั้งราคาขาย 199 บาท", cellw), Paragraph("บาท", cellw)],
    [Paragraph("ราคาขาย", cell), Paragraph("199", cellr)],
    [Paragraph("หักต้นทุน/ชิ้น", cell), Paragraph("-55", cellr)],
    [Paragraph("หักค่าส่ง + ค่าธรรมเนียม TikTok", cell), Paragraph("-25", cellr)],
    [Paragraph("กำไรสุทธิ / ชิ้น", cellb),
     Paragraph("~119", ParagraphStyle("g", parent=cellr, fontName="ThaiB", textColor=GREEN))],
]
tR = Table(profit_right, colWidths=[56*mm, 22*mm])
tR.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GREEN),
    ("ROWBACKGROUNDS", (0,1), (-1,-2), [colors.white, LIGHTG]),
    ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#dcfce7")),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
]))

wrap = Table([[tL, tR]], colWidths=[78*mm, 84*mm])
wrap.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"), ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(0,0),6)]))
story.append(wrap)
story.append(Spacer(1, 10))

# break-even
be_data = [
    [Paragraph("จุดคืนทุน (Break-even)", cellw), Paragraph("ยอดขาย", cellw), Paragraph("ระยะเวลา", cellw)],
    [Paragraph("คืนทุนเครื่อง + เซ็ตอัพ ~17,000 บาท", cell), Paragraph("~143 ชิ้น", cellb), Paragraph("&mdash;", cellr)],
    [Paragraph("ขายได้ 5 ชิ้น/วัน", cell), Paragraph("150 ชิ้น/เดือน", cell), Paragraph("~1 เดือน", cellb)],
    [Paragraph("ขายได้ 10 ชิ้น/วัน", cell), Paragraph("300 ชิ้น/เดือน", cell), Paragraph("~2 สัปดาห์", cellb)],
]
t = Table(be_data, colWidths=[80*mm, 40*mm, 42*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#7c3aed")),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f3ff")]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(Spacer(1, 14))

# ================= 4. RISKS =================
story.append(Paragraph("4. ปัญหาที่อาจเจอ &amp; วิธีรับมือ", h2))
risk_data = [
    [Paragraph("ปัญหาที่อาจเจอ", cellw), Paragraph("วิธีรับมือ", cellw)],
    [Paragraph("ปริ้นช้า ผลิตไม่ทันออเดอร์ช่วงไลฟ์พีค", cell),
     Paragraph("ปริ้นสต็อกรุ่นยอดนิยมล่วงหน้า &bull; รับคัสตอมแบบ &ldquo;พรีออเดอร์ส่งตามหลัง&rdquo;", cell)],
    [Paragraph("งานเสีย / หัวพ่นตัน / หลุดฐาน", cell),
     Paragraph("เผื่อต้นทุนงานเสีย 15% ไว้แล้ว &bull; สำรองอะไหล่หัวพ่น + แผ่นฐาน", cell)],
    [Paragraph("เคส PLA แข็งเปราะ แตกร้าวง่าย", cell),
     Paragraph("ใช้ TPU สำหรับชิ้นที่ต้องรับแรง &bull; เคสฐานใช้ของสำเร็จรูปอยู่แล้ว", cell)],
    [Paragraph("แข่งราคากับเคสสำเร็จรูป 50&ndash;100 บาท", cell),
     Paragraph("ขายงานคัสตอม/ดีไซน์เฉพาะ/ใส่ชื่อ ที่เคสตลาดทำไม่ได้", cell)],
    [Paragraph("ลิขสิทธิ์ลายการ์ตูน/แบรนด์", cell),
     Paragraph("เลี่ยงลายมีลิขสิทธิ์ &bull; ใช้ดีไซน์ของตัวเอง หรือไฟล์ลิขสิทธิ์เปิด (CC)", cell)],
    [Paragraph("ยอดวิวไลฟ์น้อยช่วงแรก", cell),
     Paragraph("โพสต์คลิปสั้นทุกวัน &bull; ไลฟ์เวลาคนเยอะ 20:00&ndash;23:00 &bull; ใช้งบบูสต์", cell)],
    [Paragraph("รุ่นมือถือเยอะ สต็อกเคสเปล่าบาน", cell),
     Paragraph("เริ่มจาก 3&ndash;5 รุ่นฮิต (iPhone 13/14/15 + Android ยอดนิยม) ก่อน", cell)],
]
t = Table(risk_data, colWidths=[72*mm, 90*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), RED),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#fef2f2")]),
    ("GRID", (0,0), (-1,-1), 0.5, LINEG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1, color=LINEG))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "หมายเหตุ: ตัวเลขเป็นค่าประมาณการเพื่อวางแผน อาจปรับตามราคาฟิลาเมนต์ ค่าส่ง และโปรโมชันจริงในตลาด", note))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Thai", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(20*mm, 12*mm, "โมเดลธุรกิจ 3D Phone Case &mdash; Hybrid".replace("&mdash;", "—"))
    canvas.drawRightString(190*mm, 12*mm, "หน้า %d" % doc.page)
    canvas.restoreState()


doc = SimpleDocTemplate(
    r"D:\Antigravity3\resume\Hybrid_3D_PhoneCase_BusinessModel.pdf",
    pagesize=A4,
    topMargin=18*mm, bottomMargin=18*mm, leftMargin=20*mm, rightMargin=20*mm,
    title="โมเดลธุรกิจ Hybrid - 3D Phone Case",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("PDF created OK")
