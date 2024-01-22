import os
from pathlib import Path

ruta_del_archivo = "App6/Archivos/MiArchivo.txt"

archivo = os.path.basename(ruta_del_archivo)
ruta = os.path.realpath(ruta_del_archivo)

print(f"archivo -> {archivo} | directorio -> {ruta}")


ruta_del_archivo_con_path = Path(ruta_del_archivo)
print(ruta_del_archivo_con_path.read_text())
print(ruta_del_archivo_con_path.name)
print(ruta_del_archivo_con_path.suffix)
print(ruta_del_archivo_con_path.stem)

print(Path.home())