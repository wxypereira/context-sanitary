<p align="center">
  <img src="./assets/banner.jpeg" width="100%" alt="Context Sanitary Banner">
</p>

# Context Sanitary Skill

> Garbage Collector de contexto e sincronizador de memória persistente para Agentes de IA.

---

## ❓ Por que usar o Context Sanitary?

Durante conversas longas ou sessões intensas de desenvolvimento com Agentes de IA (como **Antigravity**, **OpenCode** e **Hermes**), a janela de contexto tende a ser degradada por:
1. **Dumps Extensos de Terminal e Stack Traces Mortos:** Logs repetitivos que consomem milhares de tokens sem agregar valor à solução.
2. **Alucinações por Excesso de Ruído:** O agente se perde ao tentar analisar comandos intermediários antigos de navegação.
3. **Perda de Lições Aprendidas entre Sessões:** Erros que já foram corrigidos voltam a acontecer se o agente não salvar o aprendizado em memória persistente.

O **Context Sanitary** resolve isso atuando em **3 estágios automáticos**:
- **Poda Heurística Algorítmica (Zero Tokens):** Limpa ruídos operacionais e trunca logs longos mantendo apenas a essência.
- **Offload & Consulta à Memória Persistente:** Salva lições aprendidas (`[Erro ➔ Causa ➔ Solução]`) no seu **Obsidian**, **Holographic Memory**, **ai-memory**, **Honcho**, **Mem0** ou **Supermemory**.
- **Checkpoint Estrito:** Injeta um marcador no histórico forçando o agente a ignorar mensagens passadas e focar unicamente no estado consolidado.

---

## 💡 About The Project

**Context Sanitary** é uma Skill projetada para gerenciar e otimizar a janela de contexto de agentes de IA em workflows de longo prazo. Ela garante performance máxima, menor custo com tokens e zero perda de memória.

## 🧠 Suporte a Memória Persistente

| Provedor de Memória | Tipo / Local | Status da Integração | Descrição |
| --- | --- | --- | --- |
| **`ai-memory`** (Akita) | Local (Wiki Markdown + SQLite) | 🟢 Nativo | Armazena em `~/.ai-memory/wiki/` para rastreamento Git. |
| **`Obsidian`** | Local (Markdown Vault) | 🟢 Nativo | Anexa na nota `Knowledge/AI_Lessons.md` com tags de frontmatter. |
| **`Holographic Memory`** | Local (Vetor Associativo / Hermes) | 🟢 Nativo | Registra em `~/.hermes/holographic_memory.json` com busca FTS5. |
| **`Honcho`** | Cloud / Session Reasoning | 🟡 Stub / Experimental | Sincroniza estado no nível de Workspace/Session (`HONCHO_API_KEY`). |
| **`Mem0`** | Cloud / Vector Store | 🟡 Stub / Experimental | Envia triplas de solução via REST API (`MEM0_API_KEY`). |
| **`Supermemory`** | Cloud / Long-term Memory | 🟡 Stub / Experimental | Armazena contextos para consultas vetoriais de longo prazo (`SUPERMEMORY_API_KEY`). |

## 🛠️ Tech Stack

[![My Skills](https://skillicons.dev/icons?i=python,nodejs,bash,git)](https://skillicons.dev)

- **Linguagem:** Python 3 (Script Helper) & Node.js Wrapper
- **Gerenciadores de Pacotes:** `pip` / `pipx` & `npm` / `npx`

## 🧪 Resultado dos Testes

O script de suporte conta com uma suíte autônoma de testes. Abaixo o resultado da execução de validação:

```bash
$ python3 scripts/sanitary_purge.py --test-memory

--- Teste de Offload ---
{
  "ai-memory": "Salvo em ~/.ai-memory/wiki/lesson_20261007_165206_856622.md",
  "obsidian": "Anexado à nota Obsidian ~/ObsidianVault/Knowledge/AI_Lessons.md",
  "holographic": "Gravado em memória associativa Holographic",
  "honcho": "[Stub/Experimental] HONCHO_API_KEY não configurada (offload pendente)",
  "mem0": "[Stub/Experimental] MEM0_API_KEY não configurada",
  "supermemory": "[Stub/Experimental] SUPERMEMORY_API_KEY não configurada"
}

--- Teste de Consulta ---
[
  "**Solução:** Utilizar sanitary_purge.py para truncar logs",
  "[Obsidian] Utilizar sanitary_purge.py para truncar logs",
  "[Holographic] Solução: Utilizar sanitary_purge.py para truncar logs"
]
```

## 🚀 Instalação & Getting Started

### Opção A: Instalação via `pip` (Python Standard)
```bash
# Instalação direta do repositório
pip install git+https://github.com/wxypereira/context-sanitary.git

# Ou instalação local editável
pip install -e .
```

### Opção B: Instalação via `pipx` (Recomendado para CLI Isolado)
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git
```

### Opção C: Instalação via `npm` / `npx` (Node.js)
```bash
# Instalação Global via npm
npm install -g context-sanitary

# Execução direta sem instalação via npx
npx context-sanitary --test-checkpoint
```

### Opção D: Instalação como Skill de Agente (`.gemini` / `Antigravity` / `Claude`)
```bash
git clone https://github.com/wxypereira/context-sanitary.git
cp -r context-sanitary ~/.gemini/config/skills/
```

### Configurar Variáveis de Ambiente (Opcional):
Copie `.env.example` para `.env` e configure os caminhos ou chaves de API caso utilize Obsidian, Honcho, Mem0 ou Supermemory.
```bash
cp .env.example .env
```

## 🎮 Basic Usage

Execute no seu terminal ou dentro de uma conversa com o agente:

- `context-sanitary` (ou `/context-sanitary`) — Executa a poda algorítmica, realiza offload para a memória e injeta o Checkpoint.
- `context-sanitary --memory obsidian` — Especifica um provedor de memória específico.
- `context-sanitary --auto 80%` — Configura execução automática quando a janela atingir 80%.
- `context-sanitary --no-auto` — Desativa o gatilho automático por porcentagem.

## 🤝 Contribute

Contribuições são super bem-vindas! Siga os passos abaixo:

1. Faça o Fork do projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/NovaMemoria`)
3. Faça o commit das suas alterações (`git commit -m 'Add: Suporte a nova memória'`)
4. Faça o push para a branch (`git push origin feature/NovaMemoria`)
5. Abra um Pull Request

## 👥 Créditos & Agradecimentos

Este projeto foi desenvolvido em Pair Programming com colaboração entre:
- **Antigravity** (Google DeepMind Team)
- **OpenCode** (Muse Spark 1.3 Zen Agent)

## 📝 License

Este projeto está sob a licença [MIT](./LICENSE).
