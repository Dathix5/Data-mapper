# Data Mapper

By Daan Thielemans

**A Python application to link your files to specific locations on a map**

Originally made for *Studiebureau Thielemans*

## Required python packages

- folium `pip install folium`
- PyQt5 `pip install PyQt5`
- pyinstaller `pip install pyinstaller` -> only for executable

## Generating new executable for Windows

- `pyinstaller --onefile --noconsole --icon=datamapper.ico --name=DataMapper --hidden-import=geopy datamapper-ui.py`
