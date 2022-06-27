FROM ubuntu:20.04

WORKDIR /var/amqp_reverse_proxy/

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN set -ex; \
    apt update; \
    apt install -y --no-install-recommends \
    apache2 \
    curl \
    less \
    ; \
    rm -rf /var/lib/apt/lists/*

COPY reverse-proxy.conf /etc/apache2/sites-available/

RUN a2enmod proxy_http

RUN a2ensite reverse-proxy

