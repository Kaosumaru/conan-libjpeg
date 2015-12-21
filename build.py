import os, sys
import platform


def system(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)


if __name__ == "__main__":
    system('conan export Kaosumaru/stable')
    params = " ".join(sys.argv[1:])

    if platform.system() == "Windows":
        for version in ["14", "12"]:
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Release '
                              '-s compiler.runtime=MD %s' % (version, params))
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Release '
                              '-s compiler.runtime=MT %s' % (version, params))
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Debug '
                              '-s compiler.runtime=MTd %s' % (version, params))  
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Debug '
                              '-s compiler.runtime=MDd %s' % (version, params))

    else:
        # Not implemented yet, can build many gcc versions with some work
        system('conan test -s compiler="gcc" -s build_type=Debug')
        system('conan test -s compiler="gcc" -s build_type=Release')
