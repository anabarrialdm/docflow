# ADR-004: Usar Whisper local para transcripción de voz

**Fecha:** 2026-06-04  
**Estado:** Aceptado

## Contexto

DocFlow necesita permitir entrada por voz para que usuarios que no quieren escribir puedan responder las preguntas de seguimiento hablando. Se evaluaron dos opciones:

1. **Whisper API de OpenAI** — servicio en la nube, requiere pago y API key de OpenAI
2. **Whisper local** — modelo open source que corre en la computadora del usuario, completamente gratis

## Decisión

Usar Whisper local mediante la librería `openai-whisper`, sin llamadas a APIs externas.

## Razones

- Es completamente gratuito — no requiere cuenta ni créditos en OpenAI
- No envía audio a servidores externos — mejor privacidad para procesos internos de empresas
- El modelo `base` es suficientemente preciso para español en condiciones normales
- Requiere ffmpeg como dependencia del sistema, que se instala fácilmente

## Consecuencias

- La primera vez que se usa, Whisper descarga el modelo base (~140MB) automáticamente
- El modelo se carga en memoria al iniciar la sesión — hay un delay inicial de pocos segundos
- La transcripción corre en CPU — en computadoras lentas puede tardar algunos segundos
- No requiere conexión a internet para transcribir (solo para la primera descarga)

## Alternativas descartadas

- **Whisper API de OpenAI**: requiere pago, envía audio a servidores externos
- **Web Speech API del navegador**: no compatible con todos los navegadores, menos precisa en español

## Dependencias agregadas

- `openai-whisper` — modelo de transcripción
- `streamlit-audiorecorder` — grabación de audio en el navegador
- `ffmpeg` — procesamiento de audio (instalado a nivel sistema)
