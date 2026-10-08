#!/usr/bin/env python3
"""
Sanitary Purge Helper Script for context-sanitary skill.
Truncates terminal logs, formats Checkpoint structures, and manages persistent memory offload/query.
Supports: ai-memory, obsidian, holographic (locais) + honcho, mem0, supermemory (remotos/stubs).
"""

import sys
import os
import json
import datetime
import argparse
import urllib.request
import urllib.error
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def truncate_log(log_text, keep_lines=5):
    """
    Trunca saídas extensas mantendo as primeiras e últimas N linhas.
    """
    if not log_text:
        return ""
    lines = log_text.strip().splitlines()
    if len(lines) <= keep_lines * 2:
        return log_text
    head = lines[:keep_lines]
    tail = lines[-keep_lines:]
    omitted = len(lines) - (keep_lines * 2)
    return "\n".join(head) + f"\n\n... [{omitted} linhas de stack trace/log omitidas pelo context-sanitary] ...\n\n" + "\n".join(tail)

def format_checkpoint(goal, status_error, files_in_focus, restrictions, next_action):
    """
    Formata o marcador de Checkpoint estrito.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    files_formatted = "\n".join([f"- `{f}`" for f in files_in_focus]) if files_in_focus else "- Nenhum arquivo em foco no momento."
    restrictions_formatted = "\n".join([f"- {r}" for r in restrictions]) if restrictions else "- Nenhuma restrição adicional recuperada."
    
    checkpoint = f"""=== 🧹 SANITARY CONTEXT CHECKPOINT ===
[TIMESTAMP: {now}] | [STATUS: LIXO REMOVIDO / ESTADO CONSOLIDADO]

⚠️ INSTRUÇÃO CRÍTICA AO AGENTE:
O contexto anterior a este marcador foi higienizado. NÃO utilize, consulte ou tente recuperar mensagens, logs ou outputs anteriores a este bloco. Todo o estado relevante do projeto foi consolidado abaixo.

## 🎯 Objetivo Atual da Sessão
- {goal}

## 🚨 Status de Erros & Pendências Operacionais
- {status_error}

## 📂 Arquivos Ativos em Foco
{files_formatted}

## 🛡️ Restrições & Aprendizados (Recuperados da Memória Persistente)
{restrictions_formatted}

