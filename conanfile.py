from conans import ConanFile, CMake
from conans import tools
import os
import shutil

class libjpegConan(ConanFile):
    name = "libjpeg"
    version = "9a"
    url = "https://github.com/Kaosumaru/conan-libjpeg"
    settings = "os", "compiler", "build_type", "arch"
    exports = "libjpeg/*"


    libjpeg_name = "jpeg-%s" % version
    source_tgz = "http://www.ijg.org/files/jpegsr%s.zip" % version
    cmake_file = "https://raw.githubusercontent.com/Kaosumaru/conan-libjpeg/master/CMakeLists.txt"
    jconfig_file = "https://raw.githubusercontent.com/Kaosumaru/conan-libjpeg/master/jconfig.h.cmake"

    def source(self):
        self.output.info("Downloading %s" % self.source_tgz)
        tools.download(self.source_tgz, "libjpeg.zip")
        tools.unzip("libjpeg.zip", ".")
        os.unlink("libjpeg.zip")

        self.output.info("Downloading %s" % self.cmake_file)
        tools.download(self.cmake_file, "%s/CMakeLists.txt" % self.libjpeg_name)
        tools.download(self.jconfig_file, "%s/jconfig.h.cmake" % self.libjpeg_name)


    def config(self):
        pass

    def build(self):


        cmake = CMake(self.settings)
        self.run('cd %s && cmake -DCMAKE_INSTALL_PREFIX:PATH=../install . %s' % (self.libjpeg_name, cmake.command_line))
        self.run("cd %s && cmake --build . --target install %s" % (self.libjpeg_name, cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="install/include")
        self.copy("*.lib", dst="lib", src="install/lib")
        self.copy("*.a", dst="lib", src="install/lib")

        if not self.options.static:
            self.copy("*.dll", dst="bin", src="install/bin")

    def package_info(self):
        self.cpp_info.libs = ["jpeg"]
