# ADR-005: Soporte para adjuntar archivos e imágenes

**Fecha:** 2026-06-04  
**Estado:** Aceptado

## Contexto

Los usuarios que van a documentar un proceso frecuentemente ya tienen material de referencia — documentos parciales, capturas de pantalla, PDFs, archivos Word. Sin esta feature, DocFlow ignoraba ese contexto y hacía preguntas que el archivo ya respondía.

## Decisión

Agregar soporte para adjuntar archivos en la pantalla inicial. Los archivos se procesan antes de iniciar la conversación y se usan como contexto tanto para las preguntas de seguimiento como para la generación del documento final.

## Tipos de archivo soportados

| Tipo | Extensiones | Procesamiento |
|------|-------------|---------------|
| PDF | .pdf | Extracción de texto con PyMuPDF |
| Word | .docx | Extracción de texto con python-docx |
| Texto | .txt | Lectura directa |
| Imágenes | .jpg, .jpeg, .png, .webp | Envío como base64 a Claude vision |

## Razones

- Reduce preguntas redundantes sobre información que ya existe en documentos
- Permite que DocFlow analice capturas de pantalla de sistemas o procesos
- Claude soporta nativamente imágenes y texto en el mismo mensaje

## Consecuencias

- Los archivos se procesan una sola vez al inicio y se mantienen en sesión
- Las imágenes se envían como base64 — archivos muy grandes pueden aumentar el costo de tokens
- Formatos no soportados se notifican al usuario sin interrumpir el flujo

## Dependencias agregadas

- `pymupdf` — extracción de texto desde PDFs
- `python-docx` — extracción de texto desde archivos Word
- `pillow` — procesamiento de imágenes
