FROM centos:7.5.1804

WORKDIR /home/query_omdb_api

RUN yum -y install epel-release && \
    yum --enablerepo=updates clean metadata && \
    yum -y install httpd httpd-devel gcc make zlib-devel bzip2-devel openssl-devel libffi-devel && \
    yum -y --enablerepo='*' clean all && \
    rm -rf /var/cache/yum

RUN curl -L -o python.tgz https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz && \
  echo "85bb9feb6863e04fb1700b018d9d42d1caac178559ffa453d7e6a436e259fd0d python.tgz" | sha256sum -c | grep OK && \
  mkdir python_source && \
  tar -xf python.tgz -C python_source --strip 1 && \
  cd python_source && \
  ./configure --enable-shared && \
  make -j 4 && \
  make install && \
  cd .. && \
  rm -rf python_source

RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/usr-local-lib.conf && \
  ldconfig && \
  pip3 install --upgrade pip setuptools

COPY ["requirements.txt", "/home/query_omdb_api/requirements.txt"]
RUN pip3 install -r requirements.txt

copy ["query_omdb_api.py", "/home/query_omdb_api/query_omdb_api.py"]

CMD python3 query_omdb_api.py
