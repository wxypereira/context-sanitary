<p align="center">
  <img src="./assets/banner.jpeg" width="100%" alt="Context Sanitary Banner">
</p>

[English](README.md) | [Español](README.es-ES.md) | [Português](README.pt-BR.md)

---

# Context Sanitary Skill

> Garbage Collector de contexto e sincronizador de memória persistente para Agentes de IA.

---

## ❓ Por que usar o Context Sanitary?

Durante conversas longas ou sessões intensas de desenvolvimento com agentes de IA (como **Antigravity**, **OpenCode** e **Hermes**), a janela de contexto tende a se degradar por:

1. **Logs extensos de terminal e stack traces obsoletos:** registros repetitivos que consomem milhares de tokens sem agregar valor à solução.
2. **Alucinações por excesso de ruído:** o agente perde-se ao tentar interpretar comandos intermediários antigos de navegação.
3. **Perda de lições aprendidas entre sessões:** erros já corrigidos voltam a ocorrer caso o agente não persista o aprendizado em memória persistente.

O **Context Sanitary** resolve isso em **3 estágios automáticos**:

- **Poda heurística algorítmica (zero tokens):** elimina ruídos operacionais e trunca logs extensos, preservando apenas o essencial.
- **Offload e consulta à memória persistente:** salva lições aprendidas (`[Erro ➔ Causa ➔ Solução]`) no **Obsidian**, **Holographic Memory**, **ai-memory**, **Honcho**, **Mem0** ou **Supermemory**.
- **Checkpoint estrito:** injeta um marcador no histórico, forçando o agente a ignorar mensagens anteriores e concentrar-se exclusivamente no estado consolidado.

---

## 💡 Sobre o Projeto

**Context Sanitary** é uma skill projetada para gerenciar e otimizar a janela de contexto de agentes de IA em fluxos de trabalho de longo prazo. Ela assegura desempenho máximo, menor custo com tokens e nenhuma perda de memória.

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

O script auxiliar conta com uma suíte autônoma de testes. Abaixo, o resultado da execução de validação:

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

---

## 📁 Hierarquia de Pastas

```
context-sanitary/
├── bin/                    # Pontos de entrada do wrapper Node.js
│   └── context-sanitary.js
├── scripts/                # Scripts auxiliares em Python
│   └── sanitary_purge.py   # Lógica principal: poda, checkpoint, offload/consulta de memória
├── references/             # Documentos de especificação
│   ├── pipeline.md         # Especificação do pipeline em 3 estágios
│   ├── checkpoint_spec.md  # Formato e regras do Checkpoint
│   └── memory_integration.md  # Guia de integração com provedores de memória
├── tests/                  # Suite de testes (não incluída no pacote distribuído)
│   ├── evals/
│   │   └── dataset.json    # Dataset de avaliação
│   └── validate_sanitization.py  # Script de validação automatizada
├── assets/                 # Assets estáticos (banner, logos)
├── SKILL.md                # Manifesto da skill para agentes de IA
├── .env.example            # Template de variáveis de ambiente (valores em branco)
├── .gitignore
├── LICENSE
├── CHANGELOG.md
├── SECURITY.md
├── package.json            # Configuração do pacote npm
├── setup.py                # Configuração do pacote pip
├── README.md               # Documentação em inglês
├── README.pt-BR.md         # Documentação em português
└── README.es-ES.md         # Documentação em espanhol
```

---

## 📦 Schema do Payload de Saída Sanitizado

A skill gera um payload JSON padronizado para sistemas de memória persistente (Obsidian, Mem0, Supermemory, Honcho, etc.):

```json
{
  "sanitized_context": "Texto do contexto higienizado, sem ruídos e sem dados sensíveis.",
  "metadata": {
    "removed_items_count": 0,
    "has_pii_detected": false,
    "sanitization_level": "high|medium|low"
  },
  "persistent_facts": [
    "Fatos ou preferências atemporais extraídos para persistência de longo prazo"
  ]
}
```

**Campos:**
- `sanitized_context` (string): O contexto podado, livre de ruídos, pronto para armazenamento.
- `metadata` (objeto): Informações diagnósticas — contagem de itens removidos, flag de detecção de PII, nível de agressividade da sanitização.
- `persistent_facts` (array de strings): Fatos/preferências perenes extraídos para memória de longo prazo.

