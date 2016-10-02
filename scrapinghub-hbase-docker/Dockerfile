# HBase in Docker
#
# Version 0.3

# http://docs.docker.io/en/latest/use/builder/

FROM ubuntu:14.04
MAINTAINER Dave Beckett <dave@dajobe.org>

COPY *.sh /build/

ENV HBASE_VERSION 1.1.4

RUN /build/prepare-hbase.sh && \
    cd /opt/hbase && /build/build-hbase.sh \
    cd / && /build/cleanup-hbase.sh && rm -rf /build

RUN apt-get update && apt-get install -y curl vim

VOLUME /data

ADD ./hbase-site.xml /opt/hbase/conf/hbase-site.xml

ADD ./zoo.cfg /opt/hbase/conf/zoo.cfg

ADD ./hbase-server /opt/hbase-server

# REST API
EXPOSE 8080
# REST Web UI at :8085/rest.jsp
EXPOSE 8085
# Thrift API
EXPOSE 9090
EXPOSE 9091
# Thrift Web UI at :9095/thrift.jsp
EXPOSE 9095
# HBase's Embedded zookeeper cluster
EXPOSE 2181
# HBase Master web UI at :16010/master-status;  ZK at :16010/zk.jsp
EXPOSE 16010

CMD ["/opt/hbase-server"]
