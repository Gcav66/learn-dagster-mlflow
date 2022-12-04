from dagster import (
    load_assets_from_package_module,
    repository,
    define_asset_job,
    ScheduleDefinition,
)
from dagster_mlflow_project import assets

daily_job = define_asset_job(name="daily_refresh", selection="*")
daily_schedule = ScheduleDefinition(
    job=daily_job,
    cron_schedule="@daily",
)

@repository
def dagster_mlflow_project():
    return [
        daily_job,
        daily_schedule,
        load_assets_from_package_module(assets),
    ]
