 #! /usr/bin/env python

 # Copyright 2017 --Yang Hu--
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 

__author__ = 'Yang Hu'

import paramiko, os
def install_registry(vm, install_script):
	try:
		print '%s: ====== Start Docker Registry Installing ======' % (vm.ip)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(vm.ip, username=vm.user, key_filename=vm.key)
		sftp = ssh.open_sftp()
		sftp.chdir('/root/')
		file_path = os.path.dirname(__file__)
		registry_script = file_path + "/" + "docker_registry.sh"
		sftp.put(registry_script, "registry_setup.sh")
		stdin, stdout, stderr = ssh.exec_command("sudo sh /root/registry_setup.sh")
		stdout.read()
		sftp.put(install_script, "images_setup.sh")
		stdin, stdout, stderr = ssh.exec_command("sudo sh /root/images_setup.sh")
		stdout.read()
		print '%s: ========= Docker Registry Installed =========' % (vm.ip)
	except Exception as e:
		print '%s: %s' % (vm.ip, e)
	ssh.close()




