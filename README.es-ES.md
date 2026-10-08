<p align="center">
  <img src="./assets/banner.jpeg" width="100%" alt="Context Sanitary Banner">
</p>

[English](README.md) | [Español](README.es-ES.md) | [Português](README.pt-BR.md)

---

# Context Sanitary Skill

> Recolector de basura de contexto y sincronizador de memoria persistente para Agentes de IA.

---

## ❓ ¿Por qué usar Context Sanitary?

Durante conversaciones largas o sesiones intensivas de desarrollo con Agentes de IA (como **Antigravity**, **OpenCode** y **Hermes**), la ventana de contexto se degrada debido a:

1. **Dumps extensos de terminal y stack traces obsoletos:** logs repetitivos que consumen miles de tokens sin aportar valor.
2. **Alucinaciones por exceso de ruido:** el agente se confunde al analizar comandos intermedios antiguos de navegación.
3. **Pérdida de lecciones aprendidas entre sesiones:** errores corregidos vuelven a ocurrir si el agente no guarda el aprendizaje en memoria persistente.

**Context Sanitary** resuelve esto en **3 etapas automáticas**:

- **Poda heurística algorítmica (zero tokens):** limpia ruido operacional y trunca logs largos manteniendo la esencia.
- **Offload y consulta a memoria persistente:** guarda lecciones aprendidas (`[Error ➔ Causa ➔ Solución]`) en tu **Obsidian**, **Holographic Memory**, **ai-memory**, **Honcho**, **Mem0** o **Supermemory**.
- **Checkpoint estricto:** inyecta un marcador estricto en el historial, forzando al agente a ignorar mensajes pasados y enfocarse solo en el estado consolidado.

---

## 💡 Sobre el Proyecto

**Context Sanitary** es una Skill diseñada para gestionar y optimizar la ventana de contexto de agentes de IA en flujos de trabajo de largo plazo. Garantiza máximo rendimiento, menor costo de tokens y cero pérdida de memoria.

## 🧠 Soporte de Memoria Persistente

| Proveedor de Memoria | Tipo / Local | Estado de Integración | Descripción |
| --- | --- | --- | --- |
| **`ai-memory`** (Akita) | Local (Wiki Markdown + SQLite) | 🟢 Nativo | Almacena en `~/.ai-memory/wiki/` para rastreo en Git. |
| **`Obsidian`** | Local (Markdown Vault) | 🟢 Nativo | Anexa a la nota `Knowledge/AI_Lessons.md` con etiquetas frontmatter. |
| **`Holographic Memory`** | Local (Vector Asociativo / Hermes) | 🟢 Nativo | Registra en `~/.hermes/holographic_memory.json` con búsqueda FTS5. |
| **`Honcho`** | Cloud / Session Reasoning | 🟡 Stub / Experimental | Sincroniza estado a nivel de Workspace/Session (`HONCHO_API_KEY`). |
| **`Mem0`** | Cloud / Vector Store | 🟡 Stub / Experimental | Envía tríadas de solución mediante REST API (`MEM0_API_KEY`). |
| **`Supermemory`** | Cloud / Long-term Memory | 🟡 Stub / Experimental | Almacena contextos para consultas vectoriales a largo plazo (`SUPERMEMORY_API_KEY`). |

## 🛠️ Tech Stack

