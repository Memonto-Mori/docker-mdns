FROM ubuntu

MAINTAINER Brayan Espina "Brayan.espina@mail.udp.cl"
MAINTAINER Guillermo Correa "Guillermo.correa1@mail.udp.cl"

WORKDIR /Mdns

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \
&&  apt-get -y upgrade \
&& apt-get -y install build-essential \
&& apt-get -yqq install git elixir erlang pkg-config libssl-dev \
&& git clone https://github.com/rosetta-home/mdns 

RUN mix local.hex --force 

RUN chown root -R /Mdns 

RUN cd /Mdns/mdns \
&& mix do deps.get, deps.compile
 
RUN echo "cd /Mdns/mdns && iex -S mix" >> ~/.bashrc
