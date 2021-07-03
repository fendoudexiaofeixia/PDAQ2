"""
云平台查询链接：注意参数的使用
    Request URL: http://cloud.calmcar.com:5003/product/searchByPage?pagesize=10&&pagenum=1&&name=&&code=&&
    alias=&&company=&&ip=192.168.194.172&&plate_number=&&type=&&vboxversion=&&calmcarversion=&&filesysversion=&&hardwareversion=&&online
"""
import datetime
import json

import requests

# 测试 ip 为 172.16.5.28
'''
, customer_name, device_num, ip, mode_type
'''


class cloud_platform:
    def __init__(self, cus_name, ip, mode_type, serial_number, status):
        self.status = status
        self.type_mode = mode_type
        self.serial_number = serial_number
        self.cus_name = cus_name
        self.ip = ip
        self.website_url = 'http://cloud.calmcar.com:5002/'
        self.logon_website()
        self.get_comp_list()
        self.sear_prodct()

    def logon_website(self):
        """ 登录 """
        try:
            logon_cont = {
                "login_name": "testteam",
                "pass_word": "apt123",
                "app_name": "用户管理平台"
            }
            userAgent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"
            header = {'User-Agent': userAgent, }
            session = requests.Session()
            res_Rsp = session.post(self.website_url + 'admin/dologin', json=logon_cont, headers=header)
            page_mes = res_Rsp.json()
            header['token'] = page_mes['data']['token']
            self.session = session
            self.header = header
            # print(page_mes)
        except EOFError:
            print(EOFError)
            exit(0)

    ''' 获取去全部客户信息 '''

    def get_comp_list(self):
        company_list = self.session.get(self.website_url + '/company/', headers=self.header)
        res_mes = json.loads(company_list.text)['data']
        return res_mes

    ''' 
    注意修改IP
    检索设备是否存在 
    '''

    def sear_prodct(self):
        sear_res = self.session.get(
            'http://cloud.calmcar.com:5003/product/searchByPage?pagesize=10&&pagenum=1&&name=&&code=&&alias=&&company=&&ip={}&&plate_number=&&type=&&vboxversion=&&calmcarversion=&&filesysversion=&&hardwareversion=&&online'.format(
                self.ip),
            headers=self.header)
        res_mes = json.loads(sear_res.text)['data']
        return res_mes

    # 判断企业是否存在，若不存在则进行创建，否则 返回企业 ID
    def add_cus(self):
        cus_list = self.get_comp_list()
        for cus in cus_list:
            if self.cus_name == cus['name']:
                return cus['id']
        else:
            cus_address = 'China'
            added_company = {'name': self.cus_name, 'address': cus_address}
            self.session.post(self.website_url + '/company/', headers=self.header, json=added_company)
            cus_list_new = self.get_comp_list()
            for cus in cus_list_new:
                if self.cus_name == cus['name']:
                    return cus['id']

    '''
        {company: {id: 1}, createTime: "2021-07-02", code: "123123123", name: "COMPUTER", ip: "172.16.5.28",…}
        code: "123123123"  此处为序列号
        company: {id: 1}    需要获取公司列表 ID 
        createTime: "2021-07-02"  获取当前系统时间
        ip: "172.16.5.28"       通过外部函数获取
        name: "COMPUTER"
        status: "Test"
        type: "pdaq"
        若不存在 则进行创建
        '''

    def add_product(self):
        cus_id = self.add_cus()
        add_product_msg = {
            'code': self.serial_number,
            'company': {'id': cus_id},
            'createTime': str(datetime.date.today()),
            'ip': self.ip,
            'status': self.status,
            'type': self.type_mode
        }
        self.session.post(self.website_url + '/product/', headers=self.header, json=add_product_msg)
        return '添加成功'

    # 更新平台信息
    def delete_oldmsg(self):
        msg = self.sear_prodct()
        # print(msg[0]['id'])
        self.session.delete(self.website_url + 'product/' + str(msg[0]['id']), headers=self.header, verify=False)


def start_update(customer_name, ip, mode_type, serial_number, status):
    # 首先查询平台,如果存在就进行删除
    if cloud_platform(customer_name, ip, mode_type, serial_number, status).sear_prodct():
        cloud_platform(customer_name, ip, mode_type, serial_number, status).delete_oldmsg()
        print('删除成功')
        cus_id = cloud_platform(customer_name, ip, mode_type, serial_number, status).add_product()
        print('添加成功')
    else:
        # 首先进行客户信息查询
        cus_id = cloud_platform(customer_name, ip, mode_type, serial_number, status).add_product()
        print('添加成功')

# if __name__ == '__main__':
#     start_update('172.16.5.28')
#     cloud_platform().get_comp_list()
# a = cloud_platform('172.16.5.28').sear_prodct()
# print(a)
