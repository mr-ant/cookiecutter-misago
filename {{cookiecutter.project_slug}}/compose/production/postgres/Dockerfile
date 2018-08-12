
{% if cookiecutter.chinese_user == "y" -%}
FROM chenxinaz/zhparser
{%- else %}
FROM postgres:{{ cookiecutter.postgresql_version }}
{%- endif %}

COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
