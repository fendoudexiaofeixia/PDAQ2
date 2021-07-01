# import urllib
# from urllib import request
# import urllib3
# from http import cookiejar
import requests
import json
import datetime


class cloud_platform():
    def __init__(self, customer_whole_name, devide_num, ip, mode_type, old_device_num=''):
        self.website_url = 'http://cloud.calmcar.com:5002/'
        self.logon_the_website()
        self.check_company_or_add(customer_whole_name)
        if old_device_num:
            self.delete_a_machine(old_device_num)
        self.add_a_machine(devide_num, customer_whole_name, ip, mode_type)
        self.session.close()

    def logon_the_website(self):
        try:
            logon_cont = {"login_name": "testteam", "pass_word": "apt123", "app_name": "用户管理平台"}
            userAgent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"
            header = {'User-Agent': userAgent, }
            session = requests.Session()
            responseRes = session.post(self.website_url + 'admin/dologin', json=logon_cont, headers=header)
            page_message = responseRes.json()
            header['token'] = page_message['data']['token']
            self.header = header
            self.session = session
            # print(1)
        except EOFError:
            print(EOFError)
            exit(0)

    def read_company_list(self):
        company_list = self.session.get(self.website_url + '/company/', headers=self.header)
        company_list = json.loads(company_list.text)['data']
        return company_list

    def check_company_or_add(self, customer_whole_name, customer_address=''):
        company_list = self.read_company_list()
        cs_name_list = [i['name'] for i in company_list]
        if customer_whole_name in cs_name_list:
            print('customer exist!')
            return
        else:
            print('customer not exist, now add it!')
            if not customer_address:
                customer_address = 'China'
            added_company = {'name': customer_whole_name, 'address': customer_address}
            self.session.post(self.website_url + '/company/', headers=self.header, json=added_company)

    def add_a_machine(self, device_number, customer_whole_name, machine_ip, type_mode):
        # test_data = self.session.get(self.website_url+'/product',headers=self.header)
        # test_data = json.loads(test_data.text)['data']
        type_choosen = {1: 'pdaq', 2: 'FCM', 4: 'FCM'}
        company_list = self.read_company_list()
        for c_info in company_list:
            if c_info['name'] == customer_whole_name:
                get_id = c_info['id']
                break
        currect_data = str(datetime.date.today())
        machine_message = {'code': device_number, 'name': 'PDAQ', 'company': {'id': get_id}, 'ip': machine_ip,
                           'status': 'Protuction', 'type': type_choosen[type_mode], 'createTime': currect_data}
        self.session.post(self.website_url + '/product/', headers=self.header, json=machine_message)
        print('machine added in cloud')

    def delete_a_machine(self, old_devive_num):
        machine_response = self.session.post(
            self.website_url + 'product/searchByPage?pagesize=10&&pagenum=1&&code=%s&&name=&&alias=&&status=&&company=&&type=&&plate_number=&&ip=&&calmcarversion=&&vboxversion=&&filesysversion=&&hardwareversion=' % old_devive_num,
            headers=self.header)
        machine_info = json.loads(machine_response.text)['data']
        for m in machine_info:
            print(m['id'], '...', m['ip'], m['code'], m['company']['name'], m['type'])
        print('pls ensure we need to delete this/those machine...')
        print('input the machine id (in website): ')
        machine_id = input()
        self.session.delete(self.website_url + 'product/' + machine_id, headers=self.header, verify=False)
        print('ori machine delete in cloud')


if __name__ == '__main__':
    cloud_platform('商汤', 'CC-calmcar-00522007001', '192.168.196.2', 0, 'CC-calmcar-00522007002')
