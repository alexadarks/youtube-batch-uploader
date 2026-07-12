[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)]()

# 🎬 YouTube Batch Uploader

**Deja de subir videos uno por uno. Sube 100+ videos con metadatos, programación y reintentos automáticos.**

Automatiza tus subidas a YouTube con una hermosa vista previa en Excel, programación inteligente e intervención manual cero. Perfecto para podcasters, creadores de contenido, gestores de librerías de stock footage y cualquiera con un gran número de videos.

---

## ✨ ¿Qué hace?

| Característica | Beneficio |
|---------|---------|
| 📋 **Vista Previa en Excel** | Excel auto-generado con miniaturas + metadatos editables |
| ⏰ **Programación Inteligente** | Sube videos automáticamente cada N minutos |
| 🔀 **Orden Flexible** | Secuencial o aleatorio (se ve orgánico, no "batch-dump") |
| 🛡️ **Reintentos Automáticos** | Los videos fallidos se resuben hasta 3 veces automáticamente |
| ✅ **Seguimiento de Progreso** | Estado en tiempo real en cola JSON |
| 🚀 **Sin Código Requerido** | Comandos CLI + Tareas Programadas de Claude |

---

## 🎯 Perfecto Para

- 🎙️ **Podcasters** — Sube 100+ episodios con metadatos consistentes
- 📸 **Creadores de Stock Footage** — Sube en lotes con descripciones buscables
- 🎬 **Creadores de Reels** — Convierte reels de TikTok/Instagram → YouTube automáticamente
- 📺 **Streamers** — Auto-sube streams grabados con timestamps
- 🎓 **Creadores de Cursos** — Publica videos de clases en masa

---

## 🚀 Inicio Rápido (5 Minutos)

### 1️⃣ Instalar

```bash
git clone https://github.com/alexadarks/youtube-batch-uploader.git
cd youtube-batch-uploader
pip install -r requirements.txt
```

### 2️⃣ Obtener ID de Conexión

