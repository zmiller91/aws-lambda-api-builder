
import os
from api_builder import configuration
from api_builder import cloudformation

def get_description():
    return 'Bootstrap a Lambda API'


def set_args(parser):
    # todo: make non optional
    parser.add_argument("-n", "--name")


def execute(args):

    if os.path.exists("zlab-conf.json"):
        raise ValueError("Application has already been bootstrapped. Delete 'zlab-conf.json' to unbootstrap")

    conf = {
        "api_name": args.name
    }

    configuration.write_zlab_conf(conf)

    print("Updating bootstrap stack")
    conf['s3_bucket_name'] = 'zlab-' + conf["api_name"].lower() + '-lambda-code'
    configuration.write_zlab_conf(conf)
    cloudformation.main(conf["api_name"] + "-bootstrap", "cloudformation\\bootstrap.yml", conf)

