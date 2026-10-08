# Changelog — context-sanitary

Todas as mudanças relevantes deste projeto são documentadas aqui, em formato
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

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
