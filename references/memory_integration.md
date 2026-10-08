# Guia de Integração com Memória Persistente

A skill **`context-sanitary`** conecta-se ativamente com sistemas de memória de longo prazo em duas direções:

---

## 📚 Provedores de Memória Suportados

1. **`ai-memory` (Akita):** Wiki local em Markdown com índice SQLite para versionamento Git. (Suporte Nativo)
2. **`Obsidian`:** Vault em Markdown com tags de frontmatter e notas em `Knowledge/AI_Lessons.md`. (Suporte Nativo)
3. **`Holographic Memory` (Hermes / Neo37):** Armazenamento de vetores associativos com FTS5 e matrizes de memória SDM. (Suporte Nativo)
4. **`Honcho`:** Plataforma cloud e open-source de raciocínio contextual. ([Stub/Experimental])
5. **`Mem0` & `Supermemory`:** Repositórios remotos vetoriais acessíveis por REST API. ([Stub/Experimental])

---

## 📥 1. Sincronização (Offload de Saída)

Durante a fase de destilação de contexto, antes do descarte do histórico intermediário:

1. **Detecção de Soluções:** O pipeline identifica sequências do tipo `[Erro X ➔ Tentativa Y ➔ Solução Z]`.
2. **Gravando nas Memórias:**
   - **`ai-memory`:** Salva nova lição em `~/.ai-memory/wiki/`.
   - **`Obsidian`:** Anexa a entrada com timestamp e tags na nota `Knowledge/AI_Lessons.md`.
   - **`Holographic`:** Registra o evento no arquivo de memória associativa `~/.hermes/holographic_memory.json`.
   - **`Honcho`:** Prepara a mensagem no nível da sessão `HONCHO_WORKSPACE_ID` ([Stub/Experimental]).
   - **`Mem0 / Supermemory`:** Estrutura requisição HTTP POST para a API correspondente ([Stub/Experimental]).

---

## 📤 2. Consulta Ativa (Injeção de Entrada)

Antes da geração final do Checkpoint:

1. **Busca FTS e Associativa:** O `context-sanitary` realiza consultas usando tags do projeto e nomes de arquivos em foco.
2. **Resgate de Lições:** Diretrizes aprendidas em sessões passadas são resgatadas dos provedores locais/remotos.
3. **Injeção de Diretrizes:** As lições encontradas são deduplicadas e formatadas na seção `## 🛡️ Restrições & Aprendizados` do Checkpoint.
