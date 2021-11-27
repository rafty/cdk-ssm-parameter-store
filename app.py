#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from _stacks.ssm_parameter_store_stack import SsmParameterStoreStack
from _stacks.ssm_parameter_read_stack import TestReadParameterStack

environment = cdk.Environment(
    account=os.environ.get('CDK_DEPLOY_ACCOUNT', os.environ['CDK_DEFAULT_ACCOUNT']),
    region=os.environ.get('CDK_DEPLOY_REGION', os.environ['CDK_DEFAULT_REGION']),
)

app = cdk.App()
SsmParameterStoreStack(app, 'CdkSsmParameterStoreStack', env=environment)
TestReadParameterStack(app, 'GetValueFromSsmParameterStoreStack', env=environment)

app.synth()
