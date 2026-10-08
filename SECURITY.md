# Política de Segurança — context-sanitary

## Versões suportadas

| Versão | Suporte            |
| ------ | ------------------ |
| 0.1.x  | 🟢 Suportada       |
| < 0.1  | 🔴 Não suportada   |

## Como reportar uma vulnerabilidade

**Não abra issue pública para vulnerabilidades.** Prefira um canal privado:

1. Abra um issue privado ou contate os mantenedores (Antigravity + OpenCode)
   com: descrição, passos de reprodução, impacto e versão afetada.
2. Aguarde confirmação antes de divulgar. Prazo-alvo de resposta inicial:
   5 dias úteis.
3. Após correção e release, o reporte é creditado no `CHANGELOG.md`
   (salvo pedido de anonimato).

## Regras de segredos

- **Nunca commite segredos.** Chaves de API (`HONCHO_API_KEY`,
  `MEM0_API_KEY`, `SUPERMEMORY_API_KEY`) vão apenas em `.env` local,
  nunca no repositório.
- `.env.example` deve conter **só chaves vazias** (modelo, sem valores).
- `.env` está no `.gitignore` e não deve ser enviado em PRs.
- Antes de abrir um PR, rode `python3 scripts/check_pr.py` (com `--fix`
  se necessário) para detectar placeholders, URLs antigas e artefatos
  acidentais (`__pycache__/`, `.env`).

## Escopo

- `scripts/sanitary_purge.py` grava **apenas** em diretórios locais do
  usuário (`~/.ai-memory/wiki/`, `~/ObsidianVault/`, `~/.hermes/`) ou
  conforme `VAULT_PATH`. Não há exfiltração de dados: os provedores
  `honcho` / `mem0` / `supermemory` são **stubs experimentais** e não
  realizam chamadas de rede nesta versão.
- Dependências de runtime: apenas biblioteca padrão do Python 3.8+
  (sem downloads automáticos). O wrapper Node (`bin/context-sanitary.js`)
  apenas invoca `python3`/`python` local.
