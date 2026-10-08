# Pipeline da Skill `context-sanitary` em 3 Estágios

```
[Contexto Sujo] 
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ Estágio 1: Poda Heurística Algorítmica (Zero Tokens)   │
│ - Remove dumps de terminal e logs antigos              │
│ - Elimina leituras de arquivos não modificados/citados │
│ - Apaga prompts triviais de navegação e inspeção       │
└────────────────────────────────────────────────────────┘
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ Estágio 2: Offload e Consulta à Memória Persistente   │
│ - Envia [Erro Corrigido ➔ Solução] para memórias        │
│   (ai-memory, Obsidian, Holographic, Honcho, etc)      │
│ - Recupera ativamente restrições técnicas do projeto   │
└────────────────────────────────────────────────────────┘
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ Estágio 3: Injeção do Checkpoint & Instalação de Ponto │
│ - Gera estado enxuto + erro pendente (se houver)       │
│ - Define instrução estrita de ignorar o histórico     │
└────────────────────────────────────────────────────────┘
```

---

## Estágio 1: Poda Heurística Algorítmica (Zero Tokens)
Neste estágio inicial, filtros heurísticos são aplicados sem consumo extra de LLM para descartar dados operacionais descartáveis:
- **Dumps & Logs de Terminal:** Truncagem de saídas extensas mantendo no máximo 5 primeiras e 5 últimas linhas relevantes.
- **Leituras Mortas:** Descarte de conteúdos de arquivos consultados que não sofreram edições e não são mais referenciados no objetivo atual.
- **Prompts Triviais:** Eliminação de comandos intermediários repetitivos ou de mera navegação no sistema de arquivos.

---

## Estágio 2: Offload e Consulta à Memória Persistente
Garante a retenção do conhecimento útil e recupera aprendizados prévios:
- **Sincronização (Offload):** Varre a história recente da sessão buscando padrões do tipo `[Erro X ➔ Tentativa Y que falhou ➔ Solução Z]`. Grava essas triplas no `ai-memory`, `Obsidian Vault`, `Holographic Memory`, `Honcho` ou em provedores remotamente (`mem0` / `supermemory`).
- **Consulta Ativa:** Pesquisa na memória persistente por diretrizes, restrições e convenções associadas aos arquivos ativos da sessão, preparando-as para injeção no Checkpoint.

---

## Estágio 3: Injeção do Checkpoint & Marcador Estrito
Gera o bloco consolidado final contendo o timestamp, o objetivo atual, status limpo ou stack trace enxuto, arquivos em foco, restrições recuperadas e próxima ação imediata. Inclui a instrução explícita de atenção que impede o agente de olhar para mensagens anteriores ao Checkpoint.
