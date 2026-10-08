<p align="center">
  <img src="./assets/banner.jpeg" width="100%" alt="Context Sanitary Banner">
</p>

[English](README.md) | [Español](README.es-ES.md) | [Português](README.pt-BR.md)

---

# Context Sanitary Skill

> Context Garbage Collector and Persistent Memory Synchronizer for AI Agents.

## ❓ Why Use Context Sanitary?

During long conversations or intensive development sessions with AI Agents (such as **Antigravity**, **OpenCode**, and **Hermes**), the context window degrades due to:

1. **Extensive Terminal Dumps & Dead Stack Traces:** Repetitive logs consuming thousands of tokens without adding value to the solution.
2. **Noise-Induced Hallucinations:** The agent gets confused analyzing old intermediate navigation commands.
3. **Loss of Learned Lessons Across Sessions:** Previously fixed errors recur if the agent fails to save insights to persistent memory.

**Context Sanitary** resolves this in **3 automated stages**:

- **Algorithmic Heuristic Pruning (Zero Tokens):** Cleans operational noise and truncates long logs while preserving the essence.
- **Persistent Memory Offload & Query:** Saves learned lessons (`[Error ➔ Cause ➔ Solution]`) to **Obsidian**, **Holographic Memory**, **ai-memory**, **Honcho**, **Mem0**, or **Supermemory**.
- **Strict Checkpoint:** Injects a strict divider into history, forcing the agent to ignore past messages and focus solely on the consolidated state.

---

## 💡 About The Project

**Context Sanitary** is a Skill designed to manage and optimize the context window of AI agents in long-running workflows. It ensures maximum performance, lower token costs, and zero memory loss.

## 🧠 Persistent Memory Support

| Memory Provider | Type / Location | Integration Status | Description |
| --- | --- | --- | --- |
| **`ai-memory`** (Akita) | Local (Wiki Markdown + SQLite) | 🟢 Native | Stores in `~/.ai-memory/wiki/` for Git tracking. |
| **`Obsidian`** | Local (Markdown Vault) | 🟢 Native | Appends to `Knowledge/AI_Lessons.md` with frontmatter tags. |
| **`Holographic Memory`** | Local (Associative Vector / Hermes) | 🟢 Native | Records in `~/.hermes/holographic_memory.json` with FTS5 search. |
| **`Honcho`** | Cloud / Session Reasoning | 🟡 Stub / Experimental | Syncs state at Workspace/Session level (`HONCHO_API_KEY`). |
| **`Mem0`** | Cloud / Vector Store | 🟡 Stub / Experimental | Sends solution triples via REST API (`MEM0_API_KEY`). |
| **`Supermemory`** | Cloud / Long-term Memory | 🟡 Stub / Experimental | Stores contexts for long-term vector queries (`SUPERMEMORY_API_KEY`). |

## 🛠️ Tech Stack

