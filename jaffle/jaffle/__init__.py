from dagster import Definitions, load_assets_from_package_module
from jaffle.duckpond import DuckPondIOManager, DuckDb
from jaffle import assets

duckdb_localstack = DuckDb("""
set s3_access_key_id='test';
set s3_secret_access_key='test';
set s3_endpoint='localhost:4566';
set s3_use_ssl='false';
set s3_url_style='path';
"""
)

defs = Definitions(
    assets=load_assets_from_package_module(assets),
    resources={
        "io_manager": DuckPondIOManager(bucket_name="datalake", duckdb=duckdb_localstack)
    }
)