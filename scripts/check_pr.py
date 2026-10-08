#!/usr/bin/env python3
"""Verificação local pré-PR do context-sanitary.

Uso:
    python3 scripts/check_pr.py [--fix]

O que verifica (sem git, sem rede):
 1. Sintaxe: py_compile em scripts/*.py + JSON válido em package.json +
    parse de setup.py.
 2. CLI: --help, --test-checkpoint, --test-memory --memory all em HOME
    isolado (tempdir), para não poluir ~/.ai-memory, ~/ObsidianVault, ~/.hermes.
 3. Placeholders proibidos: "seu-usuario", "maestri-ai".
 4. URL oficial: setup.py, package.json e READMEs devem apontar para
    github.com/wxypereira/context-sanitary.
 5. Banner: assets/banner.jpeg existe e é referenciado nos 3 READMEs.
 6. Stubs sinalizados: honcho/mem0/supermemory marcados como Experimental.
 7. Segredos: .env.example só com valores vazios; nenhum .env no repo.
 8. Artefatos: __pycache__/*.pyc presentes (--fix remove).

Saída 0 = tudo OK. Saída 1 = falhas (lista o que corrigir).
"""

import argparse
import json
import os
import py_compile
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFFICIAL_REPO = "github.com/wxypereira/context-sanitary"
FORBIDDEN = ["seu-usuario", "maestri-ai"]
READMES = ["README.md", "README.pt-BR.md", "README.es-ES.md"]
FAILURES = []


def fail(msg):
    FAILURES.append(msg)
    print(f"[FAIL] {msg}")


def ok(msg):
    print(f"[ ok ] {msg}")


def check_syntax():
    try:
        for fname in os.listdir(os.path.join(ROOT, "scripts")):
            if fname.endswith(".py"):
                py_compile.compile(
                    os.path.join(ROOT, "scripts", fname), doraise=True
                )
        ok("py_compile scripts/*.py")
    except Exception as e:
        fail(f"py_compile falhou: {e}")
    try:
        with open(os.path.join(ROOT, "package.json"), encoding="utf-8") as f:
            json.load(f)
        ok("package.json JSON válido")
    except Exception as e:
        fail(f"package.json inválido: {e}")
    try:
        import ast

        with open(os.path.join(ROOT, "setup.py"), encoding="utf-8") as f:
            ast.parse(f.read())
        ok("setup.py parse OK")
    except Exception as e:
        fail(f"setup.py inválido: {e}")


def run(cmd, env=None):
    r = subprocess.run(
        cmd, cwd=ROOT, capture_output=True, text=True, env=env, timeout=120
    )
    return r


def check_cli():
    py = sys.executable
    script = os.path.join(ROOT, "scripts", "sanitary_purge.py")
    tmp_home = tempfile.mkdtemp(prefix="sanitary-pr-check-")
    env = dict(os.environ, HOME=tmp_home, VAULT_PATH=os.path.join(tmp_home, "vault"))
    try:
        r = run([py, script, "--help"], env=env)
        if r.returncode == 0 and "--no-auto" in r.stdout:
            ok("CLI --help com --no-auto")
        else:
            fail("CLI --help sem --no-auto ou com erro")
        r = run([py, script, "--test-checkpoint"], env=env)
        if r.returncode == 0 and "SANITARY CONTEXT CHECKPOINT" in r.stdout:
            ok("CLI --test-checkpoint")
        else:
            fail("--test-checkpoint não gerou Checkpoint")
        r = run([py, script, "--test-memory", "--memory", "all"], env=env)
        out = r.stdout + r.stderr
        if r.returncode == 0 and all(
            k in out for k in ("ai-memory", "holographic", "honcho", "mem0", "supermemory")
        ):
            ok("CLI --test-memory --memory all (6 providers)")
        else:
            fail("--test-memory --memory all incompleto")
        r = run([py, "-c", "from scripts.sanitary_purge import truncate_log; "
                 "assert truncate_log('')==''; assert truncate_log(None)==''"],
                env=env)
        if r.returncode == 0:
            ok("truncate_log guarda nulo/vazio")
        else:
            fail("truncate_log sem guarda: " + (r.stderr.strip() or "assert falhou"))
    finally:
        shutil.rmtree(tmp_home, ignore_errors=True)


SKIP_PLACEHOLDER_CHECK = {"CHANGELOG.md", "check_pr.py"}