[![My Skills](https://skillicons.dev/icons?i=python,nodejs,bash,git)](https://skillicons.dev)

- **Lenguaje:** Python 3 (Script Helper) & Node.js Wrapper
- **Gestores de Paquetes:** `pip` / `pipx` & `npm` / `npx`

## 🧪 Resultado de las Pruebas

El script auxiliar cuenta con una suite autónoma de pruebas:

```bash
$ python3 scripts/sanitary_purge.py --test-memory

--- Prueba de Offload ---
{
  "ai-memory": "Guardado en ~/.ai-memory/wiki/lesson_20261007_165206_856622.md",
  "obsidian": "Anexado a la nota Obsidian ~/ObsidianVault/Knowledge/AI_Lessons.md",
  "holographic": "Guardado en memoria asociativa Holographic",
  "honcho": "[Stub/Experimental] HONCHO_API_KEY no configurada (offload pendiente)",
  "mem0": "[Stub/Experimental] MEM0_API_KEY no configurada",
  "supermemory": "[Stub/Experimental] SUPERMEMORY_API_KEY no configurada"
}

--- Prueba de Consulta ---
[
  "**Solución:** Usar sanitary_purge.py para truncar logs",
  "[Obsidian] Usar sanitary_purge.py para truncar logs",
  "[Holographic] Solución: Usar sanitary_purge.py para truncar logs"
]
```

---

## 🚀 Instalación e Inicio Rápido

### Opción A: Instalación vía `pip` (Python Standard)

**1. Descarga / Instalación**
```bash
pip install git+https://github.com/wxypereira/context-sanitary.git
# O instalación local editable
pip install -e .
```

**2. Prueba Práctica de la SKILL**
```bash
context-sanitary --test-checkpoint
```

**3. Validación del Resultado**
```bash
context-sanitary --test-memory --memory all
# Esperado: todos los 6 proveedores listados (3 nativos OK, 3 stubs pendientes de claves)
```

**4. Eliminación / Limpieza del Paquete**
```bash
pip uninstall context-sanitary
# Elimina los entry points CLI (context-sanitary, sanitary-purge)
```

---

### Opción B: Instalación vía `pipx` (Recomendado para CLI Aislado)

**1. Descarga / Instalación**
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git
```

**2. Prueba Práctica de la SKILL**
```bash
context-sanitary --test-checkpoint
```

**3. Validación del Resultado**
```bash
context-sanitary --test-memory --memory all
```

**4. Eliminación / Limpieza del Paquete**
```bash
pipx uninstall context-sanitary
# Elimina completamente el entorno aislado y los binarios CLI
```

---

### Opción C: Instalación vía `npm` / `npx` (Node.js)

**1. Descarga / Instalación**
```bash
# Instalación global vía npm
npm install -g context-sanitary

# O ejecución directa sin instalación vía npx
npx context-sanitary --test-checkpoint
```

**2. Prueba Práctica de la SKILL**
```bash
npx context-sanitary --test-checkpoint
```

**3. Validación del Resultado**
```bash
npx context-sanitary --test-memory --memory all
```

**4. Eliminación / Limpieza del Paquete**
```bash
npm uninstall -g context-sanitary
# Elimina el paquete global y los enlaces de los binarios
```

---

### Opción D: Instalación como Skill de Agente (`.gemini` / `Antigravity` / `Claude`)

**1. Descarga / Instalación**
```bash
git clone https://github.com/wxypereira/context-sanitary.git
cp -r context-sanitary ~/.gemini/config/skills/
```

**2. Prueba Práctica de la SKILL**
```bash
# Dentro de un chat con el agente:
/context-sanitary --test-checkpoint
```

**3. Validación del Resultado**
```bash
/context-sanitary --test-memory --memory all
```

**4. Eliminación / Limpieza de la SKILL**
```bash
rm -rf ~/.gemini/config/skills/context-sanitary
# Elimina el directorio de la skill de la configuración del agente
```

---

### Configurar Variables de Entorno (Opcional):

Copie `.env.example` a `.env` y configure las rutas o claves de API si usa Obsidian, Honcho, Mem0 o Supermemory.
```bash
cp .env.example .env
```

---

## 🎮 Uso Básico

Ejecute en su terminal o dentro de un chat con el agente:

- `context-sanitary` (o `/context-sanitary`) — Ejecuta la poda algorítmica, realiza offload a la memoria e inyecta el Checkpoint.
- `context-sanitary --memory obsidian` — Especifica el proveedor de memoria.
- `context-sanitary --auto 80%` — Configura la ejecución automática al 80% de capacidad.
- `context-sanitary --no-auto` — Desactiva el gatillo automático por porcentaje.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!
1. Haga un Fork del Proyecto
2. Cree su rama de función (`git checkout -b feature/NuevaMemoria`)
3. Haga Commit de sus cambios (`git commit -m 'Add: Soporte a nueva memoria'`)
4. Haga Push a la rama (`git push origin feature/NuevaMemoria`)
5. Abra un Pull Request

---

## 👥 Créditos y Agradecimientos

Desarrollado en colaboración de Pair Programming entre:
- **Antigravity** (Google DeepMind Team)
- **OpenCode** (Muse Spark 1.3 Zen Agent)
- **Modelo de IA:** **Gemini 2.5 Pro** (Google DeepMind)

---

## 📝 Licencia

Este proyecto está bajo la Licencia [MIT](./LICENSE).