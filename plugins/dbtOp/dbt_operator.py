from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException
import subprocess
import os
from subprocess import run, PIPE



class DbtOperator(BaseOperator):


    @apply_defaults
    def __init__(self, dbt_command, dbt_project_dir='/my_dbt', *args, **kwargs):

        print(os.getcwd())
        super(DbtOperator, self).__init__(*args, **kwargs)
        self.dbt_command = dbt_command
        self.dbt_project_dir = dbt_project_dir

    def execute(self, context):

        self.log.info(f'Executing DbtOperator with dbt_command={self.dbt_command}')

        # 构建要执行的 bash 命令
        bash_command = f'cd {self.dbt_project_dir} && {self.dbt_command}'
           # 使用 subprocess 模块执行 bash 命令，并实时输出到标准输出
        process = subprocess.Popen(
            bash_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            universal_newlines=True
        )

        # 读取并打印命令输出
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.log.info(output.strip())

        # 检查命令执行结果
        if process.returncode != 0:
            # 如果命令返回值不为 0，则表示命令执行失败
            raise AirflowException(f'Dbt command execution failed with return code {process.returncode}')
        else:
            # 如果命令返回值为 0，则表示命令执行成功
            self.log.info('Dbt command execution successful')
