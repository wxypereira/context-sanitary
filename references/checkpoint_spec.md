# Especificação e Anatomia do Checkpoint Injetado

O Checkpoint atua como um divisor de águas absoluto na janela de contexto. Ele força o agente a ignorar o histórico anterior e focar apenas nas informações consolidadas.

---

## 📋 Modelo de Checkpoint

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
- Restrição 2: [Diretriz técnica recuperada da memória: ai-memory, Obsidian, Holographic, Honcho, etc.]

## ⏭️ Próxima Ação Imediata
- [Ação exata que o agente deve executar a seguir]
==================================================
```

---

## 🛠️ Regras de Tratamento de Erros Incompletos

Se a última ação do terminal retornou uma falha não resolvida:
1. **Truncagem de Stack Trace:** Corta logs longos mantendo apenas as primeiras 5 e últimas 5 linhas mais relevantes.
2. **Registro de Falha Pendente:** O erro sintetizado é listado na seção `## 🚨 Status de Erros & Pendências Operacionais`.
3. **Offload de Tentativas Frustradas:** As tentativas malsucedidas intermediárias são movidas para a memória persistente como histórico de tentativas para evitar a repetição de abordagens erradas após o checkpoint.
