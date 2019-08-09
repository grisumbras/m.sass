from conans import (
    CMake,
    ConanFile,
    python_requires,
)
import os


b2 = python_requires("b2-helper/[>=0.5.0]@grisumbras/stable")


@b2.build_with_b2
class EnumFlagsTestConan(ConanFile):
    settings = "compiler"
    generators = "b2"

    def test(self):
        pass
