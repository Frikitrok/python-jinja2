from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('emr.conf')
config = {}
config['EMR_NAME'] = 'emr_56_1'
config['MASTER_IP'] = '192.168.54.11'
slave1 = {
    'name': 'datanode1',
    'ip': '192.168.54.18'
}
slave2 = {
    'name': 'datanode2',
    'ip': '192.168.54.25'
}
slaves = [slave1, slave2]
config['slaves'] = slaves
#Render the template with data and print the output
f = open('emr1.conf', 'w')
f.write(template.render(config))
