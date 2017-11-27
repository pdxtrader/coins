FROM python:3.6.0

RUN apt-get update -qq && apt-get install -yqq curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install -yqq nodejs
RUN apt-get clean -y

RUN npm install gulp -g

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /usr/code && cp -a /tmp/node_modules /usr/code

WORKDIR /usr/code
ADD . /usr/code
RUN rm -rf ./build
RUN rm -rf ./test
RUN rm -rf ./src
EXPOSE 8080
ENTRYPOINT [ "npm", "start" ]