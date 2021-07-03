import codecs
import json
import subprocess
from collections import OrderedDict

from cloud_plaform.remote import remote_connect


class pdaq_process:
    def __init__(self, machine_ip, device_number):
        self.device_number = device_number
        # self.customer_name = customer_whole_name
        # self.ip = machine_ip
        self.remote = remote_connect.remote_connect(machine_ip)
        self.remote.SSHConnection()

    def update_pdaq_json(self):
        pdaq_config = self.remote.set_command_normal('cat /etc/pdaq.json', loadtype='str')
        pdaq_config = json.loads(pdaq_config, object_pairs_hook=OrderedDict)
        old_dev_num = pdaq_config['info']['dev_No']
        pdaq_config['info']['dev_No'] = self.device_number
        f = codecs.open('pdaq.json', 'w', 'utf-8')
        f.write(json.dumps(pdaq_config, sort_keys=False, indent=4, ensure_ascii=False))
        f.close()
        self.remote.upload_file('pdaq.json', '/home/nvidia/pdaq.json')
        self.remote.set_command_jurisdiction('sudo mv /home/nvidia/pdaq.json /etc/')
        subprocess.call('rm -rf pdaq.json', shell=True)
        return old_dev_num
