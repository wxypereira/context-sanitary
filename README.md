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

## 🚀 Installation & Getting Started

### Option A: Install via `pip` (Python Standard)

**1. Install**
```bash
pip install git+https://github.com/wxypereira/context-sanitary.git
# Or editable local install
pip install -e .
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
# Global install via npm
npm install -g context-sanitary

# Or direct run without install via npx
npx context-sanitary --test-checkpoint
```

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

**1. Install**
```bash
git clone https://github.com/wxypereira/context-sanitary.git
cp -r context-sanitary ~/.gemini/config/skills/
```

**2. Test**
```bash
# Inside an agent conversation:
/context-sanitary --test-checkpoint
```

**3. Uninstall**
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

This project was developed with the support of:
- **Antigravity** (Google DeepMind Team)
- **OpenCode** (Muse Spark 1.3 Zen Agent)
- **AI Models:** **Gemini 3.6** & **Muse Spark 1.3** (Google DeepMind)

---

## 📝 License

This project is licensed under the [MIT License](./LICENSE).