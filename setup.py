from setuptools import setup

setup(
  name="yamlcredits",
  version="1.0.0",
  description="Small tool for generating a CREDITS.md from YAML files.",
  author="Tribecamp",
  author_email="support@tribecamp.com",
  packages=["yamlcredits"],
  scripts=["bin/yamlcredits"],
  install_requires=[
    "PyYAML==5.3.1"
  ]
)
