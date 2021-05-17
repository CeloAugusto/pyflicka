from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyflicka",
    version="1.0.0",
    author="CeloAugusto",
    description="Randomly moves the mouse.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CeloAugusto/pyflicka",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "pynput",
    ],
)
