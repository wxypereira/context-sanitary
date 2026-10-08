# Changelog — context-sanitary

Todas as mudanças relevantes deste projeto são documentadas aqui, em formato
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

## [0.2.0] — 2026-10-07

Atualizações de documentação, segurança, internacionalização e ciclo de validação de instalação.

### Adicionado
- **SECURITY.md** reescrito em inglês: orienta abertura de **GitHub Issue** com template/label `security` / `vulnerability` em vez de contato privado; prazo de resposta de 5 dias úteis; creditação no CHANGELOG.
- **README.md** totalmente em inglês (título, descrição, seções, instruções).
- **Barra de navegação por idiomas** nos 3 READMEs (EN/PT/ES), posicionada logo abaixo do banner: `[English](README.md) | [Español](README.es-ES.md) | [Português](README.pt-BR.md)`.
- **Créditos atualizados**: referência explícita ao modelo de IA **Gemini 2.5 Pro** (Google DeepMind), em vez de harness/interface.
- **Ciclo de validação e limpeza** documentado para **cada método de instalação** (pip, pipx, npm/npx, clone manual como Skill): sequência obrigatória — Download/Instalação → Teste Prático → Validação → Remoção/Limpeza — garantindo isolamento entre métodos.

### Alterado
- `README.md`, `README.pt-BR.md`, `README.es-ES.md`: estrutura unificada com navegação por idiomas, seções traduzidas, tabela de memórias, resultados de testes, e blocos de instalação com ciclo completo (instalar → testar → validar → limpar).
- `SECURITY.md`: política agora em inglês, uso de Issue GitHub com tag de segurança, sem e-mail/contato privado.
- Créditos em todos os READMEs: **Modelo de IA: Gemini 2.5 Pro** (Google DeepMind).

### Segurança
- `SECURITY.md` orienta Issue pública com label `security`/`vulnerability`; mantém regras de segredos (`.env.example` vazio, `.env` no `.gitignore`, `check_pr.py` pré-PR).

---

## [0.1.0] — 2026-10-07

Sessão de Pair Programming (Antigravity + OpenCode / Muse Spark 1.3).
Versão local oficial em `/home/pereira/maestri/context-sanitary`, espelhada em
`~/.gemini/config/skills/context-sanitary`. Sem push ao GitHub nesta sessão.

### Adicionado
- Skill `context-sanitary` (Garbage Collector de contexto) com pipeline em
  3 estágios: poda heurística (zero tokens), offload/consulta em memória
  persistente e injeção de Checkpoint com marcador estrito.
- Suporte a 6 provedores de memória persistente:
  - Nativos (locais): `ai-memory` (`~/.ai-memory/wiki/`), `Obsidian`
    (`Knowledge/AI_Lessons.md`), `Holographic Memory`
    (`~/.hermes/holographic_memory.json`).
  - Experimentais (stubs): `Honcho`, `Mem0`, `Supermemory` — sinalizados
    como `[Stub/Experimental]` no script e na documentação.
- `scripts/sanitary_purge.py` com `MemoryManager(provider=all)`,
  `truncate_log()` com guarda contra texto nulo/vazio, `format_checkpoint()`
  genérico e CLI completa via `argparse`: `--test-checkpoint`,
  `--test-memory`, `--auto`, `--no-auto`, `--aggressive`, `--memory`.
- Distribuição dupla:
  - Python (`setup.py`, `console_scripts`: `context-sanitary`,
    `sanitary-purge`) instalável via `pip` / `pipx`.
  - Node (`package.json`, `bin/context-sanitary.js` com detecção
    `win32 ? python : python3`) executável via `npm` / `npx`.
- Documentação: `SKILL.md`, `references/` (`pipeline.md`,
  `checkpoint_spec.md`, `memory_integration.md`), `README.md` (EN) +
  `README.pt-BR.md` + `README.es-ES.md` com seletores de idioma,
  `assets/banner.jpeg` referenciado nos 3 READMEs, tabela de suporte às
  memórias e resultados empíricos dos testes.
- Base de publicação: `LICENSE` (MIT, formato SPDX), `.gitignore`
  (`__pycache__/`, `*.pyc`, `.env`), `.env.example`
  (`VAULT_PATH`, `HONCHO_*`, `MEM0_*`, `SUPERMEMORY_*`, `MEMORY_PROVIDER`).
- `SECURITY.md` (política de segurança) e `scripts/check_pr.py`
  (verificação local pré-PR com `--fix`).

### Corrigido
- `pipeline.md` e `checkpoint_spec.md` atualizados para os 6 provedores
  (antes citavam só `ai-memory`/`mem0`/`supermemory`).
- `LICENSE` convertida para o formato SPDX padrão (sem `#` no título).
- `except:` nus substituídos por `logging.error`/`logging.warning`
  explícitos; colisão de nomes de arquivo evitada com microssegundos
  (`%Y%m%d_%H%M%S_%f`).
- Divergência CLI × docs: flag `--no-auto` adicionada ao `argparse`.
- URLs de instalação unificadas para o repo oficial
  `https://github.com/wxypereira/context-sanitary` (antes `maestri-ai` /
  `seu-usuario`).

### Segurança
- Nenhuma chave real no repositório: `.env.example` só com chaves vazias,
  `.env` ignorado pelo git. Ver `SECURITY.md`.