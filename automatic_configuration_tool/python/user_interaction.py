class interacte_model:
    def __init__(self, config_content):
        self.config_content = config_content

    def start_config(self):
        print('\nstart configration the machine! all the config option should be fill in the index')
        # print('choosen_what you needed first...')
        print('')

    def config_num_check(self, a, invalidate_list):
        try:
            a = int(a)
            if a in invalidate_list:
                return a
            else:
                print('error input: config item input error')
                return None
        except:
            print('error input: config item input error')
            return None

    def get_ip(self):
        print('pls input the machine ip')
        ip = input()
        check_ip = ip.split('.')
        if len(check_ip) != 4 or False in [str.isdigit(_) for _ in check_ip] or False in [int(i) < 256 for i in
                                                                                          check_ip]:
            print('error input: ip format not correct')
            return None
        else:
            return ip

    def what_need_config(self, global_val_name,camera_model):
        print('choosen the ' + global_val_name + ' items :')
        currect_config_item = self.config_content[global_val_name]
        if not currect_config_item:
            print(global_val_name, 'name error')
            exit(0)
        for varl_indx, varl in enumerate(currect_config_item):
            print(str(varl_indx) + ' : ' + str(varl))
        print('')
        a = 0
        a = self.config_num_check(a, range(len(currect_config_item)))
        return a


if __name__ == '__main__':
    a = interacte_model()
    a.what_need_config('customer_name')
