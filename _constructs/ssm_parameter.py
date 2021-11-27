from aws_cdk import core as cdk
from aws_cdk import aws_ssm


class SsmStringParameter(cdk.Construct):
    def __init__(self,
                 scope: cdk.Construct,
                 id: str,
                 parameter_name: str,
                 string_value: str,
                 ) -> None:
        super().__init__(scope, id)

        email_parameter = aws_ssm.StringParameter(
            scope=self,
            id=f'{id}-construct',
            # parameter_name='/my-site/alerts-email-dev',
            parameter_name=parameter_name,
            # string_value='hoge-dev@example.com',
            string_value=string_value,
            # description='alert on dev to the email',
            type=aws_ssm.ParameterType.STRING,
            tier=aws_ssm.ParameterTier.STANDARD,
            # allowed_pattern='.*'
        )


class StringListParameter(cdk.Construct):
    def __init__(self,
                 scope: cdk.Construct,
                 id: str,
                 parameter_name: str,
                 string_list_value: list,
                 ) -> None:
        super().__init__(scope, id)

        aws_ssm.StringListParameter(
            scope=self,
            id=f'{id}-construct',
            # parameter_name='/my-site/environments',
            parameter_name=parameter_name,
            # string_list_value=list(('dev', 'staging', 'prod')),
            string_list_value=string_list_value,
            tier=aws_ssm.ParameterTier.ADVANCED
        )
