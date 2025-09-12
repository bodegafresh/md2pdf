# md2pdf


Herramienta para convertir Markdown → PDF con calidad editorial, branding, diagramas, gráficos e IA (pulido y resumen).


## Rápido inicio


### Opción A: Docker
```bash
docker build -t md2pdf .
docker run --rm -p 8080:8080 -v $PWD:/work -w /work md2pdf \
md2pdf generate --in examples/cotizacion_kolff.md --theme kolff --out-dir output
```


### Opción B: Local (Python 3.12)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
md2pdf generate --in examples/cotizacion_kolff.md --theme kolff --out-dir output
uvicorn md2pdf.interfaces.api:app --reload --port 8080
```


## CLI
```bash
md2pdf generate --in <ruta.md> [--theme default|kolff] [--ai-polish on] [--include-summary on]
md2pdf preview --in <ruta.md> [--theme default|kolff]
md2pdf organize --scan docs/ --by cliente,fecha
```


## API
- `POST /render` → PDF (devuelve binario)
- `POST /preview` → HTML
- `GET /themes` → lista de temas


## Tests
```bash
pytest --maxfail=1 --disable-warnings -q --cov=md2pdf --cov-report=term-missing