from setuptools import find_packages, setup

setup(
    name="dagster_mlflow_project",
    packages=find_packages(exclude=["dagster_mlflow_project_tests"]),
    install_requires=[
        "dagster",
        "mlflow",
        "numpy",
        "pandas",
        "scikit-learn",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
