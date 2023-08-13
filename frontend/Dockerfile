FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm ci

COPY . .
RUN npm run build
RUN mkdir -p /usr/share/nginx/html
RUN cp -r /app/build/* /usr/share/nginx/html/

RUN npm install --global http-server

CMD ["npx", "-y", "http-server", "-p", "9000", "/usr/share/nginx/html"]
