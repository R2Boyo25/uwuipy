import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="uwuipy",
    version="0.0.3",
    author="Cuprum77",
    description="Allows the easy implementation of uwuifying words for applications like Discord bots and websites",
    packages=["uwuipy"]
)