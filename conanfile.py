from conans import (
    ConanFile,
    python_requires,
)


b2 = python_requires("b2-helper/[>=0.5.0]@grisumbras/stable")


@b2.build_with_b2
class MSassConan(ConanFile):
    name = "m.sass"
    version = "0.1.0"
    description = "SASS version of m.css"
    url = "https://github.com/grisumbras/m.sass"
    homepage = url
    license = "MIT"

    exports_sources = (
        "LICENSE*",
        "jamroot.jam",
        "sass/*"
    )

    def package_info(self):
        self.info.header_only()
        self.cpp_info.includedirs = ["share/m.sass"]
