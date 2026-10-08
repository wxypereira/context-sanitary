---
name: context-sanitary
description: >-
  Garbage Collector de contexto para agentes de IA. Higieniza o histórico eliminando ruído operacional
  (dumps de terminal, leituras mortas, prompts triviais), realiza offload de aprendizados para memória
  persistente (ai-memory, Obsidian, Holographic, Honcho [Experimental], Mem0 [Experimental], Supermemory [Experimental]) e injeta um Checkpoint consolidado com instrução de atenção estrita.
  Use quando o contexto estiver muito carregado, ao atingir limites de tokens, ou com os comandos /context-sanitary.
---

# Skill: `context-sanitary`

A skill **`context-sanitary`** atua como um *Garbage Collector* de contexto para agentes de IA. Diferente de resumos genéricos, ela limpa ruídos operacionais, sincroniza lições aprendidas com a memória persistente e declara um marcador de corte absoluto no histórico.

---

## 🚀 Sintaxe e Argumentos de Comando

| Comando / Argumento | Descrição |
| --- | --- |
| `/context-sanitary` | Executa a limpeza padrão, realiza offload de memória e injeta o Checkpoint. |
| `/context-sanitary --auto [X%]` | Ativa o gatilho automático ao atingir `X%` da capacidade da janela de contexto (ex: `--auto 80%`). |
| `/context-sanitary --no-auto` | Desativa a execução automática por porcentagem de contexto. |
| `/context-sanitary --aggressive` | Força a remoção de todas as mensagens intermediárias, mantendo apenas a instrução inicial e o estado final. |
| `/context-sanitary --memory [provider]` | Especifica a memória de destino/busca (`ai-memory`, `obsidian`, `holographic`, `honcho` [Experimental], `mem0` [Experimental], `supermemory` [Experimental] ou `all`). Padrão: `all`. |

---

## 🛠️ Pipeline de Execução em 3 Estágios

Consulte a especificação detalhada em [pipeline.md](./references/pipeline.md).

1. **Estágio 1: Poda Heurística Algorítmica (Zero Tokens)**
   - Remove dumps de terminal e logs antigos. Trunca erros ativos para as 5 primeiras e 5 últimas linhas relevantes.
   - Elimina leituras de arquivos não modificados nem citados na iteração ativa.
   - Apaga prompts triviais de navegação e inspeção.

2. **Estágio 2: Offload e Consulta à Memória Persistente**
   - **Offload:** Transfere padrões `[Erro Corrigido ➔ Solução]` para `ai-memory`, `Obsidian`, `Holographic Memory` (nativos) ou `Honcho`, `mem0`, `supermemory` ([Stubs/Experimentais]).
   - **Consulta:** Faz busca FTS/vetorial/associativa por restrições técnicas do projeto e arquivos ativos.

3. **Estágio 3: Injeção do Checkpoint & Marcador Estrito**
   - Gera a estrutura enxuta consolidada.
   - Injeta instrução crítica de atenção descartando qualquer histórico anterior ao marcador.

---

## 📄 Anatomia do Checkpoint

Veja o template e regras completas em [checkpoint_spec.md](./references/checkpoint_spec.md).

```markdown
=== 🧹 SANITARY CONTEXT CHECKPOINT ===
[TIMESTAMP: YYYY-MM-DD HH:MM:SS] | [STATUS: LIXO REMOVIDO / ESTADO CONSOLIDADO]

⚠️ INSTRUÇÃO CRÍTICA AO AGENTE:
O contexto anterior a este marcador foi higienizado. NÃO utilize, consulte ou tente recuperar mensagens, logs ou outputs anteriores a este bloco. Todo o estado relevante do projeto foi consolidado abaixo.

## 🎯 Objetivo Atual da Sessão
- [Descrição do objetivo em andamento]

## 🚨 Status de Erros & Pendências Operacionais
- [SE HOUVER ERRO ATIVO]: "Execução pausada no erro X no arquivo Y. Stack trace limpo: ..."
- [SE LIMPO]: "Nenhum erro ativo no momento."

## 📂 Arquivos Ativos em Foco
- `caminho/do/arquivo1.ext` (Modificado - contém a lógica X)
- `caminho/do/arquivo2.ext` (Referência ativa)

## 🛡️ Restrições & Aprendizados (Recuperados da Memória Persistente)
- Restrição 1: [Regra derivada de erro corrigido na sessão ou projeto]
- Restrição 2: [Diretriz técnica recuperada da memória]

## ⏭️ Próxima Ação Imediata
- [Ação exata que o agente deve executar a seguir]
==================================================
```

---

## 🔄 Integração com Memória Persistente

Consulte o guia detalhado em [memory_integration.md](./references/memory_integration.md).

- **Sincronização (Offload):** Varre ciclos resolvidos e grava na wiki em `ai-memory`, no vault em `Obsidian`, no banco associativo em `Holographic` (nativos) ou prepara envio em `Honcho`, `mem0`, `supermemory` ([Stubs/Experimentais]).
- **Consulta Ativa:** Recupera tags e lições vinculadas aos arquivos da sessão e insere no Checkpoint.
