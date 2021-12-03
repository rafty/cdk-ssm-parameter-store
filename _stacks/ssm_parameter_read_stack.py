import json
from aws_cdk import Stack
from aws_cdk import CfnOutput
from constructs import Construct
from aws_cdk import aws_ssm


class TestReadParameterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        email = aws_ssm.StringParameter.value_for_string_parameter(
            scope=self,
            parameter_name='/my-site/alerts-email-dev'
        )

        CfnOutput(
            scope=self,
            id='parameter-email',
            value=email
        )

        environments = aws_ssm.StringListParameter.from_string_list_parameter_name(
            scope=self,
            id='GetEnvironmentFromSsmParameter',
            string_list_parameter_name='/my-site/environments',
        )

        CfnOutput(
            scope=self,
            id='parameter_environments',
            value=json.dumps(self.resolve(environments.string_list_value))
        )

        token = aws_ssm.StringParameter.value_for_secure_string_parameter(
            scope=self,
            parameter_name='/my-site/token',
            version=1
        )

        # cdk.CfnOutput(
        #     scope=self,
        #     id='parameter-token',
        #     value=token
        # )
