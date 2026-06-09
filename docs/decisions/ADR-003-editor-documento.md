# ADR-003: Editor de documento en pantalla de resultado

**Fecha:** 2026-06-04  
**Estado:** Aceptado

## Contexto

DocFlow genera documentos automáticamente basándose en una conversación. Sin embargo, la IA puede cometer errores, omitir detalles o formatear algo de forma que no refleje exactamente lo que el usuario necesita. El usuario no tenía forma de corregir el documento sin salir de la herramienta.

## Decisión

Agregar un editor de texto directamente en la pantalla de resultado, junto con botones para guardar cambios y descargar el documento editado.

## Razones

- El documento generado por IA no siempre es perfecto — el usuario debe poder corregirlo
- Editar dentro de DocFlow es más fluido que descargar, abrir en otro editor, corregir y volver
- Es una mejora pequeña con alto impacto en la experiencia del usuario

## Consecuencias

- El usuario tiene control total sobre el documento final
- Los cambios se guardan en el archivo de output local
- La vista previa en Markdown permite verificar el formato antes de descargar

## Alternativas descartadas

- **Edición en un editor externo**: requiere salir de DocFlow, rompe el flujo
- **Regenerar el documento con instrucciones**: más complejo, agrega una ronda extra de interacción con la IA
