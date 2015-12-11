from conans import ConanFile, CMake
from conans import tools
import os
import shutil

class libjpegConan(ConanFile):
    name = "libjpeg"
    version = "9a"
    url = "https://github.com/Kaosumaru/conan-libjpeg"
    settings = "os", "compiler", "build_type", "arch"
    exports = "CMake/*"

    libjpeg_name = "jpeg-%s" % version
    source_tgz = "http://www.ijg.org/files/jpegsr%s.zip" % version


    def source(self):
        self.output.info("Downloading %s" % self.source_tgz)
        tools.download(self.source_tgz, "libjpeg.zip")
        tools.unzip("libjpeg.zip", ".")
        os.unlink("libjpeg.zip")

        self.output.info("Copying CMakeLists.txt")
        shutil.move("CMake/CMakeLists.txt", self.libjpeg_name)
        shutil.move("CMake/jconfig.h.cmake", self.libjpeg_name)


    def config(self):
        pass

    def build(self):


        cmake = CMake(self.settings)
        self.run('cd %s && mkdir build' % self.libjpeg_name)
        self.run('cd %s/build && cmake -DCMAKE_INSTALL_PREFIX:PATH=../../install .. %s' % (self.libjpeg_name, cmake.command_line))
        self.run("cd %s/build && cmake --build . --target install %s" % (self.libjpeg_name, cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="install/include")
        self.copy("*.lib", dst="lib", src="install/lib")
        self.copy("*.a", dst="lib", src="install/lib")

    def package_info(self):
        self.cpp_info.libs = ["jpeg"]
