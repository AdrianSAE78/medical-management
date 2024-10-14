from fpdf import FPDF, FontFace, XPos, YPos

def marcar():
    text = '(MARCAR)'
    pdf.set_font('DejaVu', size=5)
    return text

pdf = FPDF()

pdf.add_page(orientation='P', format='a3')
pdf.set_margins(left=30, right=30, top=8)


#----------237 complete cell------------
pdf.add_font('DejaVu', '', 'dejavu_font/ttf/DejaVuSans.ttf')
pdf.add_font('DejaVu', 'B', 'dejavu_font/ttf/DejaVuSans-Bold.ttf')
pdf.set_draw_color(95, 95, 95)
pdf.set_font('DejaVu', size=10, style='B')
pdf.set_fill_color(204, 204, 255)

#-----------Section A-------------
#def SectionA():
pdf.cell(0, 5, "A. DATOS DEL ESTABLECIMIENTO Y USUARIO/PACIENTE", 1, fill=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)
pdf.set_font('DejaVu', size=6, style='B')
pdf.set_fill_color(204, 255, 204)
pdf.cell(55, 5, 'INSTITUCIÓN DEL SISTEMA', 1, fill=True, align='C')
pdf.cell(17, 5, 'UNICÓDIGO', 1, fill=True, align='C')
pdf.cell(70, 5, 'ESTABLECIMIENTO DE SALUD', 1, fill=True, align='C')
pdf.cell(55, 5, 'NÚMERO DE HISTORIA CLÍNICA ÚNICA', 1, fill=True, align='C')
pdf.cell(40, 5, 'NÚMERO DE ARCHIVO', 1, fill=True, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.cell(55, 6, '', 1, align='C')
pdf.cell(17, 6, '', 1, align='C')
x = pdf.get_x()
y = pdf.get_y()
pdf.multi_cell(70, 3, 'HOSPITAL GINECO OBSTETRICO PEDIATRICO DE NUEVA AURORA "LUZ ELENA ARISMENDI"', 1, 'C')
pdf.set_xy(x + 70, y)
pdf.cell(55, 6, '', 1, align='C')
pdf.cell(40, 6, '', 1, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.cell(42, 8, 'PRIMER APELLIDO', 1, fill=True, align='C')
pdf.cell(42, 8, 'SEGUNDO APELLIDO', 1, fill=True, align='C')
pdf.cell(42, 8, 'PRIMER NOMBRE', 1, fill=True, align='C')
pdf.cell(42, 8, 'SEGUNDO NOMBRE', 1, fill=True, align='C')
pdf.cell(9, 8, 'SEXO', 1, fill=True, align='C')
x = pdf.get_x()
y = pdf.get_y()
pdf.multi_cell(20, 4, 'FECHA\nNACIMIENTO', 1, fill=True, align='C')
pdf.set_xy(x + 20, y)
pdf.cell(10, 8, 'EDAD', 1, fill=True, align='C')
pdf.set_font('DejaVu', size=5)
pdf.cell(30, 4, '**CONDICIÓN EDAD** (MARCAR)', 1, fill=True, align='C', markdown=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)
x = pdf.get_x()
y = pdf.get_y()
pdf.set_xy(x + 207, y)
pdf.set_font('DejaVu', size=6, style='B')
pdf.cell(5, 4, 'H', 1, fill=True, align='C')
pdf.cell(5, 4, 'D', 1, fill=True, align='C')
pdf.cell(9, 4, 'M', 1, fill=True, align='C')
pdf.cell(11, 4, 'A', 1, fill=True, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.cell(42, 5, '', 1, align='C')
pdf.cell(42, 5, '', 1, align='C')
pdf.cell(42, 5, '', 1, align='C')
pdf.cell(42, 5, '', 1, align='C')
pdf.cell(9, 5, '', 1, align='C')
pdf.cell(20, 5, '', 1, align='C')
pdf.cell(10, 5, '', 1, align='C')
pdf.cell(5, 5, '', 1, align='C')
pdf.cell(5, 5, '', 1, align='C')
pdf.cell(9, 5, '', 1, align='C')
pdf.cell(11, 5, '', 1, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

#-----------Line Break-------------

pdf.cell(0, 3, '', 1, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.set_font('DejaVu', size=10, style='B')
pdf.set_fill_color(204, 204, 255)

#-----------Section B--------------
#def SectionB():
pdf.cell(0, 5, "B. SERVICIO Y PRIORIDAD DE ATENCIÓN", 1, fill=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)
pdf.set_font('DejaVu', size=5, style='B')
pdf.set_fill_color(204, 255, 204)


pdf.cell(92, 4, 'DIAGNÓSTICO', 1, fill=True, align='C')
pdf.cell(15, 4, 'CIE', 1, fill=True, align='C')
pdf.cell(15, 12, 'SERVICIO', 1, fill=True, align='C')
pdf.set_font('DejaVu', size=5)
pdf.cell(25, 4, 'EMERGENCIA', 1, fill=True, align='C')
pdf.cell(8, 4, '', 1, align='C')
pdf.set_font('DejaVu', size=5, style='B')
pdf.cell(25, 4, 'ESPECIALIDAD', 1, fill=True, align='C')
pdf.cell(32, 4, '', 1, align='C')
pdf.cell(25, 4, 'PRIORIDAD', 1, fill=True, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)


pdf.set_font('DejaVu', size=6, style='B')
pdf.cell(3, 4, '1.', 1, fill=True, align='C')
pdf.set_font('DejaVu', size=5, style='B')
pdf.cell(89, 4, '', 1, align='C')
pdf.cell(15, 4, '', 1, align='C')
x = pdf.get_x()
pdf.set_x(x+15)
pdf.set_font('DejaVu', size=5)
pdf.cell(25, 4, 'CONSULTA EXTERNA', 1, fill=True, align='C')
pdf.cell(8, 4, '', 1, align='C')
pdf.set_font('DejaVu', size=5, style='B')
pdf.cell(25, 4, 'SALA', 1, fill=True, align='C')
pdf.cell(32, 4, '', 1, align='C')
pdf.set_font('DejaVu', size=5)
pdf.cell(12.5, 4, 'URGENTE', 1, fill=True, align='C')
pdf.cell(12.5, 4, '', 1, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.set_font('DejaVu', size=6, style='B')
pdf.cell(3, 4, '2.', 1, fill=True, align='C')
pdf.set_font('DejaVu', size=5, style='B')
pdf.cell(89, 4, '', 1, align='C')
pdf.cell(15, 4, '', 1, align='C')
x = pdf.get_x()
pdf.set_x(x+15)
pdf.set_font('DejaVu', size=5)
pdf.cell(25, 4, 'HOSPITALIZACIÓN', 1, fill=True, align='C')
pdf.cell(8, 4, '', 1, align='C')
pdf.set_font('DejaVu', size=5, style='B')
pdf.cell(25, 4, 'CAMA', 1, fill=True, align='C')
pdf.cell(32, 4, '', 1, align='C')
pdf.set_font('DejaVu', size=5)
pdf.cell(12.5, 4, 'RUTINA', 1, fill=True, align='C')
pdf.cell(12.5, 4, '', 1, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.multi_cell(0, 4, f'**TRATAMIENTO TERAPEUTICO (ESPECIFIQUE NOMBRE Y TIEMPO DE ADMINISTRACIÓN):**', 1, align='L', markdown=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.multi_cell(0, 4, f'', 1, align='L', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

#-----------Line Break-------------

pdf.cell(0, 3, '', 1, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.set_font('DejaVu', size=10, style='B')
pdf.set_fill_color(204, 204, 255)

#-----------Section C--------------
pdf.cell(0, 5, "C. LISTADO DE EXÁMENES", 1, fill=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.set_font('DejaVu', size=5)

x = pdf.get_x()
y = pdf.get_y()

#-----------Left--------------
with pdf.table(width=84, col_widths=(27, 10, 27, 10), text_align='LEFT', align="LEFT", line_height=(3.2), first_row_as_headings=False, outer_border_width=0.3) as table:

    style_defined = FontFace(fill_color=(204,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_undefined = FontFace(fill_color=(255,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_header = FontFace(fill_color=(204,204,255), size_pt=7, family='DejaVu', emphasis='B')

    row = table.row()
    row.cell("HEMATOLOGÍA", style=style_header, colspan=4, align="C")

    row = table.row()
    row.cell("BIOMETRÍA HEMÁTICA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("FRAGILIDAD OSMÓTICA ERITROCITARIA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("HEMATOCRITO (HCTO)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("METABISULFITO", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("HEMOGLOBINA (HB)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HEMATOZOOARIO", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("PLAQUETAS", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("INVESTIGACIÓN DE LEISHMANIA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("RETICULOCITOS", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("EOSINÓFILO EN MOCO NASAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("VELOCIDAD DE ERITROSEDIMENTACIÓN", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("FROTIS SANGRE PERIFERICA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("HIERRO SERICO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("ÁCIDO FÓLICO", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FIJACIÓN HIERRO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("VITAMINA B12", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("PORCENTAJE SATURACIÓN TRANSFERRINA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("TRANSFERRINA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FERRITINA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

pdf.set_xy(x + 87, y)

x = pdf.get_x()
y = pdf.get_y()

#-----------Middle--------------
with pdf.table(width=60, col_widths=(17, 3), text_align='LEFT', align="LEFT", line_height=(4), first_row_as_headings=False, outer_border_width=0.3) as table:

    style_defined = FontFace(fill_color=(204,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_undefined = FontFace(fill_color=(255,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_header = FontFace(fill_color=(204,204,255), size_pt=7, family='DejaVu', emphasis='B')

    row = table.row()
    row.cell("COAGULACIÓN Y HEMOSTASIA", style=style_header, colspan=2, align="C")

    row = table.row()
    row.cell("TIEMPO DE PROTROMBINA (TP)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("TIEMPO DE TROMBOPLASTINA PARCIAL (TTP)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("TIEMPO DE TROMBINA (TT)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("INR", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FACTOR COAGULACIÓN VIII", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FACTOR COAGULACIÓN IX", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FACTOR VON WILLEBRAND", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FIBRINOGENO", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("DIMERO-D", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("IDENTIFICACION DE INHIBIDORES", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

pdf.set_xy(x + 63, y)

#-----------Right--------------
with pdf.table(width=87, col_widths=(35.5, 8, 35.5, 8), text_align='LEFT', align="LEFT", line_height=(2.9), first_row_as_headings=False, outer_border_width=0.3) as table:
    style_defined = FontFace(fill_color=(204,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_undefined = FontFace(fill_color=(255,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_header = FontFace(fill_color=(204,204,255), size_pt=7, family='DejaVu', emphasis='B')

    row = table.row()
    row.cell("QUÍMICA SANGUÍNEA", style=style_header, colspan=4, align="C")

    row = table.row()
    row.cell("GLUCOSA BASAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("BILIRRUBINA DIRECTA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("GLUCOSA POST PRANDIAL 2 HORAS", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("BILIRRUBINA INDIRECTA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("GLUCOSA AL AZAR", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("COLESTEROL TOTAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("SOBRECARGA GLUCOSA 75 gramos", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("LIPOPROTEÍNA DE ALTA DENSIDAD (HDL)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("TEST DE SULLIVAN (GLUCOSA 50 gramos)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("LIPOPROTEÍNA DE BAJA DENSIDAD (LDL)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("UREA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("LIPOPROTEÍNA DE MUY BAJA DENSIDAD (VLDL)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CREATININA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("TRIGLICERIDOS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ACIDO ÚRICO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("ALBUMINA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FOSFATASA ALCALINA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("PROTEÍNAS TOTALES", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("DESHIDROGENASA LACTICA (LDH)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HEMOGLOBINA GLICOSILADA (HBA1C)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ASPARTATO AMINOTRANSFERASA (AST/TGO)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CPK TOTAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ALANINA AMINOTRANSFERASA (ALT/TGP)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("FRUCTOSAMINA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("GAMMA-GLUTARIL TRANSFERASA (GGT)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("PCR CUANTITATIVO", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("AMILASA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("LIPASA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("BILIRRUBINA TOTAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)


pdf.set_xy(x - 87, y + 52)
x = pdf.get_x()
y = pdf.get_y()

#-----------Left--------------
with pdf.table(width=84, col_widths=(27, 10, 27, 10), text_align='LEFT', align="LEFT", line_height=(3.25), first_row_as_headings=False, outer_border_width=0.3) as table:
    style_defined = FontFace(fill_color=(204,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_undefined = FontFace(fill_color=(255,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_header = FontFace(fill_color=(204,204,255), size_pt=7, family='DejaVu', emphasis='B')

    row = table.row()
    row.cell("INMUNOLOGÍA / INFECCIOSAS", style=style_header, colspan=4, align="C")

    row = table.row()
    row.cell("COMPLEMENTO C3", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("ANTIGENO SUPERFICIE HEPATITIS B (HBSAG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("COMPLEMENTO C4", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("ANTICUERPOS ANTICORE Ig-G (HBcAG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("IgA TOTAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("ANTICUERPOS ANTICORE Ig-M (HBcAG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("IgE TOTAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HEPATITIS C: HVC", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("IgG TOTAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("VIH (1+2) CUALITATIVA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("IgM TOTAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("VIH (1+2) CUANTITATIVA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("PROCALCITONINA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HERPES 1 (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("IL-6", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HERPES 1 (IgM)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HERPES 2 (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANCA-C", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HERPES 2 (IgM)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANCA-P", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("RUBEOLA (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTI-DNA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("RUBEOLA (IgM)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTI-CCP", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("TOXOPLASMA (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTI-SM", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("TOXOPLASMA (IgM)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTI-RO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CITOMEGALOVIRUS (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTI-LA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CITOMEGALOVIRUS (IgM)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTI CARDIOLIPINA IgG", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("EPSTEIN BAR (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTI CARDIOLIPINA IgM", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("EPSTEIN BAR (IgM)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTIFOSFOLIPIDOS IgG", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("DENGUE (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTIFOSFOLIPIDOS IgM", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("DENGUE (IgM)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FACTOR REUMATOIDEO (IgM)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CLAMIDIA (IgA)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("SFLT1 (MARCADOR DE PREECLAMPSIA)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CLAMIDIA (IgG)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("PIGF (MARCADOR DE PREECLAMPSIA)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("FTA-ABS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ANTICUERPOS ANTICORE Ig-G(HBcAG)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("HEPATITIS A (IgM)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("HEPATITIS A TOTAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)


pdf.set_xy(x + 87, y + 4)

x = pdf.get_x()
y = pdf.get_y()
#-----------Middle--------------
with pdf.table(width=60, col_widths=(17, 3), text_align='LEFT', align="LEFT", line_height=(4), first_row_as_headings=False, outer_border_width=0.3) as table:

    style_defined = FontFace(fill_color=(204,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_undefined = FontFace(fill_color=(255,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_header = FontFace(fill_color=(204,204,255), size_pt=7, family='DejaVu', emphasis='B')

    row = table.row()
    row.cell("ORINA", style=style_header, colspan=2, align="C")

    row = table.row()
    row.cell("ELEMENTAL Y MICROSCOPICO (EMO)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("GRAM GOTA FRESCA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("OSMOLARIDAD URINARIA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("SODIO EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("POTASIO EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CLORO EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CALCIO URINARIO", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FOSFORO EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("MAGNESIO EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("GLUCOSA EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("UREA EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CREATINA EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("NITRÓGENO UREICO EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ÁCIDO ÚRICO EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("PROTEINAS EN ORINA PARCIAL", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("FÓSFORO EN ORINA 24 HORAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("POTASIO EN ORINA 24 HORAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("PROTEINAS EN ORINA 24 HORAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("DEPURACIÓN CREATININA (ORINA 24 HORAS)", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ÁCIDO ÚRICO EN ORINA 24 HORAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CALCIO EN ORINA 24 HORAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("AMILASA EN ORINA 24 HORAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("COBRE EN ORINA 24 HORAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("AZÚCARES REDUCTORES", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("DROGAS DE ABUSO EN ORINA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ALBUMINURIA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

pdf.set_xy(x + 63, y + 15)
x = pdf.get_x()

#-----------Left--------------
with pdf.table(width=84, col_widths=(27, 10, 27, 10), text_align='LEFT', align="LEFT", line_height=(3.1), first_row_as_headings=False, outer_border_width=0.3) as table:
    
    style_defined = FontFace(fill_color=(204,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_undefined = FontFace(fill_color=(255,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_header = FontFace(fill_color=(204,204,255), size_pt=7, family='DejaVu', emphasis='B')

    row = table.row()
    row.cell("HECES", style=style_header, colspan=4, align="C")

    row = table.row()
    row.cell("COPROLÓGICO / COPROPARASITARIO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CRIPTOSPORIDIUM", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("COPROPARASITARIO POR CONCENTRACIÓN", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("OXIUROS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("COPRO SERIADO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("GARDIA-LAMBLIA ANTÍGENO", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("INVESTIGACION DE POLIMORFONUCLEARES (PMN)", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("INVESTIGACIÓN DE GRASAS", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("SANGRE OCULTA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("AZÚCARES REDUCTORES", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("INVESTIGACIÓN DE pH", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HELICOBACTER PYLORI", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ROTAVIRUS", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("ADENOVIRIS", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

y = pdf.get_y()

pdf.set_xy(x, y + 4)

#-----------Left--------------
with pdf.table(width=84, col_widths=(21, 7, 21, 7, 21, 7), text_align='LEFT', align="LEFT", line_height=(3.1), first_row_as_headings=False, outer_border_width=0.3) as table:
    
    style_defined = FontFace(fill_color=(204,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_undefined = FontFace(fill_color=(255,255,255), size_pt=5, family='DejaVu', emphasis=None)
    style_header = FontFace(fill_color=(204,204,255), size_pt=7, family='DejaVu', emphasis='B')

    row = table.row()
    row.cell("MARCADORES TUMORALES", style=style_header, colspan=6, align="C")

    row = table.row()
    row.cell("CEA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("PSA LIBRE", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("HE4", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("AFP", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("PSA TOTAL", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("B-HCG LIBRE", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CA 125", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("β2 -MICROGLOBULINA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("B-HCG CUANTITATIVA", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CA 15.3", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("ANTI-TPO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CA 19.9", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("ANTI-TG", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("CA 72.4", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("TIROGLOBULINA", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("", style=style_defined)
    row.cell("", style=style_undefined)

    row = table.row()
    row.cell("COPROLÓGICO", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CRIPTOSPORIDIUM", style=style_defined)
    row.cell("", style=style_undefined)
    row.cell("CRIPTOSPORIDIUM", style=style_defined)
    row.cell("", style=style_undefined)

pdf.add_page(orientation='P')
pdf.output('Doc.pdf')
