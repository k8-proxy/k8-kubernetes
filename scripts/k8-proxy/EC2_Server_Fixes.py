from pprint import pprint
from unittest import TestCase
from k8_kubernetes.kubernetes.Ssh import Ssh


class EC2_Server_Fixes:
    def __init__(self, ssh_config):
        self.ssh_config  = ssh_config
        self.ec2_ssh     = Ssh(self.ssh_config)
        self.logs_folder = '/run/desktop/mnt/host/c/'


class test_EC2_Server_Fixes(TestCase):

    def setUp(self) -> None:
        self.ssh_config = {
            "user"    : "ubuntu"                                        ,
            "server"  : '54.155.152.233', #'18.202.249.123'                                ,

            "ssh_key" : '/Users/diniscruz/_dev/_AWS_Config/packer.pem'
        }
        self._ = EC2_Server_Fixes(self.ssh_config)
        print()

    def test_k8_logs_folder_size(self):
        pprint(self._.k8_logs_folder_size())


