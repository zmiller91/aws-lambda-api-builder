import json
import os

EXECUTABLE_NAME = 'api_builder'
APPLICATION_DESCRIPTION = '''
This is a CLI to build, package, and release AWS APIs using API Gateway and Lambda.
'''
ZLAB_CONF_FILE = "zlab-conf.json"


def check_bootstrap():
    if not os.path.exists(ZLAB_CONF_FILE):
        raise ValueError("Application not bootstrapped.  Run `zlab bootstrap --name {ApplicationName}` to boostrap")

def get_zlab_conf():
    with open(ZLAB_CONF_FILE) as conf:
        return json.load(conf)

def write_zlab_conf(conf):
    f = open(os.path.join(ZLAB_CONF_FILE), 'w')
    f.write(json.dumps(conf))
    f.close()