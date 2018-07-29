import json
import os
from api_builder import configuration

def get_description():
    return 'Bootstrap a Lambda API'


def set_args(parser):
    # todo: make non optional
    parser.add_argument("-n", "--name")


def execute(args):

    if os.path.exists("zlab-conf.json"):
        raise ValueError("Application has already been bootstrapped. Delete 'zlab-conf.json' to unbootstrap")

    configuration.write_zlab_conf({
        "api_name": args.name
    })

