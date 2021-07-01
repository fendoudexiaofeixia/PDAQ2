from scp import SCPClient
import paramiko
import time
import numpy as np
from pexpect import *
import socket


class remote_connect():
    def __init__(self, ip):
        self.ip = ip
        self.usrname = 'nvidia'
        self.password = 'Ap4K5m'
        self.port = 22

    def SSHConnection(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.usrname, self.password)
        self.ssh = ssh

    def set_command_normal(self, cmd, loadtype=''):
        stdin, stdout, stderr = self.ssh.exec_command(cmd, timeout=120)
        if loadtype == 'bytes':
            out = stdout.read().splitlines()
        elif loadtype == 'str':
            out = stdout.read()
            out = out.decode('utf-8')
        else:
            out = stdout.readlines()
        # err = stderr.readlines()
        return out

    def set_command_jurisdiction(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd, get_pty=True, timeout=120)
        stdin.write(self.password + '\n')
        out = stdout.readlines()
        err = stderr.readlines()
        return out

    def upload_file(self, localfile, remotefile):
        scpclient = SCPClient(self.ssh.get_transport(), socket_timeout=60)
        scpclient.put(localfile, remotefile)

    def download_file(self, remotefile, localfile):
        scpclient = SCPClient(self.ssh.get_transport(), socket_timeout=60)
        scpclient.get(remotefile, localfile)

        # sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        # sftp = self.ssh.open_sftp()
        # sftp.get(remotefile, localfile)

    def close_ssh(self):
        self.ssh.close()
