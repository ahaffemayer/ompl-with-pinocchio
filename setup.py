from setuptools import setup, find_packages

setup(
    name="ompl-with-pinocchio",
    version="0.1.0",
    description="A package to bridge OMPL and Pinocchio for motion planning.",
    author="Arthur Haffemayer",
    author_email="arthur.haffemayer@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)