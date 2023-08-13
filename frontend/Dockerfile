# build env
FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm ci

COPY . .
RUN npm run build
RUN cp -r /app/build/* /usr/share/nginx/html/ # Добавленная строка
RUN npm install --global http-server

CMD ["npx", "-y", "http-server", "-p", "9000", "/app/build"]
