#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class ImmerConan(ConanFile):
    name = "immer"
    version = "0.4.0"
    url = "https://github.com/slepasteur/conan-immer.git"
    homepage = "https://github.com/arximboldi/immer"
    author = "Simon Lepasteur <slepasteur@gmail.com>"
    description = "Postmodern immutable and persistent data structures for C++"
    license = "MIT"
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"
    
    def source(self):
        self.run("git clone https://github.com/arximboldi/immer")
        os.rename("immer", self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*.h", dst=os.path.join("include", "immer"), src=os.path.join(self._source_subfolder, "immer"))
        self.copy(pattern="*.hpp", dst=os.path.join("include", "immer"), src=os.path.join(self._source_subfolder, "immer"))

    def package_id(self):
        self.info.header_only()