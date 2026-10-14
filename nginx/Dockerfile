FROM nginx:latest
COPY default.conf /etc/nginx/conf.d/default.conf
COPY selfsigned.crt /etc/nginx/selfsigned.crt
COPY selfsigned.key /etc/nginx/selfsigned.key
COPY .htpasswd /etc/nginx/.htpasswd
EXPOSE 80 443
