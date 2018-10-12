import openpyxl

wb=openpyxl.load_workbook('m1.xlsx')

ws=wb.worksheets[0]

data_range=ws.calculate_dimension().split(':')

left_top = openpyxl.utils.coordinate_to_tuple(data_range[0])
right_bottom = openpyxl.utils.coordinate_to_tuple(data_range[1])

col_width=[]

row_height=[]

for i in range(left_top[0], right_bottom[0]):
    col_letter=openpyxl.utils.get_column_letter(i)
    col_width.append(ws.column_dimensions[col_letter].width)

for i in range(left_top[1], right_bottom[1]):
    row_height.append(ws.row_dimensions[i].height)


print(row_height)
print(col_width)