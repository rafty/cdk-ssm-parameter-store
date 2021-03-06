from aws_cdk import Stack
from constructs import Construct
from _constructs.ssm_parameter_construct import SsmStringParameter
from _constructs.ssm_parameter_construct import StringListParameter


class SsmParameterStoreStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        SsmStringParameter(
            self,
            id='SsmStringParameter-email-dev',
            parameter_name='/my-site/alerts-email-dev',
            string_value='hoge-dev@example.com',
        )

        StringListParameter(
            self,
            id='SsmStringParameter-environments',
            parameter_name='/my-site/environments',
            string_list_value=['dev', 'stg', 'prod']
        )
