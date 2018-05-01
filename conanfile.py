from conans import ConanFile
from conans.tools import download, unzip
import os

class SDL(ConanFile):

    name = "SDL"
    version = "2.0.8"
    url = "https://www.libsdl.org/download-2.0.php"
    license = "zlib"
    description = "Simple DirectMedia Layer is a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D"
    settings = {"os" : ["Windows"], 
                "arch": ["x86", "x86_64"]}
    
    def source(self):
        site = "https://www.libsdl.org/release/"
        zipName = "SDL2-devel-%s-VC.zip" % self.version
        download(site + zipName, zipName)
        unzip(zipName)
    
    def package(self):
        if self.settings.arch == "x86_64":
            arch = "x64"
        else: 
            arch = "x86"
        folderName = "SDL2-%s" % self.version
        self.copy("*.h",   src=folderName + "/include",       dst="include", keep_path=False)
        self.copy("*.lib", src=folderName + "/lib/%s" % arch, dst="lib",     keep_path=False)
        self.copy("*.dll", src=folderName + "/lib/%s" % arch, dst="bin",     keep_path=False)
        self.copy("*.txt", src=folderName, dst="")
        
    def package_info(self):
        self.cpp_info.includedirs   = ["include"]
        self.cpp_info.libdirs       = ["lib"]
        self.cpp_info.bindirs       = ["bin"]
    