[![My Skills](https://skillicons.dev/icons?i=python,nodejs,bash,git)](https://skillicons.dev)

- **Language:** Python 3 (Helper Script) & Node.js Wrapper
- **Package Managers:** `pip` / `pipx` & `npm` / `npx`

## 🧪 Test Results

The helper script includes an autonomous test suite. Below is the validation run output:

```bash
$ python3 scripts/sanitary_purge.py --test-memory

--- Offload Test ---
{
  "ai-memory": "Saved to ~/.ai-memory/wiki/lesson_20261007_165206_856622.md",
  "obsidian": "Appended to Obsidian note ~/ObsidianVault/Knowledge/AI_Lessons.md",
  "holographic": "Recorded in associative Holographic Memory",
  "honcho": "[Stub/Experimental] HONCHO_API_KEY not configured (offload pending)",
  "mem0": "[Stub/Experimental] MEM0_API_KEY not configured",
  "supermemory": "[Stub/Experimental] SUPERMEMORY_API_KEY not configured"
}

--- Query Test ---
[
  "**Solution:** Use sanitary_purge.py to truncate logs",
  "[Obsidian] Use sanitary_purge.py to truncate logs",
  "[Holographic] Solution: Use sanitary_purge.py to truncate logs"
]
```

---

## 📁 Folder Hierarchy

```
context-sanitary/
├── bin/                    # Node.js wrapper entry points
│   └── context-sanitary.js
├── scripts/                # Python helper scripts
│   └── sanitary_purge.py   # Core logic: pruning, checkpoint, memory offload/query
├── references/             # Specification documents
│   ├── pipeline.md         # 3-stage pipeline specification
│   ├── checkpoint_spec.md  # Checkpoint format & rules
│   └── memory_integration.md  # Memory provider integration guide
├── tests/                  # Test suite (not included in distributed package)
│   ├── evals/
│   │   └── dataset.json    # Evaluation dataset
│   └── validate_sanitization.py  # Automated validation script
├── assets/                 # Static assets (banner, logos)
├── SKILL.md                # Skill manifest for AI agents
├── .env.example            # Environment variable template (blank values)
├── .gitignore
├── LICENSE
├── CHANGELOG.md
├── SECURITY.md
├── package.json            # npm package config
├── setup.py                # pip package config
├── README.md               # English documentation
├── README.pt-BR.md         # Portuguese documentation
└── README.es-ES.md         # Spanish documentation
```

---

## 📦 Sanitized Output Payload Schema

The skill outputs a standardized JSON payload for persistent memory systems (Obsidian, Mem0, Supermemory, Honcho, etc.):

```json
{
  "sanitized_context": "Cleaned context text without noise or sensitive data.",
  "metadata": {
    "removed_items_count": 0,
    "has_pii_detected": false,
    "sanitization_level": "high|medium|low"
  },
  "persistent_facts": [
    "Timeless facts or preferences extracted for long-term persistence"
  ]
}
```

**Fields:**
- `sanitized_context` (string): The pruned, noise-free context ready for storage.
- `metadata` (object): Diagnostic info — count of removed items, PII detection flag, sanitization aggressiveness level.
- `persistent_facts` (array of strings): Extracted evergreen facts/preferences for long-term memory.

---

## 🚀 Installation & Getting Started

### Option A: Install via `pip` (Python Standard)

**1. Install**
```bash
pip install git+https://github.com/wxypereira/context-sanitary.git
# Or editable local install (clones full repo including tests)
pip install -e .
```

**For production use without test files:**
```bash
# Using pip with --no-deps and manual install, or download release artifact
pip install git+https://github.com/wxypereira/context-sanitary.git#subdirectory=.
```

**2. Test**
```bash
context-sanitary --test-checkpoint
```

**3. Uninstall**
```bash
pip uninstall context-sanitary
```

---

### Option B: Install via `pipx` (Recommended for Isolated CLI)

**1. Install**
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git
```

**For production use without test files:**
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git#subdirectory=.
```

**2. Test**
```bash
context-sanitary --test-checkpoint
```

**3. Uninstall**
```bash
pipx uninstall context-sanitary
```

---

### Option C: Install via `npm` / `npx` (Node.js)

**1. Install**
```bash
# Global install via npm (from npm registry, excludes test files)
npm install -g context-sanitary

# Or direct run without install via npx (from npm registry, excludes test files)
npx context-sanitary --test-checkpoint
```

**Note:** The npm package publishes only the distribution files (excludes `tests/`, `scripts/__pycache__/`, etc.).

**2. Test**
```bash
npx context-sanitary --test-checkpoint
```

**3. Uninstall**
```bash
npm uninstall -g context-sanitary
```

---

### Option D: Install as Agent Skill (`.gemini` / `Antigravity` / `Claude`)

**1. Install (full repo including tests):**
```bash
git clone https://github.com/wxypereira/context-sanitary.git
cp -r context-sanitary ~/.gemini/config/skills/
```

**2. Install (production — excludes test files):**
```bash
# Download only the skill folder without tests/evals
git clone --depth=1 --filter=blob:none --sparse https://github.com/wxypereira/context-sanitary.git
cd context-sanitary
git sparse-checkout set --no-cone SKILL.md references scripts/sanitary_purge.py bin assets
cp -r context-sanitary ~/.gemini/config/skills/
```

**3. Test**
```bash
# Inside an agent conversation:
/context-sanitary --test-checkpoint
```

**4. Uninstall**
```bash
rm -rf ~/.gemini/config/skills/context-sanitary
```

---

### Configure Environment Variables (Optional):

Copy `.env.example` to `.env` and set paths or API keys if using Obsidian, Honcho, Mem0, or Supermemory.
```bash
cp .env.example .env
```

---

## 🎮 Basic Usage

Run in your terminal or inside an agent conversation:

- `context-sanitary` (or `/context-sanitary`) — Runs algorithmic pruning, offloads to memory, and injects the Checkpoint.
- `context-sanitary --memory obsidian` — Targets a specific memory provider.
- `context-sanitary --auto 80%` — Enables auto-execution when context window hits 80%.
- `context-sanitary --no-auto` — Disables percentage-based auto-trigger.

---

## 🤝 Contribute

Contributions are welcome! Follow these steps:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/NewMemory`)
3. Commit your changes (`git commit -m 'Add: Support for new memory'`)
4. Push to the branch (`git push origin feature/NewMemory`)
5. Open a Pull Request

---

## 👥 Credits & Acknowledgments

This project was developed with the support of **Gemini 3.6 Flash**, alternating between **Muse Spark 1.3** and **Nemotron 3 Super**.

---

## 📝 License

This project is licensed under the [MIT License](./LICENSE).