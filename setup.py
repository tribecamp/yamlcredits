from setuptools import setup

def readme():
  with open("README.md") as f:
    return f.read()

setup(
  name="yamlcredits",
  version="1.0.0",
  description="Small tool for generating a CREDITS.md from YAML files.",
  long_description=readme(),
  url="http://github.com/tribecamp/yamlcredits",
  author="Tribecamp",
  author_email="support@tribecamp.com",
  license="MIT",
  keywords="tribecamp yaml credits markdown",
  python_requires=">=3.6",
  packages=["yamlcredits"],
  scripts=["bin/yamlcredits"],
  install_requires=[
    "PyYAML==5.3.1"
  ]
)
