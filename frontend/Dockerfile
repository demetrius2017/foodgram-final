FROM node:18
WORKDIR /app

# Создание пользователя с ограниченными правами
RUN adduser -D myuser
USER myuser

# Копирование файлов package.json и package-lock.json
COPY package.json package.json
COPY package-lock.json package-lock.json

# Установка зависимостей и сборка проекта
RUN npm ci && \
    npm run build && \
    npm install --global http-server@1.0.0

# Здоровье приложения
HEALTHCHECK CMD curl --fail http://localhost:9000 || exit 1

# Запуск сервера
CMD ["npx", "-y", "http-server", "-p", "9000", "/app/build"]
