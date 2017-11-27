FROM node:carbon

WORKDIR /usr/code
COPY package.json .
RUN npm install
COPY . . 

CMD [ "npm", "start" ]
