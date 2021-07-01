import os
import subprocess
import json
from automatic_configuration_tool.python import mode_config_process
import pandas as pd
from automatic_configuration_tool.python import system_config_process
# import remote_connect
from automatic_configuration_tool.python import user_interaction
from automatic_configuration_tool.python import record_and_log


def get_info_list():
    with open(r'/home/calmcar/PycharmProject/PDAQ2/automatic_configuration_tool/python/global_variable.json',
              'r') as jsonfile:
        jsoncontent = json.load(jsonfile)
    jsonfile.close()
    customer_list_path = jsoncontent['CaA_list_path']
    customer_list = []
    cacontent = pd.DataFrame(pd.read_excel(customer_list_path, sheet_name='customer_list'))
    for index in cacontent.index:
        line_content = list(cacontent.loc[index].values)
        customer_list.append(line_content)
    jsoncontent['customer_list'] = customer_list
    return jsoncontent


class process_choosen(user_interaction.interacte_model):
    def ip_input(self, ip):
        format_ = True
        print('pls fill in pdaq ip: ')
        ip = ip
        check_ip = ip.split('.')
        if len(check_ip) != 4:
            format_ = False
        for _ in check_ip:
            try:
                _ = int(_)
            except:
                format_ = False
                continue
            if 0 <= format_ < 255:
                pass
            else:
                format_ = False
        if not format_:
            print('ip format error!')
            exit(0)
        return ip

    def config_choosen(self, camera_model):
        # print('choosen the config mathod:')
        # for index,listcontent in config_list:
        #     print(index,listcontent)
        # a = input()
        a = self.what_need_config('config_mathod', camera_model)
        return a

    def device_choosen(self, serial_number):
        print('please input machine deviced num: ')
        _dev_ = serial_number
        _dev_check = True
        try:
            _dev_cresult = _dev_.split('-')
            if len(_dev_cresult) < 4:
                _dev_check = False
            if _dev_cresult[0] != 'CC':
                _dev_check = False
            # if int(_dev_cresult[2][:2]) > 3 or len(_dev_cresult[2]) != 11:
            #     _dev_check = False
            int(_dev_cresult[2])
        except:
            _dev_check = False
        if not _dev_check:
            print('device num input error')
            exit(0)
        return _dev_

    def customer_name_choosen(self):
        a = self.what_need_config('customer_list')
        return a

    def upload_or_modify(self, camera_model):
        a = self.what_need_config('system_method', camera_model)
        return a


def start_main(ip, camera_model, serial_number, customer_name):
    need_info = get_info_list()
    the_process = process_choosen(need_info)
    _c_ip = the_process.ip_input(ip)
    # _c1_ = the_process.config_choosen()
    _c1_ = 0
    if _c1_ == 0:
        mode_config_process.mode_process_and_exit(_c_ip, need_info, camera_model)
        print('\nif need configration the cloud:')
        print('0: no\n1: yes')
        """ 修改为直接配置云平台 """
        _c1_0 = 1
        if int(_c1_0) == 1:
            _c1_ = 1
        # if _c1_ == 1:
        device_num = the_process.device_choosen(serial_number)
        #     print('now we get the customer list:')
        #     for itemname in need_info['customer_list']:
        #         print(itemname)
        #     print('if need add new customer? \n0:no\n1:yes')
        #     i = input()
        #     if int(i) == 1:
        #         print('pls input customer full name and shorthand(separation with a space): ')
        #         new_customer = input()
        #         customer_name = new_customer.split()[0]
        #         whole_customer_name = [_[0] for _ in need_info['customer_list']]
        #         if customer_name in whole_customer_name:
        #             print('customer name already exist ')
        #         else:
        #             record_and_log.update_customer_list(new_customer, need_info['CaA_list_path'])
        #     else:
        #         customer_name_indx = the_process.customer_name_choosen()
        #         customer_name = need_info['customer_list'][customer_name_indx][0]
        need_add_or_modify = the_process.upload_or_modify(camera_model)
        need_add_or_modify = need_info['system_method'][need_add_or_modify]
        cloud_related = system_config_process.clode_process(customer_name, _c_ip, device_num)
        old_dev_num = cloud_related.update_pdaq_json()
        if 'add' in need_add_or_modify:
            old_dev_num = ''
        else:
            pass
        cloud_related.update_cloud_and_saveinfo(old_device_num=old_dev_num)
        record_and_log.add_or_update_machine_list([customer_name, device_num, _c_ip], need_info['CaA_list_path'],
                                                  original_devnum=old_dev_num)


# if __name__ == '__main__':
#     start_main('192.168.194.174', 1, ' ', '华人运通')
