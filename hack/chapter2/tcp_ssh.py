# coding=utf-8

# import os
import paramiko


def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    # path = os.path.join(os.environ['HOME'], '.ssh/known_hosts')
    # client.load_host_keys(path)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024)
    return


if __name__ == '__main__':
    ssh_command('127.0.0.1', 22, 'root', 'fuck', 'ls -a')
