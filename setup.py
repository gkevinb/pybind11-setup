from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "simple",
        ["src/bindings.cpp", "src/simple.cpp"]
    ),
]

setup(
    name="simple",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)