FROM python:3.3.6-wheezy

RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >> /etc/apt/sources.list
RUN apt-get update && apt-get install -qy libffi-dev libxml2-dev libxslt-dev libssl-dev sqlite3 libsqlite3-dev graphviz python-openssl
RUN pip3 install ipython scrapy lxml scrapyjs beautifulsoup4 requests
#crypto for splash
RUN yes | pip install --upgrade cryptography
RUN yes | pip uninstall cryptography
RUN LDFLAGS="-L/usr/lib/x86_64-linux-gnu" pip install cryptography --no-use-wheel
###
RUN pip3 install frontera[distributed,zeromq,sql,hbase,kafka] colorlog
RUN pip install urllib3
RUN pip3 install pydot scrapy_proxies scrapy-splash selenium treq
#RUN pip3 install --upgrade kafka-python
RUN mkdir /code
WORKDIR /code
# pry in python
# from IPython import embed
# embed() # this will drop us into IPython
