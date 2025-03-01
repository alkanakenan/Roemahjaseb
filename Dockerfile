FROM python:3.9

# Clone repo baru
RUN git clone -b main https://github.com/alkanakenan/Roemahjaseb /home/Roemahjaseb/ \
    && chmod 777 /home/Roemahjaseb \
    && mkdir /home/Roemahjaseb/bin/

# Salin file konfigurasi
COPY ./sample_config.env ./config.env* /home/Roemahjaseb/

# Set working directory
WORKDIR /home/Roemahjaseb/

# Update pip dan install dependensi
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install av
RUN pip install av --no-binary av
RUN pip install -r requirements.txt

# Jalankan perintah start
CMD ["bash", "start"]
