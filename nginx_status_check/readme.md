Ansible Nginx Service Management Module
This Ansible module checks the status of the Nginx service and starts it if it is not already active. The module uses the systemctl command to interact with the system's service manager.

Requirements
Python 3
Ansible
Access to a system where Nginx is installed and managed by systemd
Features
Check if the Nginx service is active
Start the Nginx service if it is inactive
Returns a success or failure message based on the operation outcome
Module Usage


Example Playbook:
- name: Ensure Nginx is running
  hosts: your_target_host
  tasks:
    - name: Manage Nginx service
      script: path/to/your/script.py