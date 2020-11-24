import netmiko

connection = netmiko.ConnectHandler(ip='172.16.98.128', device_type='cisco_ios', username='cisco',password='cisco123!')
print(connection.send_command('show ip int br'))

config_commands= [
    'interface loopback 0',
    'ip address 10.10.10.10 255.255.255.0',
    'description loopback created with netmiko'
     ]
setconfig = connection.send_config_set(config_commands)
#print (set_config)

