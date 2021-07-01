import json
import pandas as pd
from collections import OrderedDict
from automatic_configuration_tool.python import user_interaction
from automatic_configuration_tool.python import remote_connect
import codecs
import subprocess

index_command = ['/proc/device-tree/i2c@3180000/tca9548@70/i2c@0/ov10635_a@30',
                 '/proc/device-tree/i2c@3180000/tca9548@70/i2c@0/camera_a@30',
                 '/proc/device-tree/i2c@3180000/cax02_a@6a']
index_name = ['series3', 'series5', 'series6']


def read_json_file():
    with open('global_variable.json', 'r') as jsonfile:
        jsoncontent = json.load(jsonfile)
    jsonfile.close()
    return jsoncontent


class gather_configuration():
    def __init__(self, config_json, choosen_mode, series_name):
        self.config_json = config_json
        self.series_name = series_name
        eval('self.' + choosen_mode + '()')
        print('gather config updated')

    def set1_ZF(self):
        self.config_json['general']['run_mode'] = 0
        self.config_json['general']['enable_gps'] = 1
        self.config_json['general']['can_number'] = 2
        self.config_json['recorder']['bitrate'] = 50000000
        self.config_json['recorder']['fps'] = 30
        self.config_json['recorder']['clip_length'] = 5
        self.config_json['tcp_server']['enable_break'] = 1
        self.config_json['tcp_server']['server_image'] = 1
        self.config_json['gps']['uri'] = '/dev/ttyTHS2'
        print('g1')

    def set2_SQ2in1ands6(self):
        self.config_json['general']['run_mode'] = 0
        self.config_json['recorder']['clip_length'] = 5
        self.config_json['rtmp']['enable_alirtmp'] = 1
        self.config_json['rtmp']['enable_localrtmp'] = 1
        self.config_json['rtmp']['rtmp_bitrate'] = 1000000
        self.config_json['rtmp']['rtmp_fps'] = 25
        self.config_json['rtmp']['enable_rtmp_audio'] = 1
        self.config_json['audioinput']['enable_audio'] = 1
        self.config_json['tcp_server']['enable_upload_ftp'] = 1
        self.config_json['tcp_server']['http_url'] = 'https://icvredata-pv.saicmotor.com:8083/'
        self.config_json['general']['enable_gps'] = 1
        self.config_json['gps']['uri'] = '/dev/ttyTHS2'
        if '5' in self.series_name:
            self.config_json['general']['camera_number'] = 6
            self.config_json['general']['vertical_camera_num'] = 2
            for cam_indx in range(6):
                self.config_json['camera' + str(cam_indx)]['width'] = 1280
                self.config_json['camera' + str(cam_indx)]['height'] = 720
        elif '6' in self.series_name:
            self.config_json['general']['camera_number'] = 3
            self.config_json['general']['vertical_camera_num'] = 3
            for cam_indx in range(3):
                self.config_json['camera' + str(cam_indx)]['width'] = 5120
                self.config_json['camera' + str(cam_indx)]['height'] = 720
        print('g2')

    def set3_sdk(self):
        self.config_json['general']['run_mode'] = 0
        self.config_json['recorder']['clip_length'] = 5
        self.config_json['tcp_server']['enable'] = 1
        self.config_json['tcp_server']['server_image'] = 1
        print('g3')


class fcm_configuration():
    def __init__(self, config_content, choosen_mode):
        self.config_content = config_content
        eval('self.' + choosen_mode + '()')
        print('fcm config updated')

    def set1_12fps(self):
        self.config_content['general']['can_number'] = 2
        self.config_content['general']['fps'] = 12
        self.config_content['recorder']['enable'] = 1
        self.config_content['detection']['enable'] = 1
        self.config_content['lane']['enable'] = 1
        self.config_content['prohibition']['enable'] = 1
        self.config_content['speed_limit']['enable'] = 1
        self.config_content['traffic_light']['enable'] = 1
        self.config_content['roadmark']['enable'] = 1
        print('f1')

    def set2_15fps(self):
        self.config_content['general']['can_number'] = 2
        self.config_content['general']['fps'] = 15
        self.config_content['recorder']['enable'] = 1
        self.config_content['detection']['enable'] = 1
        self.config_content['lane']['enable'] = 1
        self.config_content['prohibition']['enable'] = 0
        self.config_content['speed_limit']['enable'] = 0
        self.config_content['traffic_light']['enable'] = 0
        self.config_content['roadmark']['enable'] = 0
        print('f2')


def method0_pass_all_config(config_content):
    def is_dict(dict_a):
        value_list = []
        if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
            for x in dict_a:
                # temp_key = dict_a.keys()[x]
                temp_value = dict_a[x]
                # print ("%s %s"%(x, temp_value))
                is_dict(temp_value)  # 自我调用实现无限遍历
        else:
            value_list.append(dict_a)
        return value_list

    modify_list = []
    for config_keys in config_content:
        for mim_keys, mim_values in config_content[config_keys].items():
            print(config_keys, mim_keys, mim_values)
            change_to_val = input()
            if change_to_val:
                value_type = type(mim_values)
                modify_list.append([config_keys, mim_keys, value_type(change_to_val)])
    for need_modify_data in modify_list:
        config_content[need_modify_data[0]][need_modify_data[1]] = need_modify_data[2]
    return config_content


