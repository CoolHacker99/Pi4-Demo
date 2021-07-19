import configparser
import argparse
import paramiko
from scp import SCPClient

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('local_path', type=str)

    config = configparser.ConfigParser()
    config.read('config.ini')

    host_ip = config['SSH']['server']
    port = int(config['SSH']['port'])
    user = config['SSH']['user']
    password = config['SSH']['password']
    remote_path = config['SCP']['remote_path']
    local_path = parser.parse_args().local_path

    ssh = createSSHClient(host_ip, port, user, password)
    scp = SCPClient(ssh.get_transport())
    scp.put(local_path, remote_path=remote_path)
    scp.close()

    print(f'Сopying was successful to "{remote_path}"')

if __name__ == '__main__':
    main()