1. Ve a **[YouTubeStudioMCP.com](https://YouTubeStudioMCP.com)**
2. Inicia sesión → Autoriza → Copia ID de Conexión
3. Guárdalo (lo necesitarás pronto)

### 3️⃣ Configurar

```bash
cp config.example.yaml config.yaml
# Edita con tu ID de Conexión, ruta de carpeta de videos, preferencias
```

### 4️⃣ Generar Vista Previa

```bash
python3 scripts/build_preview_spreadsheet.py \
  "/ruta/a/videos" \
  "./videos_preview.xlsx"
```

Abre Excel → Llena **Título** para cada video → Guarda

### 5️⃣ Crear Cola

```bash
python3 scripts/build_upload_queue.py \
  "./videos_preview.xlsx" \
  "/ruta/a/videos" \
  "TU_ID_DE_CONEXION" \
  "./upload_queue.json"
```

### 6️⃣ Programar Subidas

Pídele a Claude:
> "Configura una tarea programada que suba videos de mi cola cada 30 minutos."

✅ **¡Listo!** Los videos se suben automáticamente.

---

## 📚 Documentación

**[📖 Comienza aquí: Índice Completo de Documentación](INDEX.md)**

| Documento | Tiempo | Para |
|----------|--------|------|
| [QUICKSTART.md](QUICKSTART.md) | 5 min | Personas apuradas |
| [SETUP.md](SETUP.md) | 15 min | Setup por primera vez |
| [examples/WORKFLOW.md](examples/WORKFLOW.md) | 25 min | Guía completa + solución de problemas |

---

## 🎯 ¿Por Qué Usar Esto?

| Sin Esto | Con Esto |
|----------|----------|
| ⏱️ Subir 100 videos = 5+ horas de trabajo manual | ⚡ Mismo = 5 min setup |
| 😴 Click, espera, repite, click, espera, repite | 🤖 Configura y olvídate |
| 📝 Metadatos dispersos en notas | 📊 Todo en un archivo Excel |
| ❌ ¿Falla subida? Comienza de nuevo manual | ✅ Reintentos automáticos hasta 3x |
| 🎲 Orden de subida = aleatorio | 🎯 Controla el orden exacto |

**Ejemplo real:** 50 Reels de Instagram → YouTube

```
0:00   ✅ Videos 1-3 subidos
0:30   ✅ Videos 4-6 subidos  
1:00   ✅ Videos 7-9 subidos
...
~4:30  ✅ Los 50 subidos
5:00   🎉 Listo, tarea se detiene automáticamente
```

---

## 🔧 Configuración

Copia y personaliza:

```bash
cp config.example.yaml config.yaml
```

```yaml
youtube:
  connection_id: "abc123xyz789"  # De YouTubeStudioMCP.com
  channel_name: "Mi Canal"
  privacy_status: "public"  # public, unlisted, private

upload:
  batch_size: 3              # 3 videos por lote
  interval_minutes: 30       # Cada 30 minutos
  order: "shuffle"           # Aleatorio = orgánico, no batch-dump
  
paths:
  video_directory: "/Users/tu/Videos/mis-reels"
  preview_spreadsheet: "./videos_preview.xlsx"
  upload_queue: "./upload_queue.json"
```

---

## 📊 Vista Previa del Excel

Tu archivo Excel se ve así:

| # | Vista Previa | Nombre de Archivo | Fecha | Título | Descripción |
|---|---------|----------|------|-------|-------------|
| 1 | 🖼️ | video1.mp4 | 2024-01-15 | **TÚ LLENARÁS ESTO** | **TÚ LLENARÁS ESTO** |
| 2 | 🖼️ | video2.mp4 | 2024-01-16 | **TÚ LLENARÁS ESTO** | **TÚ LLENARÁS ESTO** |
| 3 | 🖼️ | video3.mp4 | 2024-01-17 | **TÚ LLENARÁS ESTO** | **TÚ LLENARÁS ESTO** |

- 🖼️ **Vista Previa** = Miniatura auto-generada
- ✏️ **Título & Descripción** = Tú editas estas
- Fechas auto-extraídas del nombre de archivo

---

## 🚨 Problemas Comunes & Soluciones

### ¿Sin miniaturas?
```bash
rm -rf .preview_thumbs_cache/
python3 scripts/build_preview_spreadsheet.py ...
```

### ¿"ID de Conexión inválido"?
1. Ve a https://YouTubeStudioMCP.com
2. Verifica que tu ID de Conexión sea correcto
3. Pídele a Claude: "Lista mis canales de YouTube"

### ¿Videos no se suben?
1. Comprueba conexión a internet
2. Verifica que archivos de video sean válidos
3. Revisa `upload_queue.json` para errores
4. Asegúrate de que MCP de Claude está conectado

**[Solución completa de problemas →](SETUP.md)**

---

## 🎬 Opciones Avanzadas

```bash
# Subir más lentamente (mejor para canales pequeños)
--batch-size 1 --interval 60

# Subir más rápido (para canales establecidos)
--batch-size 5 --interval 15

# Orden secuencial (estilo playlist)
--order sequential

# Aleatorio reproducible (mismo orden cada vez)
--order shuffle --seed 42
```

---

## 🤝 Contribuir

¿Ideas? ¿Bugs? ¿Quieres ayudar?

- [CONTRIBUTING.md](CONTRIBUTING.md) — Cómo contribuir
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) — Descripción del código
- **Planeado:** Soporte Linux/Windows, interfaz web, otras plataformas

---

## 📄 Licencia

**MIT** — Usa libremente, comercialmente o personalmente. Ver [LICENSE](LICENSE).

---

## 🌍 Idiomas

- 🇬🇧 [English](README.md)
- 🇪🇸 Español (este archivo)

---

## 🚀 Próximos Pasos

1. **[Inicio Rápido (5 min) →](QUICKSTART.md)**
2. **[Setup Completo (15 min) →](SETUP.md)**  
3. **[Flujo Completo (25 min) →](examples/WORKFLOW.md)**
4. **[Repo GitHub →](https://github.com/alexadarks/youtube-batch-uploader)**

---

## 💡 Consejos para Creadores

### Organiza tus videos
```
video_2024-01-15_tips.mp4       ← Fecha auto-extraída
contenido_2024-01-16_receta.mp4 ← Fecha auto-extraída
episodio_final.mp4              ← Sin fecha
```

### Sube en ondas
Divide 200 videos en 4 lotes de 50, sube semanalmente → se ve natural

### Ajusta la frecuencia
- Canal pequeño? 1 video por hora
- Canal establecido? 5 videos cada 15 min

### Reutiliza metadatos
El archivo Excel recuerda tus títulos anteriores → edita y reconstruye → mismos metadatos preservados

---

**Hecho con ❤️ para creadores de contenido.**

*Porque subir 100 videos manualmente no es un rasgo de personalidad.*
