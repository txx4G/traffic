## На Windows

### Установка GDAL

1. Выполнить `pip install -r requirements.windows.txt`
3. В `.env` добавить:
    - `GDAL_LIBRARY_PATH=../.venv/Lib/site-packages/osgeo/gdal304.dll`
    - `GEOS_LIBRARY_PATH=../.venv/Lib/site-packages/osgeo/geos_c.dll`

### Установка Spatialite

1. Извлечь все `*.dll` из `mod_spatialite-5.1.0-win-amd64.7z` в `.venv/Scripts`
3. В `.env` добавить: `SPATIALITE_LIBRARY_PATH=mod_spatialite`
