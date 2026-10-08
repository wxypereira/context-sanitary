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

## 📁 Jerarquía de Carpetas

```
context-sanitary/
├── bin/                    # Puntos de entrada del wrapper Node.js
│   └── context-sanitary.js
├── scripts/                # Scripts auxiliares en Python
│   └── sanitary_purge.py   # Lógica principal: poda, checkpoint, offload/consulta de memoria
├── references/             # Documentos de especificación
│   ├── pipeline.md         # Especificación del pipeline en 3 etapas
│   ├── checkpoint_spec.md  # Formato y reglas del Checkpoint
│   └── memory_integration.md  # Guía de integración con proveedores de memoria
├── tests/                  # Suite de pruebas (no incluida en el paquete distribuido)
│   ├── evals/
│   │   └── dataset.json    # Dataset de evaluación
│   └── validate_sanitization.py  # Script de validación automatizada
├── assets/                 # Assets estáticos (banner, logos)
├── SKILL.md                # Manifiesto de la skill para agentes de IA
├── .env.example            # Plantilla de variables de entorno (valores en blanco)
├── .gitignore
├── LICENSE
├── CHANGELOG.md
├── SECURITY.md
├── package.json            # Configuración del paquete npm
├── setup.py                # Configuración del paquete pip
├── README.md               # Documentación en inglés
├── README.pt-BR.md         # Documentación en portugués
└── README.es-ES.md         # Documentación en español
```

---

## 📦 Esquema del Payload de Salida Sanitizado

La skill genera un payload JSON estandarizado para sistemas de memoria persistente (Obsidian, Mem0, Supermemory, Honcho, etc.):

```json
{
  "sanitized_context": "Texto del contexto higienizado, sin ruidos ni datos sensibles.",
  "metadata": {
    "removed_items_count": 0,
    "has_pii_detected": false,
    "sanitization_level": "high|medium|low"
  },
  "persistent_facts": [
    "Hechos o preferencias atemporales extraídos para persistencia a largo plazo"
  ]
}
```

**Campos:**
- `sanitized_context` (string): El contexto podado, libre de ruido, listo para almacenamiento.
- `metadata` (objeto): Información diagnóstica — cuenta de elementos removidos, bandera de detección de PII, nivel de agresividad de la sanitización.
- `persistent_facts` (array de strings): Hechos/preferencias perennes extraídos para memoria a largo plazo.

---

## 🚀 Instalación e Inicio Rápido

### Opción A: Instalación vía `pip` (Python Standard)

**1. Instalar**
```bash
pip install git+https://github.com/wxypereira/context-sanitary.git
# O instalación local editable (clona repo completo incluyendo tests)
pip install -e .
```

**Para uso en producción sin archivos de prueba:**
```bash
# Usando pip con subdirectory
pip install git+https://github.com/wxypereira/context-sanitary.git#subdirectory=.
```

**2. Probar**
```bash
context-sanitary --test-checkpoint
```

**3. Desinstalar**
```bash
pip uninstall context-sanitary
```

---

### Opción B: Instalación vía `pipx` (Recomendado para CLI Aislado)

**1. Instalar**
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git
```

**Para uso en producción sin archivos de prueba:**
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git#subdirectory=.
```

**2. Probar**
```bash
context-sanitary --test-checkpoint
```

**3. Desinstalar**
```bash
pipx uninstall context-sanitary
```

---

### Opción C: Instalación vía `npm` / `npx` (Node.js)

**1. Instalar**
```bash
# Instalación global vía npm (desde npm registry, excluye archivos de prueba)
npm install -g context-sanitary

# O ejecución directa sin instalación vía npx (desde npm registry, excluye archivos de prueba)
npx context-sanitary --test-checkpoint
```

**Nota:** El paquete npm publica solo los archivos de distribución (excluye `tests/`, `scripts/__pycache__/`, etc.).

**2. Probar**
```bash
npx context-sanitary --test-checkpoint
```

**3. Desinstalar**
```bash
npm uninstall -g context-sanitary
```

---

### Opción D: Instalación como Skill de Agente (`.gemini` / `Antigravity` / `Claude`)

**1. Instalar (repo completo incluyendo tests):**
```bash
git clone https://github.com/wxypereira/context-sanitary.git
cp -r context-sanitary ~/.gemini/config/skills/
```

**2. Instalar (producción — excluye archivos de prueba):**
```bash
# Descarga solo la carpeta de la skill sin tests/evals
git clone --depth=1 --filter=blob:none --sparse https://github.com/wxypereira/context-sanitary.git
cd context-sanitary
git sparse-checkout set --no-cone SKILL.md references scripts/sanitary_purge.py bin assets
cp -r context-sanitary ~/.gemini/config/skills/
```

**3. Probar**
```bash
# Dentro de un chat con el agente:
/context-sanitary --test-checkpoint
```

**4. Desinstalar**
```bash
rm -rf ~/.gemini/config/skills/context-sanitary
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

Desarrollado con el soporte de **Gemini 3.6 Flash**, alternando entre **Muse Spark 1.3** y **Nemotron 3 Super**.

---

## 📝 Licencia

Este proyecto está bajo la Licencia [MIT](./LICENSE).