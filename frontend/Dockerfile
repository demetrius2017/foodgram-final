FROM node:13.12.0-alpine as build

# Создаем группу и пользователя для безопасности
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Устанавливаем домашний каталог для нашего приложения
WORKDIR /app

# Используем созданного пользователя
USER appuser

# Копируем файлы package.json и package-lock.json (если он есть)
COPY package*.json ./

# Устанавливаем все зависимости, включая react и react-dom
RUN npm install

# Копируем остальные файлы
COPY . .

# Собираем проект
RUN npm run build

# Здоровье контейнера проверяется путем проверки доступности HTTP сервера
# HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1

# Команда для копирования результата сборки
CMD ["cp", "-r", "build", "result_build"]

