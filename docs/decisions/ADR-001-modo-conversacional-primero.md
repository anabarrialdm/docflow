# ADR-001: Comenzar con el modo conversacional

**Fecha:** 2026-06-04  
**Estado:** Aceptado

## Contexto

DocFlow tiene dos modos posibles:
1. **Conversacional** — para procesos operativos documentados a través de preguntas de seguimiento
2. **Técnico** — para estructuras de datos extraídas automáticamente desde bases de datos

Ambos resuelven partes del problema, pero requieren distintos niveles de complejidad técnica.

## Decisión

Comenzar con el modo conversacional.

## Razones

- Es más alcanzable como primer prototipo funcional
- No requiere conexión a bases de datos ni manejo de credenciales
- Permite validar la idea central (preguntas de seguimiento inteligentes) antes de añadir complejidad
- Genera valor visible más rápido

## Consecuencias

- El modo técnico queda documentado como Fase 2
- El prototipo inicial puede construirse con Python y una interfaz simple
- Se puede demostrar y obtener feedback real antes de invertir más tiempo

## Alternativa descartada

Construir ambos modos en paralelo — descartado porque aumenta la complejidad sin validar primero la hipótesis central.
