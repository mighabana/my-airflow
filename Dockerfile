FROM apache/airflow:2.10.5

USER root
# Additional APT package installation
# Reference: https://airflow.apache.org/docs/docker-stack/build.html#adding-new-apt-package
RUN apt-get update \
    && apt-get install -y \
    # Add your apt packages here
        vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd docker \ 
    && usermod -aG docker airflow \
    && newgrp docker

# Additional python package installation
# Reference: https://airflow.apache.org/docs/docker-stack/build.html#adding-a-new-pypi-package
USER airflow
RUN pip install --no-cache-dir 'apache-airflow>=2.10.5' 'apache-airflow[password]' 'apache-airflow[celery]'

COPY ./config/webserver_config.py /opt/airflow/webserver_config.py
