FROM httpd:2.4
COPY ./* /usr/local/apache2/htdocs/transition/
WORKDIR /usr/local/apache2/htdocs
