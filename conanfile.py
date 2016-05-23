from conans import ConanFile, CMake
from conans import tools
import os


class GumboConan(ConanFile):
    name = "Gumbo"
    version = "0.10.1"
    url = "https://github.com/google/gumbo-parser.git"
    license = "Apache License, Version 2.0"
    settings = "os", "compiler", "build_type", "arch"
    exports = "CMakeLists.txt"

    build_dir = "build"
    source_dir = "gumbo-parser-0.10.1"

    def source(self):
        tools.download("https://github.com/google/gumbo-parser/archive/v0.10.1.zip",
                       "gumbo-parser.zip")
        tools.unzip("gumbo-parser.zip")
        os.unlink("gumbo-parser.zip")

    def build(self):
        if self.settings.os == "Windows":
            self.run("IF not exist %s mkdir %s" % (self.build_dir, self.build_dir))
        else:
            self.run("mkdir %s" % self.build_dir)

        cmake = CMake(self.settings)
        self.run('cd %s && cmake .. %s -DGUMBO_PRJ_DIR:string=%s' % (self.build_dir, cmake.command_line, self.source_dir))
        self.run("cd %s && cmake --build . %s" % (self.build_dir, cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="%s/src" % self.source_dir)
        self.copy("*.lib", dst="lib", src=self.build_dir)
        self.copy("*.a", dst="lib", src=self.build_dir)

    def package_info(self):
        self.cpp_info.libs = ["gumbo"]
