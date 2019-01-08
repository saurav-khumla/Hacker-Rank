import xlrd
import xlwt

workbook = xlrd.open_workbook(r'H:\BMI\Hierachy 2 no numbers1.xlsx')  # We need to read the data
worksheet = workbook.sheet_by_name("INPUT")  #from the Excel sheet named "INPUT"

num_rows = worksheet.nrows  #Number of Rows

input_arr = []
childStr = '';

for curr_row in range(1, num_rows, 1):
    data = worksheet.cell_value(curr_row, 0)
    end = data.find(" -")
    # print(end)
    if(end > -1):
        data = data[0:end]

    dotIndex = data.find(".")
    if(dotIndex>-1):
        childStr = data[dotIndex+1:]
    elif(childStr!=''):
        data = childStr+"."+data+".PLANT";


    print(data)
    input_arr.append(data)

#print(input_arr)

workbook1 = xlwt.Workbook()
sheet = workbook1.add_sheet("TableOP")

for row in range(len(input_arr)):
    sheet.write(row, 0, input_arr[row])

workbook1.save(r"H:\BMI\outputNew.xls")