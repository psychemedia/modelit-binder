#!/usr/bin/env python3
# based on postBuild in https://github.com/ouseful-template-repos/binder-selenium-demoscraper
from webdriverdownloader import GeckoDriverDownloader
gdd = GeckoDriverDownloader()
gdd.download_and_install("v0.23.0")
