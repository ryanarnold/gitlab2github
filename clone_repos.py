import xlrd
import os

# Constants
subdir = {
    'LOCAL ONLY': 'local',
    'GITHUB PRIVATE': 'private',
    'GITHUB PUBLIC': 'public',
}

if __name__ == '__main__':
    excel_file_path = 'projects.xlsx'

    workbook = xlrd.open_workbook(excel_file_path)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        name = sheet.cell_value(row, 0)
        todo = sheet.cell_value(row, 1)
        git_url = sheet.cell_value(row, 5)

        
        clone_command = f'git clone {git_url} {subdir[todo]}/{name}'
        os.system(clone_command)