---

## 🚀 Instalação & Início Rápido

### Opção A: Instalação via `pip` (Python Standard)

**1. Instalar**
```bash
pip install git+https://github.com/wxypereira/context-sanitary.git
# Ou instalação local editável (clona repo completo incluindo testes)
pip install -e .
```

**Para uso em produção sem arquivos de teste:**
```bash
# Usando pip com subdirectory
pip install git+https://github.com/wxypereira/context-sanitary.git#subdirectory=.
```

**2. Testar**
```bash
context-sanitary --test-checkpoint
```

**3. Desinstalar**
```bash
pip uninstall context-sanitary
```

---

### Opção B: Instalação via `pipx` (Recomendado para CLI Isolado)

**1. Instalar**
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git
```

**Para uso em produção sem arquivos de teste:**
```bash
pipx install git+https://github.com/wxypereira/context-sanitary.git#subdirectory=.
```

**2. Testar**
```bash
context-sanitary --test-checkpoint
```

**3. Desinstalar**
```bash
pipx uninstall context-sanitary
```

---

### Opção C: Instalação via `npm` / `npx` (Node.js)

**1. Instalar**
```bash
# Instalação global via npm (do npm registry, exclui arquivos de teste)
npm install -g context-sanitary

# Ou execução direta sem instalação via npx (do npm registry, exclui arquivos de teste)
npx context-sanitary --test-checkpoint
```

**Nota:** O pacote npm publica apenas os arquivos de distribuição (exclui `tests/`, `scripts/__pycache__/`, etc.).

**2. Testar**
```bash
npx context-sanitary --test-checkpoint
```

**3. Desinstalar**
```bash
npm uninstall -g context-sanitary
```

---

### Opção D: Instalação como Skill de Agente (`.gemini` / `Antigravity` / `Claude`)

**1. Instalar (repo completo incluindo testes):**
```bash
git clone https://github.com/wxypereira/context-sanitary.git
cp -r context-sanitary ~/.gemini/config/skills/
```

**2. Instalar (produção — exclui arquivos de teste):**
```bash
# Baixa apenas a pasta da skill sem tests/evals
git clone --depth=1 --filter=blob:none --sparse https://github.com/wxypereira/context-sanitary.git
cd context-sanitary
git sparse-checkout set --no-cone SKILL.md references scripts/sanitary_purge.py bin assets
cp -r context-sanitary ~/.gemini/config/skills/
```

**3. Testar**
```bash
# Dentro de uma conversa com o agente:
/context-sanitary --test-checkpoint
```

**4. Desinstalar**
```bash
rm -rf ~/.gemini/config/skills/context-sanitary
```

---

### Configurar Variáveis de Ambiente (Opcional):

Copie `.env.example` para `.env` e configure os caminhos ou chaves de API caso utilize Obsidian, Honcho, Mem0 ou Supermemory.
```bash
cp .env.example .env
```

---

## 🎮 Uso Básico

Execute no seu terminal ou dentro de uma conversa com o agente:

- `context-sanitary` (ou `/context-sanitary`) — Executa a poda algorítmica, realiza offload para a memória e injeta o Checkpoint.
- `context-sanitary --memory obsidian` — Especifica um provedor de memória específico.
- `context-sanitary --auto 80%` — Configura execução automática quando a janela atingir 80%.
- `context-sanitary --no-auto` — Desativa o gatilho automático por porcentagem.

---

## 🤝 Contribuir

Contribuições são super bem-vindas! Siga os passos abaixo:

1. Faça o Fork do projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/NovaMemoria`)
3. Faça o commit das suas alterações (`git commit -m 'Add: Suporte a nova memória'`)
4. Faça o push para a branch (`git push origin feature/NovaMemoria`)
5. Abra um Pull Request

---

## 👥 Créditos & Agradecimentos

Este projeto foi desenvolvido com o suporte do **Gemini 3.6 Flash**, alternando entre **Muse Spark 1.3** e **Nemotron 3 Super**.

---

## 📝 Licença

Este projeto está sob a licença [MIT](./LICENSE).