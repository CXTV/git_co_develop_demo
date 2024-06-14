{{ codegen.generate_source(
    name = 'tpch',
    schema_name = 'TPCH_SF1',
    database_name = 'SNOWFLAKE_SAMPLE_DATA',
    table_names = ['ORDERS','LINEITEM'],
    include_descriptions  = True,
    generate_columns  =True
) }}