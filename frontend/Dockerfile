FROM node:13.12.0-alpine as build

WORKDIR /app

# Копируем файлы зависимостей и устанавливаем зависимости
COPY package.json package-lock.json ./
RUN npm ci

# Копируем остальные файлы и собираем проект
COPY . .
RUN npm run build

# Устанавливаем http-server глобально
RUN npm install --global http-server

# Запускаем сервер на порту 9000
CMD ["http-server", "-p", "9000", "/app/build"]
