# 这是dbt-snowflake和airflow的第一个项目
> 概述
- 该项目使用了snowflake里的示例数据库tpch数据库，实现了将snowflake_smaple_data数据库里的数据ETL到了目标数据库dbt_demo里的Public schema下
# 主要的技术点
1. 自主整合了dbt-snowflake 和airflow
2. 开发了自己的dbtOperator，实现了直接使用dbt的原生语句直接在dags里操作
3. codegen生成source 和Model的代码
4. airflow使用了TriggerDagRunOperator,建立了Dags之间的关系

# 未实现
1. 项目过于简单，没有涉及到SDC type 2
2. airflow的配置，本次没有设置，直接使用了以前的docker image
3. 失败后的处理，发邮件没有完善
4. data quality 无