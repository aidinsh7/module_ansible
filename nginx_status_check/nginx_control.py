
from ansible.module_utils.basic import AnsibleModule
import subprocess

def check_nginx_status():
    try:
        result = subprocess.run(['systemctl', 'is-active', 'nginx'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip() == "active"
    except subprocess.CalledProcessError:
        return False

def start_nginx():
    try:
        subprocess.run(['systemctl', 'start', 'nginx'], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    nginx_active = check_nginx_status()
    
    if not nginx_active:
        start_success = start_nginx()
        if start_success:
            module.exit_json(changed=True, msg="Nginx service started successfully.")
        else:
            module.fail_json(msg="Failed to start Nginx service.")
    else:
        module.exit_json(changed=False, msg="Nginx service is already active.")

if __name__ == '__main__':
    main()
