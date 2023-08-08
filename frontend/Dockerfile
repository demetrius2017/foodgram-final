FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build
RUN mkdir -p result_build && \
    chmod -R 777 result_build
CMD cp -r build/* result_build/