class mode_process_and_exit():
    def __init__(self, machine_ip, json_file, camera_model):
        # self.json_content = read_json_file()
        self.json_content = json_file
        remote = remote_connect.remote_connect(machine_ip)
        remote.SSHConnection()
        self.remote = remote
        self.usr_interaction = user_interaction.interacte_model(self.json_content)
        self.start_process(camera_model)
        self.remote.close_ssh()

    def start_process(self, camera_model):
        mode_num = self.usr_interaction.what_need_config('machine_mode', camera_model)
        choosen_mode = self.json_content['machine_mode'][mode_num]
        print('vbox配置功能暂时取消')
        """ 目前取消vbox及calmcar上传功能 """
        # self.upload_package(choosen_mode)
        if choosen_mode == 'gather':
            self.gather_process()
        elif choosen_mode == 'fcm':
            self.fcm_process()
        elif choosen_mode == 'bsd':
            self.bsd_process()
        else:
            print('mode process unknown error')

    def upload_package(self, choosen_mode):
        if choosen_mode == 'fcm' or choosen_mode == 'bsd':
            # calmcar_name = self.json_content['calmcar_located'].split('/')[-1]
            print('pls input calmcar package loacted:')
            calmcar_located = input()
            calmcar_name = calmcar_located.split('/')[-1]
            self.remote.upload_file(calmcar_located, '/home/nvidia/' + calmcar_name)
            self.remote.set_command_normal('tar -xvf ' + calmcar_name)
        # vbox_name = self.json_content['vbox_located'].split('/')[-1]
        print('pls input vbox package loacted:')
        vbox_located = input()
        vbox_name = vbox_located.split('/')[-1]
        self.remote.upload_file(vbox_located, '/home/nvidia/' + vbox_name)
        self.remote.set_command_normal('tar -xvf ' + vbox_name)
        print('package upload and unpack')

    def _follow_up_process(self, config_content, upload_located):
        f = codecs.open('config.json', 'w', 'utf-8')
        f.write(json.dumps(config_content, sort_keys=False, indent=4, ensure_ascii=False))
        f.close()
        self.remote.upload_file('config.json', upload_located)
        subprocess.call('rm -rf config.json', shell=True)

    def gather_communication_update(self):
        config_data = self.remote.set_command_normal('cat /home/nvidia/vbox/communication/config.json', loadtype='str')
        config_data = json.loads(config_data, object_pairs_hook=OrderedDict)
        config_data['shared_memory']['filename'] = 'vbox'
        self._follow_up_process(config_data, '/home/nvidia/vbox/communication/config.json')

    def fcm_vbox_update(self):
        # ~~~~~~~~~~~~~~~update vbox~~~~~~~~~~~~~~
        vbox_config = self.remote.set_command_normal('cat /home/nvidia/vbox/bin/config.json', loadtype='str')
        vbox_config = json.loads(vbox_config, object_pairs_hook=OrderedDict)
        vbox_config['general']['run_mode'] = 1
        self._follow_up_process(vbox_config, '/home/nvidia/vbox/bin/config.json')
        # ~~~~~~~~~~~~~~~vbox updated~~~~~~~~~~~~

    def gather_process(self):
        self.gather_communication_update()
        origin_config_data = self.remote.set_command_normal('cat /home/nvidia/vbox/bin/config.json', loadtype='str')
        origin_config_data = json.loads(origin_config_data, object_pairs_hook=OrderedDict)
        g_mode_number = self.usr_interaction.what_need_config('gather_method')
        choosen_g_mode = self.json_content['gather_method'][g_mode_number]
        if 'order_alone' in choosen_g_mode:
            config_after_modify = method0_pass_all_config(origin_config_data)
        else:
            series_result = []
            for ix in index_command:
                series_result += self.remote.set_command_normal('if [ -e %s ]; then echo True;else echo False;fi' % ix)
            series_result = [_.replace('\n', '') for _ in series_result]
            ensure_series_name = index_name[series_result.index('True')]
            print('the series num: ', ensure_series_name)
            config_after_modify = gather_configuration(origin_config_data, choosen_g_mode,
                                                       ensure_series_name).config_json
        self._follow_up_process(config_after_modify, '/home/nvidia/vbox/bin/config.json')
        print('gather mode config done')

    def fcm_process(self):
        self.fcm_vbox_update()
        calmcar_config = self.remote.set_command_normal('cat /home/nvidia/calmcar/bin/config.json', loadtype='str')
        calmcar_config = json.loads(calmcar_config, object_pairs_hook=OrderedDict)
        f_mode_num = self.usr_interaction.what_need_config('fcm_method')
        choosen_f_mode = self.json_content['fcm_method'][f_mode_num]
        if 'order_alone' in choosen_f_mode:
            calmcar_config_after_modify = method0_pass_all_config(calmcar_config)
        else:
            calmcar_config_after_modify = fcm_configuration(calmcar_config, choosen_f_mode).config_content
        self._follow_up_process(calmcar_config_after_modify, '/home/nvidia/calmcar/bin/config.json')
        print('fcm mode config done')

    def bsd_process(self):
        self.fcm_vbox_update()
        self.remote.set_command_normal('cd /home/nvidia/calmcar/bin && mv bsd.json config.json')
        bsd_config = self.remote.set_command_normal('cat /home/nvidia/calmcar/bin/config.json', loadtype='str')
        bsd_config = json.loads(bsd_config, object_pairs_hook=OrderedDict)
        bsd_config['recorder']['enable'] = 1
        self._follow_up_process(bsd_config, '/home/nvidia/calmcar/bin/config.json')
        print('bsd mode config done')


# if __name__ == '__main__':
    # a = mode_process_and_exit('192.168.196.220')
