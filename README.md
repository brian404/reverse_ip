# reverse_ip

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![python](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/)
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=2.0&x2=0)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

***A Python Based Non-Interactive  reverse_IP Script To Find The Domains On a Server***

### Requirements

- Python (2.7.*)
- Python `pip`
- Python module `requests`
- Python module `colorama`

### Install modules

	pip install -r requirements.txt
	
### Tested on

- Windows 7/8/8.1
- Kali linux (2017.1)
- Mac OSX 10.9.5
- Termux 0.117
	
### Changelog

- Integrated Reverse IP Via Hacker Target's Api as Well!
- Changed Script From Interactive To Non-Interactive.

### Usage

***Reverse IP Via Hacker Target's Api***

	python rev.py -r hackthissite.org

***Reverse IP Via YouGet Signal's Api***

	python rev.py -s hackthissite.org
	
***Reverse IP With Both Modules***

	python rev.py --all hackthissite.org
