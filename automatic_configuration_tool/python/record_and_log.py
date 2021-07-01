from xlutils.copy import copy
import xlrd

def update_customer_list(new_costomer_info,file_located):
    new_costomer_info = new_costomer_info.split()
    excal_file = xlrd.open_workbook(file_located)
    sheet_name = excal_file.sheet_names()
    rows = excal_file.sheet_by_name('customer_list').nrows
    new_sheet = copy(excal_file)
    open_the_sheet = new_sheet.get_sheet(sheet_name.index('customer_list'))
    open_the_sheet.write(rows,0,new_costomer_info[0])
    open_the_sheet.write(rows,1,new_costomer_info[1])
    new_sheet.save(file_located)

def add_or_update_machine_list(new_machine_info,file_located,original_devnum=''):
    #[customer name, device num, machine ip , add or modify]
    workbook = xlrd.open_workbook(file_located)
    sheet_name = workbook.sheet_names()
    sheet_index = sheet_name.index('machine_list')
    sheet_val = workbook.sheet_by_index(sheet_index)
    if not original_devnum:
        rows = sheet_val.nrows
        modify_flag = 'A'
    else:
        device_num_list = [sheet_val.cell_value(i, 1) for i in range(sheet_val.nrows)]
        try:
            rows = device_num_list.index(original_devnum)
        except:
            print('no such device num record in the list, add in a new row')
            rows = sheet_val.nrows
        modify_flag = 'M'
    new_workbook = copy(workbook)
    new_sheet = new_workbook.get_sheet(sheet_index)
    new_machine_info = new_machine_info+[modify_flag]
    for idex in range(4):
        new_sheet.write(rows,idex,new_machine_info[idex])
    new_workbook.save(file_located)


if __name__ == '__main__':
    # update_customer_list('test test','../demand/customer_and_machine_list.xlsx')
    add_or_update_machine_list(['add']*4,'../demand/customer_and_machine_list.xlsx','test')