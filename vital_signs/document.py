from fpdf import FPDF, XPos, YPos

def marcar():
    text = '(MARCAR)'
    pdf.set_font('helvetica', size=5)
    return text

pdf = FPDF()

pdf.add_page(orientation='P', format='a3')
pdf.set_margins(left=30, right=30, top=8)

#----------237 complete cell------------


pdf.set_font('helvetica', size=10, style='B')
pdf.set_fill_color(204, 204, 255)

#-----------Section A-------------
pdf.cell(0, 5, "A. DATOS DEL ESTABLECIMIENTO Y USUARIO/PACIENTE", 1, fill=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)
pdf.set_font('helvetica', size=6, style='B')
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
pdf.set_font('helvetica', size=5)
pdf.cell(30, 4, '**CONDICIÓN EDAD** (MARCAR)', 1, fill=True, align='C', markdown=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)
x = pdf.get_x()
y = pdf.get_y()
pdf.set_xy(x + 207, y)
pdf.set_font('helvetica', size=6, style='B')
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

pdf.set_font('helvetica', size=10, style='B')
pdf.set_fill_color(204, 204, 255)

#-----------Section B--------------

pdf.cell(0, 5, "B. SERVICIO Y PRIORIDAD DE ATENCIÓN", 1, fill=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)
pdf.set_font('helvetica', size=5, style='B')
pdf.set_fill_color(204, 255, 204)


pdf.cell(92, 4, 'DIAGNÓSTICO', 1, fill=True, align='C')
pdf.cell(15, 4, 'CIE', 1, fill=True, align='C')
pdf.cell(15, 12, 'SERVICIO', 1, fill=True, align='C')
pdf.set_font('helvetica', size=5)
pdf.cell(25, 4, 'EMERGENCIA', 1, fill=True, align='C')
pdf.cell(8, 4, '', 1, align='C')
pdf.set_font('helvetica', size=5, style='B')
pdf.cell(25, 4, 'ESPECIALIDAD', 1, fill=True, align='C')
pdf.cell(32, 4, '', 1, align='C')
pdf.cell(25, 4, 'PRIORIDAD', 1, fill=True, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)


pdf.set_font('helvetica', size=6, style='B')
pdf.cell(3, 4, '1.', 1, fill=True, align='C')
pdf.set_font('helvetica', size=5, style='B')
pdf.cell(89, 4, '', 1, align='C')
pdf.cell(15, 4, '', 1, align='C')
x = pdf.get_x()
pdf.set_x(x+15)
pdf.set_font('helvetica', size=5)
pdf.cell(25, 4, 'CONSULTA EXTERNA', 1, fill=True, align='C')
pdf.cell(8, 4, '', 1, align='C')
pdf.set_font('helvetica', size=5, style='B')
pdf.cell(25, 4, 'SALA', 1, fill=True, align='C')
pdf.cell(32, 4, '', 1, align='C')
pdf.set_font('helvetica', size=5)
pdf.cell(12.5, 4, 'URGENTE', 1, fill=True, align='C')
pdf.cell(12.5, 4, '', 1, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.set_font('helvetica', size=6, style='B')
pdf.cell(3, 4, '2.', 1, fill=True, align='C')
pdf.set_font('helvetica', size=5, style='B')
pdf.cell(89, 4, '', 1, align='C')
pdf.cell(15, 4, '', 1, align='C')
x = pdf.get_x()
pdf.set_x(x+15)
pdf.set_font('helvetica', size=5)
pdf.cell(25, 4, 'HOSPITALIZACIÓN', 1, fill=True, align='C')
pdf.cell(8, 4, '', 1, align='C')
pdf.set_font('helvetica', size=5, style='B')
pdf.cell(25, 4, 'CAMA', 1, fill=True, align='C')
pdf.cell(32, 4, '', 1, align='C')
pdf.set_font('helvetica', size=5)
pdf.cell(12.5, 4, 'RUTINA', 1, fill=True, align='C')
pdf.cell(12.5, 4, '', 1, align='C', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.multi_cell(0, 4, f'**TRATAMIENTO TERAPEUTICO (ESPECIFIQUE NOMBRE Y TIEMPO DE ADMINISTRACIÓN):**', 1, align='L', markdown=True, new_x=XPos.LMARGIN ,new_y=YPos.NEXT)

pdf.multi_cell(0, 4, f'', 1, align='L', new_x=XPos.LMARGIN ,new_y=YPos.NEXT)






pdf.add_page(orientation='P')
pdf.output('Doc.pdf')


