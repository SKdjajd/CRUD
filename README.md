# 🗂️ Sistema CRUD de Gestión de Usuarios

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=yellow)

## 📋 Descripción
Sistema CLI completo **CRUD** para gestión de usuarios con:
- ✅ **Validación RUT chileno** (algoritmo oficial DV)
- ✅ **Validación email** (regex)
- ✅ **Persistencia** en `bdd.txt` (CSV plano)
- ✅ **Menú interactivo** (1-5 opciones)

## 🚀 Funcionalidades

| Operación | Descripción |
|-----------|-------------|
| **Crear** | Ingresar usuario nuevo (RUT único) |
| **Leer** | Listar todos los usuarios |
| **Actualizar** | Eliminar + recrear |
| **Eliminar** | Buscar por RUT y borrar |

## 📦 Instalación

```bash
git clone <URL_REPO>
cd CRUD
pip install -r requirements.txt  # Sin dependencias externas
```

## 🎮 Uso

```bash
python Prot_1_cli.py
# o
python BDD.py.py
```

**Menú ejemplo:**
```
[1] Ingresar datos    [2] Actualizar datos
[3] Eliminar datos    [4] Visualizar datos
[5] Salir
```

## 📁 Estructura de Archivos

| Archivo | Función |
|---------|---------|
| `BDD.py.py` | Lógica CRUD + validaciones |
| `Prot_1_cli.py` | Interfaz de usuario |
| `requirements.txt` | Dependencias (vacío) |
| `bdd.txt` | Base de datos (generado) |

## 💾 Datos Almacenados
```
RUT, Nombre, Edad, Correo
12.345.678-9, Juan Pérez, 25, juan@email.com
```

## ⚠️ Notas Importantes
- **Backup**: Respalda `bdd.txt` antes de eliminar
- **Seguridad**: Validaciones básicas, no para producción
- **Python**: 3.6+ (stdlib only)

## 📄 Licencia
MIT - Úsalo libremente con atribución.

---

⭐ **¡Star si te sirve!**