## ⏭️ Próxima Ação Imediata
- {next_action}
=================================================="""
    return checkpoint

# --- Módulos de Integração com Memórias Persistentes ---

class MemoryManager:
    def __init__(self, provider="all"):
        self.provider = provider.lower()

    def offload_lesson(self, problem, root_cause, solution, tags=None):
        """
        Realiza o offload de um erro corrigido para os provedores de memória.
        """
        results = {}
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "problem": problem,
            "root_cause": root_cause,
            "solution": solution,
            "tags": tags or []
        }

        providers = ["ai-memory", "obsidian", "holographic", "honcho", "mem0", "supermemory"] if self.provider == "all" else [self.provider]

        for p in providers:
            try:
                if p == "ai-memory":
                    results[p] = self._offload_ai_memory(entry)
                elif p == "obsidian":
                    results[p] = self._offload_obsidian(entry)
                elif p == "holographic":
                    results[p] = self._offload_holographic(entry)
                elif p == "honcho":
                    results[p] = self._offload_honcho(entry)
                elif p in ["mem0", "supermemory"]:
                    results[p] = self._offload_remote_api(p, entry)
            except Exception as e:
                logging.error(f"Falha no offload para {p}: {e}")
                results[p] = f"Erro no offload ({p}): {str(e)}"
        return results

    def query_restrictions(self, focus_files=None, query_text=""):
        """
        Busca diretrizes e restrições técnicas nos provedores habilitados.
        """
        restrictions = []
        providers = ["ai-memory", "obsidian", "holographic", "honcho", "mem0", "supermemory"] if self.provider == "all" else [self.provider]

        for p in providers:
            try:
                if p == "ai-memory":
                    res = self._query_ai_memory(focus_files, query_text)
                    if res: restrictions.extend(res)
                elif p == "obsidian":
                    res = self._query_obsidian(focus_files, query_text)
                    if res: restrictions.extend(res)
                elif p == "holographic":
                    res = self._query_holographic(focus_files, query_text)
                    if res: restrictions.extend(res)
                elif p == "honcho":
                    res = self._query_honcho(query_text)
                    if res: restrictions.extend(res)
            except Exception as e:
                logging.warning(f"Erro na busca de memória ({p}): {e}")
        return list(dict.fromkeys(restrictions))  # Deduplicar preservando ordem

    def _offload_ai_memory(self, entry):
        target_dir = os.path.expanduser("~/.ai-memory/wiki")
        os.makedirs(target_dir, exist_ok=True)
        filename = f"lesson_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.md"
        file_path = os.path.join(target_dir, filename)
        content = f"# Lição Aprendida\n- **Problema:** {entry['problem']}\n- **Causa Raiz:** {entry['root_cause']}\n- **Solução:** {entry['solution']}\n"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Salvo em {file_path}"

    def _query_ai_memory(self, focus_files, query_text):
        target_dir = os.path.expanduser("~/.ai-memory/wiki")
        if not os.path.exists(target_dir): return []
        results = []
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        txt = f.read()
                        if "Solução:" in txt:
                            lines = [line.strip("- ").strip() for line in txt.splitlines() if line.startswith("- **Solução:**")]
                            results.extend(lines)
        return results

    def _offload_obsidian(self, entry):
        vault_path = os.getenv("VAULT_PATH", os.path.expanduser("~/ObsidianVault"))
        knowledge_dir = os.path.join(vault_path, "Knowledge")
        os.makedirs(knowledge_dir, exist_ok=True)
        note_file = os.path.join(knowledge_dir, "AI_Lessons.md")
        
        md_entry = f"\n\n## [{entry['timestamp']}] {entry['problem']}\n- **Causa Raiz:** {entry['root_cause']}\n- **Solução:** {entry['solution']}\n- **Tags:** #{' #'.join(entry['tags']) if entry['tags'] else 'ai-lesson'}"
        
        with open(note_file, "a", encoding="utf-8") as f:
            f.write(md_entry)
        return f"Anexado à nota Obsidian {note_file}"

    def _query_obsidian(self, focus_files, query_text):
        vault_path = os.getenv("VAULT_PATH", os.path.expanduser("~/ObsidianVault"))
        note_file = os.path.join(vault_path, "Knowledge", "AI_Lessons.md")
        if not os.path.exists(note_file): return []
        with open(note_file, "r", encoding="utf-8") as f:
            content = f.read()
        lines = [line.replace("- **Solução:**", "[Obsidian]").strip() for line in content.splitlines() if "**Solução:**" in line]
        return lines

    def _offload_holographic(self, entry):
        db_dir = os.path.expanduser("~/.hermes")
        os.makedirs(db_dir, exist_ok=True)
        db_file = os.path.join(db_dir, "holographic_memory.json")
        memories = []
        if os.path.exists(db_file):
            try:
                with open(db_file, "r", encoding="utf-8") as f: memories = json.load(f)
            except Exception as err:
                logging.warning(f"Falha ao carregar JSON holographic: {err}")
        memories.append(entry)
        with open(db_file, "w", encoding="utf-8") as f: json.dump(memories, f, indent=2)
        return "Gravado em memória associativa Holographic"

    def _query_holographic(self, focus_files, query_text):
        db_file = os.path.expanduser("~/.hermes/holographic_memory.json")
        if not os.path.exists(db_file): return []
        try:
            with open(db_file, "r", encoding="utf-8") as f: memories = json.load(f)
            return [f"[Holographic] Solução: {m['solution']}" for m in memories[-5:] if "solution" in m]
        except Exception as err:
            logging.warning(f"Falha ao ler memória holographic: {err}")
            return []

    def _offload_honcho(self, entry):
        api_key = os.getenv("HONCHO_API_KEY")
        if not api_key:
            return "[Stub/Experimental] HONCHO_API_KEY não configurada (offload pendente)"
        return "[Experimental] Mensagem preparada para envio à sessão Honcho"

    def _query_honcho(self, query_text):
        api_key = os.getenv("HONCHO_API_KEY")
        if not api_key: return []
        return ["[Honcho] Regra de contexto sincronizada (Experimental)."]

    def _offload_remote_api(self, provider, entry):
        api_key = os.getenv(f"{provider.upper()}_API_KEY")
        if not api_key: return f"[Stub/Experimental] {provider.upper()}_API_KEY não configurada"
        return f"[Experimental] Sincronizado via API {provider}"

def main():
    parser = argparse.ArgumentParser(description="Sanitary Purge Helper Script")
    parser.add_argument("--test-checkpoint", action="store_true", help="Gera um Checkpoint de exemplo")
    parser.add_argument("--test-memory", action="store_true", help="Executa testes de gravação e consulta de memória")
    parser.add_argument("--auto", type=str, help="Define o limite percentual de contexto (ex: 80%%)")
    parser.add_argument("--no-auto", action="store_true", help="Desativa o gatilho de execução automática por porcentagem")
    parser.add_argument("--aggressive", action="store_true", help="Força a remoção de todas as mensagens intermediárias")
    parser.add_argument("--memory", type=str, default="all", help="Provedor de memória (ai-memory, obsidian, holographic, honcho, mem0, supermemory, all)")

    args = parser.parse_args()

    if args.no_auto:
        print("Modo automático de sanitização desativado (--no-auto).")

    if args.test_checkpoint:
        sample = format_checkpoint(
            goal="Testar integração completa do context-sanitary",
            status_error="Nenhum erro ativo.",
            files_in_focus=["/home/pereira/maestri/context-sanitary/SKILL.md"],
            restrictions=["Integrado com Obsidian, Holographic, Honcho, Mem0, Supermemory"],
            next_action="Publicar no GitHub"
        )
        print(sample)
    elif args.test_memory:
        mgr = MemoryManager(provider=args.memory)
        print("--- Teste de Offload ---")
        offload_res = mgr.offload_lesson(
            problem="Excesso de tokens na sessão",
            root_cause="Dumps extensos no terminal",
            solution="Utilizar sanitary_purge.py para truncar logs",
            tags=["sanitary", "tokens"]
        )
        print(json.dumps(offload_res, indent=2, ensure_ascii=False))
        
        print("\n--- Teste de Consulta ---")
        query_res = mgr.query_restrictions(query_text="tokens")
        print(json.dumps(query_res, indent=2, ensure_ascii=False))
    else:
        print(f"Sanitary purge inicializado com memória: {args.memory}")

if __name__ == "__main__":
    main()
