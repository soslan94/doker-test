# ./jenkins/Dockerfile
FROM jenkins/jenkins:lts

# Нужен docker CLI внутри контейнера Jenkins
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl gnupg lsb-release \
  && curl -fsSL https://download.docker.com/linux/debian/gpg \
       | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
       https://download.docker.com/linux/debian $(. /etc/os-release; echo $VERSION_CODENAME) stable" \
       > /etc/apt/sources.list.d/docker.list \
  && apt-get update && apt-get install -y --no-install-recommends docker-ce-cli \
  && rm -rf /var/lib/apt/lists/*

# Минимум плагинов: Pipeline и Docker Pipeline (+ git)
RUN jenkins-plugin-cli --plugins "workflow-aggregator docker-workflow git"

# Можно вернуться к пользователю jenkins, но мы запустим сервис как root в compose.
USER jenkins