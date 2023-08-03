FROM node:13.12.0-alpine as build

WORKDIR /app

# Копирование файлов package.json и package-lock.json (если он есть)
COPY package*.json ./

# Установка всех зависимостей, включая react и react-dom
RUN npm install

# Копирование остальных файлов
COPY . .

# Сборка проекта
RUN npm run build

# Команда для копирования результата сборки
CMD cp -r build result_build
