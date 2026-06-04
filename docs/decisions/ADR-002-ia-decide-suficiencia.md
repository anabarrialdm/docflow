# ADR-002: La IA decide cuándo hay suficiente información

**Fecha:** 2026-06-04  
**Estado:** Aceptado

## Contexto

DocFlow necesita saber cuándo dejar de hacer preguntas y generar el documento final. Hay dos enfoques posibles:

1. **Número fijo de rondas** — DocFlow pregunta siempre N veces y luego genera
2. **La IA evalúa en cada ronda** — Claude decide si tiene suficiente información o necesita más

## Decisión

La IA evalúa en cada ronda si tiene suficiente información para generar un documento completo. Si la tiene, responde `LISTO`. Si no, genera más preguntas específicas.

## Razones

- Un número fijo de rondas no se adapta a la complejidad del proceso — un proceso simple no necesita 5 rondas, uno complejo puede necesitar más
- La IA puede evaluar la calidad y completitud de la información mejor que una regla rígida
- Es consistente con la propuesta central de DocFlow: hacer preguntas inteligentes, no genéricas

## Consecuencias

- El número de rondas es impredecible — puede ser 1 o puede ser 10
- Si la IA es demasiado permisiva, generará documentos incompletos
- Si la IA es demasiado estricta, el usuario puede sentir que la conversación no termina
- La calidad del criterio depende del prompt — si el prompt cambia, el comportamiento cambia

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|--------|------------|
| Loop infinito de preguntas | Agregar límite máximo de rondas como fallback |
| Documento generado con info insuficiente | Mejorar el prompt de evaluación |
| Usuario abandona por demasiadas preguntas | Dar opción de generar documento en cualquier momento |

## Mejoras futuras identificadas

- Agregar comando `/generar` para que el usuario fuerce la generación del documento cuando quiera
- Agregar límite máximo de rondas configurable
