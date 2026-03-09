#views.py
import openpyxl
from django.shortcuts import render
from django.http import HttpResponse

def work_instruction_home(request):
    return HttpResponse("Work Instruction Home Page")

def excel_data_view(request):
    # Path to your Excel file (store in media/static or database)
    filepath = 'Documents/pythonProjects/django_project/excel/DG2_3_1.xls'

    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook['Sheet1']  # or workbook.active

    # Extract specific section (e.g., rows 2-10, columns A-C)
    data = []
    for row in sheet.iter_rows(min_row=6, max_row=15, min_col=4, max_col=6, values_only=True):
        data.append(row)
    
    context = {'excel_data': data}
    return render(request, 'excel_display.html', context)
    #return render(request, '')
