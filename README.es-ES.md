<p align="center">
  <img src="./assets/banner.jpeg" width="100%" alt="Context Sanitary Banner">
</p>

# Context Sanitary Skill

> Recolector de basura de contexto y sincronizador de memoria persistente para Agentes de IA.

[Português (pt-BR)](./README.pt-BR.md) | [English (en-US)](./README.md) | [Español (es-ES)](./README.es-ES.md)

---

## ❓ ¿Por qué usar Context Sanitary?

Durante conversaciones largas o sesiones intensivas de desarrollo con Agentes de IA (como **Antigravity**, **OpenCode** y **Hermes**), la ventana de contexto se degrada debido a:
1. **Dumps Extensos de Terminal y Stack Traces Muertos:** Logs repetitivos que consumen miles de tokens sin aportar valor.
2. **Alucinaciones por Exceso de Ruido:** El agente se confunde al analizar comandos intermedios antiguos de navegación.
3. **Pérdida de Lecciones Aprendidas entre Sesiones:** Errores corregidos vuelven a ocurrir si el agente no guarda el aprendizaje en memoria persistente.

**Context Sanitary** resuelve esto en **3 etapas automáticas**:
- **Poda Heurística Algorítmica (Zero Tokens):** Limpia ruido operacional y trunca logs largos manteniendo la esencia.
- **Offload y Consulta a Memoria Persistente:** Guarda lecciones aprendidas (`[Error ➔ Causa ➔ Solución]`) en tu **Obsidian**, **Holographic Memory**, **ai-memory**, **Honcho**, **Mem0** o **Supermemory**.
- **Checkpoint Estricto:** Inyecta un marcador estricto en el historial, forzando al agente a ignorar mensajes pasados y enfocarse solo en el estado consolidado.

---

## 💡 About The Project

**Context Sanitary** es una Skill diseñada para gestionar y optimizar la ventana de contexto de agentes de IA en workflows de largo plazo. Garantiza máximo rendimiento, menor costo de tokens y cero pérdida de memoria.

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

## 🚀 Instalación y Inicio Rápido

### Opción A: Instalación vía `pip` (Python Standard)
```bash
pip install git+https://github.com/wxypereira/context-sanitary.git
```

### Opción B: Instalación vía `pipx` (Recomendado CLI)
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git
```

### Opción C: Instalación vía `npm` / `npx` (Node.js)
```bash
# Instalación global vía npm
npm install -g context-sanitary

# Ejecución directa vía npx
npx context-sanitary --test-checkpoint
```

### Opción D: Instalación como Skill de Agente (`.gemini` / `Antigravity` / `Claude`)
```bash
git clone https://github.com/wxypereira/context-sanitary.git
cp -r context-sanitary ~/.gemini/config/skills/
```

## 🎮 Uso Básico

Ejecuta en tu terminal o dentro de un chat con el agente:

- `context-sanitary` (o `/context-sanitary`) — Ejecuta la poda algorítmica e inyecta el Checkpoint.
- `context-sanitary --memory obsidian` — Especifica el proveedor de memoria.
- `context-sanitary --auto 80%` — Configura la ejecución automática al 80% de capacidad.
- `context-sanitary --no-auto` — Desactiva el activador automático.

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!
1. Haz un Fork del Proyecto
2. Crea tu rama de función (`git checkout -b feature/NuevaMemoria`)
3. Haz Commit de tus cambios (`git commit -m 'Add: Soporte a nueva memoria'`)
4. Haz Push a la rama (`git push origin feature/NuevaMemoria`)
5. Abre un Pull Request

## 👥 Créditos y Agradecimientos

Desarrollado en colaboración de Pair Programming entre:
- **Antigravity** (Google DeepMind Team)
- **OpenCode** (Muse Spark 1.3 Zen Agent)

## 📝 Licencia

Este proyecto está bajo la Licencia [MIT](./LICENSE).
