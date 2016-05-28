from conans import ConanFile, CMake
from conans import tools
import os


class GumboConan(ConanFile):
    name = "Gumbo"
    version = "0.10.1"
    #original project url = "https://github.com/google/gumbo-parser.git"
    url = "https://github.com/ruipires/conan-gumbo.git" # repo of this wrapper
    license = "Apache License, Version 2.0"
    settings = "os", "compiler", "build_type", "arch"
    exports = "CMakeLists.txt"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    build_dir = "build"
    source_dir = "gumbo-parser-%s" % version

    def source(self):
        tools.download("https://github.com/google/gumbo-parser/archive/v%s.zip" % self.version,
                       "gumbo-parser.zip")
        tools.unzip("gumbo-parser.zip")
        os.unlink("gumbo-parser.zip")

    def build(self):
        if self.settings.os == "Windows":
            self.run("IF not exist %s mkdir %s" % (self.build_dir, self.build_dir))
        else:
            self.run("mkdir %s" % self.build_dir)

        cmake = CMake(self.settings)

        activated = getattr(self.options, "shared")
        options = "-DBUILD_SHARED_LIBS=ON" if activated else "-DBUILD_SHARED_LIBS=OFF"

        self.run('cd %s && cmake .. %s -DGUMBO_PRJ_DIR:string=%s %s'
                        % (self.build_dir, cmake.command_line, self.source_dir, options))

        self.run("cd %s && cmake --build . %s"
                        % (self.build_dir, cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="%s/src" % self.source_dir)
        self.copy("*.lib", dst="lib", src=self.build_dir, keep_path=False)
        self.copy("*.a", dst="lib", src=self.build_dir, keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=self.build_dir, keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=self.build_dir, keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src=self.build_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gumbo"]
