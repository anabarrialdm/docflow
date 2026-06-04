# Origen del Problema

## Contexto

Este documento describe el problema real que dio origen a DocFlow, identificado durante una pasantía en análisis e ingeniería de datos.

## El dolor observado

Durante la documentación del Proyecto Datahub en Endavant Group, se identificaron dos fricciones principales:

### 1. Dependencia mutua improductiva
- La persona que documenta **depende** de quienes conocen el proceso para obtener información
- Quienes conocen el proceso **dependen** de la persona que documenta para plasmar ese conocimiento
- Esto genera coordinación constante, reuniones largas y bloqueos cuando alguna de las partes no está disponible

### 2. Documentación que no escala
- Procesos operativos (como agregar una nueva fuente de datos) requieren capturar pasos, responsables, decisiones y excepciones — información difícil de extraer con preguntas genéricas
- Estructuras técnicas (como diccionarios de datos con 29 tablas y cientos de campos) son imposibles de documentar manualmente de forma sostenible

## Ejemplo concreto

El documento de Datahub contiene:
- 9 procesos operativos con pasos y responsables
- 29 tablas con diccionario de datos completo (nombre, tipo, descripción por campo)
- Roles técnicos y operativos
- Requerimientos de infraestructura

Todo esto fue documentado manualmente mediante reuniones y explicaciones directas — un proceso que consumió tiempo significativo de personas técnicas con alta demanda.

## Hipótesis

Si la herramienta de documentación:
1. Permite a quien sabe describir brevemente el proceso con sus propias palabras
2. Hace preguntas de seguimiento específicas basadas en lo que se describió
3. Genera automáticamente un documento estructurado

...entonces se reduce drásticamente el tiempo de documentación y la dependencia entre personas.
