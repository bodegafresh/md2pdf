FROM python:3.12-slim


# Dependencias del sistema para WeasyPrint y PlantUML/Mermaid
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential curl git ca-certificates \
libcairo2 libpango-1.0-0 libharfbuzz0b libffi8 libxml2 libxslt1.1 \
libjpeg62-turbo libpng16-16 libglib2.0-0 fonts-dejavu-core \
default-jre graphviz \
&& rm -rf /var/lib/apt/lists/*


# Mermaid CLI (mmdc)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
&& apt-get update && apt-get install -y nodejs \
&& npm i -g @mermaid-js/mermaid-cli@10.9.1 \
&& npm cache clean --force


WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY src/ /app/src/
COPY themes/ /app/themes/
COPY examples/ /app/examples/
ENV PYTHONPATH=/app/src


EXPOSE 8080
ENTRYPOINT ["python","-m","md2pdf.interfaces.cli"]