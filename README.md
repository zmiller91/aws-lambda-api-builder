###Requirements

* Python 3.6
* Pip 

### Install Dependencies

* **pipenv**
```commandline
pip install pipenv
```
* **awscli**
```commandline
pip install awscli
```

### Install aws-lambda-api-builder

Install from pip:

```commandline
pip install aws-lambda-api-builder
```

Install from Github

```commandline
git clone https://github.com/zmiler91/aws-lambda-api-builder
cd aws-lambda-api-builder
pipenv install
python setup.py sdist bdist_wheel
pipenv install -e .
```

If you've installed aws-lambda-api-builder from Github then you will need to use `pipenv shell` in order for your `zlab` 
to be recognized. 

```commandline
pipenv shell
zlab --help

> usage: api_builder [sub-command] [options]
> 
> This is a CLI to build, package, and release AWS APIs using API Gateway and
> Lambda.
> 
> positional arguments:
>  {lambda}
> 
> optional arguments:
>   -h, --help
```

### Setup

Since aws-lambda-api builder uses boto3 to interact with AWS, you will need to install and configure the AWS CLI. If you
have not already installed the AWS CLI, please refer to the "Install Dependencies" section of this README.

#### Creating an S3 bucket

`aws-lambda-api-builder` will upload a zipped archive of your application to S3 so it can be used in your Lambda 
functions. You can use the AWS console to create an S3 bucket; for the purposes of this README I've created a bucket 
called `my-example-api`.

#### Creating an IAM Policy

We will be creating an IAM User for `aws-lambda-api-builder` in the next section, but before we do so we will need
to create an IAM Policy so we can limit the user's permissions and only allow them to read out of the bucket created
in the previous section.

You can create this policy using the Visual Editor or you can copy the JSON document below replacing `my-example-api`
with the name of your S3 bucket: 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": [
                "arn:aws:s3:::my-example-api/*"
            ]
        }
    ]
}
```

Once you've defined your policy you will need to give your policy a name, for the purposes of this README I've name my
policy `aws-lambda-api-builder-s3`. You can also give your policy an optional description. If you want to grant
access to multiple buckets, then you just need to add the bucket to the `Resource` array in the policy document.

#### Creating an IAM User

aws-lambda-api-builder needs access to some resources in your AWS account so it can upload S3 files that contain your 
zipped archive.  To do this, you'll want to create an IAM user in the AWS console.  

```
User name: aws-api-lambda-builder
Access type: Programmatic access
```

After you've defined the name and access type, you will be asked to set a permission.  You can use the "Attach existing
policies directly" option and find and select the policy created in the previous section. 

Once the user has been created you will be provided an "Access key ID" and a "Secret access key", you will want to 
remember both of these. Your credentials will only be provided to you once, so you will not be able to recover them
if you do not write them down. 

#### Configure AWS

Once you've created your IAM user you will need to configure the AWS CLI.

```commandline
aws configure
> AWS Access Key ID [None]: {access key from the previous section}
> AWS Secret Access Key [None]: {secret access key from the previous section}
> Default region name [None]: {the aws region you're using, mine is us-east-1}
> Default output format [None]:
```

Your configuration and access keys will be saved to the `.aws` directory in your home directory. If you've already
configured your AWS CLI with another user, then you can attach the IAM Policy created in the previous section to
this user.  

### Development Environment

Integrate the pipenv environment by following the instructions here: https://www.jetbrains.com/help/pycharm/pipenv.html

### Usage Examples

```commandline
$ zlab lambda --help
```