def text_files():
    for dirpath, _, filenames in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for fn in filenames:
            if fn in SKIP_PLACEHOLDER_CHECK:
                continue
            if fn.endswith((".md", ".py", ".json", ".js", ".example")):
                yield os.path.join(dirpath, fn)


def check_placeholders():
    bad = []
    for path in text_files():
        try:
            with open(path, encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except OSError:
            continue
        for token in FORBIDDEN:
            if token in content:
                bad.append(f"{os.path.relpath(path, ROOT)} contém '{token}'")
    if bad:
        for b in bad:
            fail(b)
    else:
        ok("sem placeholders (seu-usuario/maestri-ai)")


def check_repo_url():
    targets = ["setup.py", "package.json"] + READMES
    missing = []
    for rel in targets:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            if OFFICIAL_REPO not in f.read():
                missing.append(rel)
    if missing:
        fail("sem URL oficial em: " + ", ".join(missing))
    else:
        ok(f"URL oficial {OFFICIAL_REPO} em setup/package/READMEs")


def check_banner():
    banner = os.path.join(ROOT, "assets", "banner.jpeg")
    if not os.path.isfile(banner):
        fail("assets/banner.jpeg ausente")
        return
    ok("assets/banner.jpeg existe")
    for rel in READMES:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            if "assets/banner.jpeg" in f.read():
                ok(f"{rel} referencia o banner")
            else:
                fail(f"{rel} não referencia assets/banner.jpeg")


def check_stubs():
    for rel in ["SKILL.md", "references/memory_integration.md"]:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            content = f.read()
        if re.search(r"[Ee]xperimental|Stub", content):
            ok(f"{rel} sinaliza stubs")
        else:
            fail(f"{rel} sem marcação Experimental/Stub")


def check_secrets():
    if os.path.exists(os.path.join(ROOT, ".env")):
        fail(".env presente no repo (não commitar)")
    else:
        ok("sem .env no repo")
    example = os.path.join(ROOT, ".env.example")
    bad = []
    with open(example, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            # VAULT_PATH e MEMORY_PROVIDER são defaults locais, não segredos.
            if key in ("VAULT_PATH", "MEMORY_PROVIDER"):
                continue
            if val.strip().strip('"').strip("'"):
                bad.append(key)
    if bad:
        fail(".env.example com valores preenchidos: " + ", ".join(bad))
    else:
        ok(".env.example só com chaves vazias")


def check_artifacts(fix=False):
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        if "__pycache__" in dirnames:
            found.append(os.path.join(dirpath, "__pycache__"))
        for fn in filenames:
            if fn.endswith(".pyc"):
                found.append(os.path.join(dirpath, fn))
    if not found:
        ok("sem __pycache__/*.pyc")
        return
    if fix:
        for p in found:
            if os.path.isdir(p):
                shutil.rmtree(p, ignore_errors=True)
            elif os.path.exists(p):
                os.remove(p)
        ok(f"removidos {len(found)} artefato(s) __pycache__/*.pyc")
    else:
        fail(f"{len(found)} artefato(s) __pycache__/*.pyc (rode com --fix)")


def main():
    ap = argparse.ArgumentParser(description="Verificação pré-PR (local, sem git)")
    ap.add_argument("--fix", action="store_true", help="Remove __pycache__/*.pyc")
    args = ap.parse_args()

    # Artefatos primeiro: py_compile/CLI abaixo recriam __pycache__,
    # então o gate vale para o estado pré-execução.
    check_artifacts(fix=args.fix)
    check_syntax()
    check_cli()
    check_placeholders()
    check_repo_url()
    check_banner()
    check_stubs()
    check_secrets()
    if args.fix:
        # Limpa o __pycache__ regenerado pelas verificações acima.
        check_artifacts(fix=True)
    else:
        # Limpeza silenciosa do __pycache__ regenerado por este próprio
        # script (py_compile), sem mascarar o gate pré-execução acima.
        for dirpath, dirnames, filenames in os.walk(ROOT):
            if ".git" in dirpath:
                continue
            if "__pycache__" in dirnames:
                shutil.rmtree(os.path.join(dirpath, "__pycache__"), ignore_errors=True)
            for fn in filenames:
                if fn.endswith(".pyc"):
                    try:
                        os.remove(os.path.join(dirpath, fn))
                    except OSError:
                        pass

    print()
    if FAILURES:
        print(f"{len(FAILURES)} falha(s). Corrija antes de abrir o PR.")
        return 1
    print("Tudo OK — pronto para abrir o PR.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
