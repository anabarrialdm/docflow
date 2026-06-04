# DocFlow

Herramienta de documentación inteligente que adapta su estrategia según el tipo de proceso a documentar.

## El problema

Documentar procesos en equipos técnicos es lento y depende de personas con poco tiempo. Quien documenta debe esperar reuniones. Quien sabe del proceso debe interrumpir su trabajo. El resultado suele ser documentación incompleta o desactualizada.

## La solución

DocFlow reduce esa fricción con dos enfoques:

- **Modo conversacional** — para procesos operativos. La persona describe el proceso brevemente y DocFlow hace preguntas de seguimiento inteligentes y específicas basadas en lo que fue descrito. Al final genera un documento estructurado.
- **Modo técnico** *(fase futura)* — para estructuras de datos. Se conecta a la fuente, extrae lo que puede automáticamente, y solo pregunta lo que no puede inferir.

## Estado actual

🚧 En desarrollo — Fase 1: Modo conversacional

## Estructura del proyecto

```
docflow/
├── README.md
├── docs/
│   ├── decisions/       # Decisiones de diseño y arquitectura (ADRs)
│   └── process/         # Documentación del proceso de construcción
└── src/                 # Código fuente
```

## Origen

Este proyecto nació de una experiencia real documentando el Proyecto Datahub en Endavant Group, donde se identificó que la documentación manual genera dependencias innecesarias entre personas y consume tiempo valioso de quienes más saben.

## Autora

Desarrollado por una estudiante de tercer año de Ingeniería de Software como proyecto personal para resolver un problema real vivido en pasantía.
