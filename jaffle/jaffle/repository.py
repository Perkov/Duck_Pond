from dagster import load_assets_from_package_module, repository, with_resources
from jaffle.duckpond import DuckDb
from dagster import resource
from jaffle import assets
from duckpond import DuckPondIOManager
from dagster import io_manager

@resource(config_schema={"vars":str})
def duckdb(init_context):
    return DuckDb(init_context.resource_config["vars"])

duckdb_localstack = duckdb.configured(
    {
        "vars":"""
set s3_access_key_id='test';
set s3_secret_access_key='test';
set s3_endpoint='https://0.0.0.0:4566;
set s3_use_ssl='false';
set s3_url_style='path';
"""
    }
)
     
@io_manager(required_resource_keys={"duckdb"})
def duckpond_io_manager(init_context):
    return DuckPondIOManager("datalake", init_context.resources.duckdb)


@repository
def jaffle():
    return [
        with_resources(
            load_assets_from_package_module(assets),
            ("io_namager":duckpond_io_manager, "duckdb": duckdb_localstack)
        )
    ]