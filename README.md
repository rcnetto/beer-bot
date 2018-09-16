1. Install Python
$ sudo apt install pip

2. Fix PIP bug
https://stackoverflow.com/questions/28210269/importerror-cannot-import-name-main-when-running-pip-version-command-in-windo

In linux you need to modify file: /usr/bin/pip from:

from pip import main
if __name__ == '__main__':
    sys.exit(main())
to this:

from pip import __main__
if __name__ == '__main__':
    sys.exit(__main__._main())

3. Install Scrapy
pip install Scrapy --user
https://doc.scrapy.org/en/latest/intro/install.html#intro-install

4. Run crawl
scrapy crawl bahiamalte.com.br

4. pip install virtualenv --user

5. sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
