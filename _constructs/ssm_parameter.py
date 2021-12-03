from aws_cdk import aws_ssm
from constructs import Construct


class SsmStringParameter(Construct):
    def __init__(self,
                 scope: Construct,
                 id: str,
                 parameter_name: str,
                 string_value: str,
                 ) -> None:
        super().__init__(scope, id)

        aws_ssm.StringParameter(
            scope=self,
            id=f'{id}-construct',
            parameter_name=parameter_name,
            string_value=string_value,
            type=aws_ssm.ParameterType.STRING,
            tier=aws_ssm.ParameterTier.STANDARD,
        )


class StringListParameter(Construct):
    def __init__(self,
                 scope: Construct,
                 id: str,
                 parameter_name: str,
                 string_list_value: list,
                 ) -> None:
        super().__init__(scope, id)

        aws_ssm.StringListParameter(
            scope=self,
            id=f'{id}-construct',
            parameter_name=parameter_name,
            string_list_value=string_list_value,
            tier=aws_ssm.ParameterTier.ADVANCED
        )
