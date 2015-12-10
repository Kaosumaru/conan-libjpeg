from conans import ConanFile, CMake
from conans import tools
import os

class libjpegConan(ConanFile):
    name = "libjpeg"
    version = "9a"
    url = "https://github.com/Kaosumaru/conan-libjpeg"
    settings = "os", "compiler", "build_type", "arch"
    exports = "libjpeg/*"

    options = { "static": [True, False] }
    default_options = "=False\n".join(options.keys()) + "=False"

    libjpeg_name = "libjpeg-%s" % self.version
    source_tgz = "http://www.ijg.org/files/jpegsr%s.zip" % self.version

    def source(self):
        self.output.info("Downloading %s" % self.source_tgz)
        tools.download(self.source_tgz, "libjpeg.tar.gz")
        tools.unzip("libjpeg.tar.gz", ".")
        os.unlink("libjpeg.tar.gz")

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
        if self.options.static:
            self.cpp_info.libs = ["libjpeg_static"]
        else:
            self.cpp_info.libs = ["libjpeg"]
