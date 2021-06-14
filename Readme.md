# Audible Dataset Generator v1.0
## Web Scraper using Selenium and Python to fetch audiobook details and required reviews for user from www.audible.com and convert to csv
# Dataset [Link](https://www.kaggle.com/rohitdass/audible-dataset) Updated on 02-06-2021
### Created on May 2021
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.7.8](https://img.shields.io/badge/python-3.7.8-blue.svg)](https://www.python.org/downloads/release/python-378/)
[![Selenium 3.141.0](https://img.shields.io/badge/Selenium-3.141.0-blue)](https://selenium-python.readthedocs.io/)
[![GitHub license](https://img.shields.io/github/license/rohit7044/Audible-Dataset-Generator-v1.0)](https://github.com/rohit7044/Audible-Dataset-Generator-v1.0/blob/main/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/rohit7044/Audible-Dataset-Generator-v1.0)](https://github.com/rohit7044/Audible-Dataset-Generator-v1.0/network)
[![GitHub stars](https://img.shields.io/github/stars/rohit7044/Audible-Dataset-Generator-v1.0)](https://github.com/rohit7044/Audible-Dataset-Generator-v1.0/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/rohit7044/Audible-Dataset-Generator-v1.0)](https://github.com/rohit7044/Audible-Dataset-Generator-v1.0/issues)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/rohit7044/Audible-Dataset-Generator-v1.0/graphs/commit-activity)


[![Stargazers repo roster for @rohit7044/Audible-Dataset-Generator-v1.0](https://reporoster.com/stars/rohit7044/Audible-Dataset-Generator-v1.0)](https://github.com/rohit7044/Audible-Dataset-Generator-v1.0/stargazers)
[![Forkers repo roster for @rohit7044/Audible-Dataset-Generator-v1.0](https://reporoster.com/forks/rohit7044/Audible-Dataset-Generator-v1.0)](https://github.com/rohit7044/Audible-Dataset-Generator-v1.0/network/members)
# Requirements
- Working Laptop/Desktop ?
- Latest [Python](https://www.python.org/downloads/) version should not be a problem.
  Disclaimer: [Python 3.7.8](https://www.python.org/downloads/release/python-378/) is installed on my system.
- [Selenium](https://selenium-python.readthedocs.io/) which when I installed was [3.141.0](https://pypi.org/project/selenium/).
- [Google Chrome](https://www.google.com/intl/en_in/chrome/)
- Since my Chrome version was 90, So this [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/) was the most compatible one for me. If you want   to download your compatible chromedriver then check you [Chrome version](https://www.google.com/chrome/update/) and then download the compatible [chromedriver](https://chromedriver.chromium.org/downloads)
- CSV reader (Microsoft Excel,etc..)
- IDE ([PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows))
# Optional Requirements
- [Chropath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo).For finding specific xpath if needed.
# Installation
Please go through the installations as stated in the requirements list above.
Set the python path and chromedriver path as well. I am not using virtual environments(not a fan of 🐍)

# FlowChart
![Flowchart](https://lucid.app/publicSegments/view/7d5f80b0-4a80-47f4-bf08-1a83357af28d/image.jpeg)
Click this badge for the process demo ? [![Workflow Video](https://img.shields.io/badge/YouTube-Workflow-red)](https://www.youtube.com/watch?v=9EtaHr72w1M)

# Important Notes
- The following robot needs the latest product list link and the audible.com website link
- Reviews_Crawler function takes the number of reviews you want (in multiples of 10)
- The show_more_open_times variable takes the number of times the showmore button should be clicked while taking reviews. Initially before clicking showmore button, there are 10 reviews, so every showmore button will generate 10 reviews. For Example - if I put 3 in show_more_open_times variable in main.py, the robot will click showmore button 2 times, generating 30 reviews(initially there are 10 reviews) and creating 30 review columns separately in csv.
- The csv file is encoded in utf-8
- Unfortunately this version(1.0) has no pause button nor multithreading, So the iteration of 1200 books or above will take some significant amount of time and if stopped it will again iterate from beginning, duplicating files into csv.
- I have not tested the iteration over 1200 books, So any issue please ping me up.
