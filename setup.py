import re
from codecs import open
from os import path

from setuptools import setup

name = "kedro-glue"
here = path.abspath(path.dirname(__file__))

# get package version
package_name = name.replace("-", "_")
with open(path.join(here, package_name, "__init__.py"), encoding="utf-8") as f:
    version = re.search(r'__version__ = ["\']([^"\']+)', f.read()).group(1)

# get the dependencies and installs
with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]

# get test dependencies and installs
with open("test_requirements.txt", "r", encoding="utf-8") as f:
    test_requires = [x.strip() for x in f if x.strip() and not x.startswith("-r")]


# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    name=name,
    version=version,
    description="Kedro-Glue makes it easy to deploy Kedro projects to Glue",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/quantumblacklabs/kedro-glue",
    author="QuantumBlack Labs",
    python_requires=">=3.5, <3.8",
    install_requires=requires,
    tests_require=test_requires,
    license="Apache Software License (Apache 2.0)",
    packages=["kedro_glue"],
    package_data={"kedro_glue": []},
    zip_safe=False,
    entry_points={
        "kedro.project_commands": ["glue = kedro_glue.plugin:commands"]
    },
)
