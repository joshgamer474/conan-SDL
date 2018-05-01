from conans import ConanFile
from conans.tools import download, unzip

class SDL(ConanFile):

    name = "SDL"
    version = "2.0.8"
    url = "https://www.libsdl.org/download-2.0.php"
    license = "zlib"
    description = "Simple DirectMedia Layer is a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D"
    settings = {"os" : ["Windows"], 
                "arch": ["x86", "x86_64"]}
    
    def source(self):
        if self.settings.arch == "x86_64":
            arch = "x64"
        else:
            arch = "x86"
        
        site = "https://www.libsdl.org/release/"
        zipName = "SDL2-%s-win32-%s.zip" % (self.version, arch)
        download(site + zipName, zipName)
        unzip(zipName)
    
    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        
    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
    