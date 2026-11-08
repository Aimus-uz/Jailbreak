#!/usr/bin/env python3
"""GAMEPOINT: put Uzbek or Russian texts into the Jailbreak source before building.

    python3 tools/gp-lang/apply.py uz     (or ru)

Run from the repository root on a clean checkout. The English source stays in git;
this only changes the working copy used for the build. If upstream changed a text,
the script stops and prints which one, so the translation table can be updated.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, 'entries_lang.py'), encoding='utf-8').read(), ns)
exec(open(os.path.join(HERE, 'entries_mod.py'), encoding='utf-8').read(), ns)
ENTRIES = ns['E'] + ns['E2']

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('uz', 'ru'):
        sys.exit('usage: apply.py uz|ru')
    col = 2 if sys.argv[1] == 'uz' else 3
    missing, done, cache = [], 0, {}
    for entry in ENTRIES:
        path, find, repl = entry[0], entry[1], entry[col]
        if path not in cache:
            raw = open(path, 'rb').read()
            bom = raw.startswith(b'\xef\xbb\xbf')
            text = raw.decode('utf-8-sig')
            crlf = '\r\n' in text
            cache[path] = [text.replace('\r\n', '\n'), bom, crlf]
        text = cache[path][0]
        n = text.count(find)
        if n == 0:
            missing.append((path, find.splitlines()[0][:90]))
            continue
        cache[path][0] = text.replace(find, repl)
        done += n
    for path, (text, bom, crlf) in cache.items():
        if crlf: text = text.replace('\n', '\r\n')
        data = text.encode('utf-8')
        open(path, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + data)
    print(f'[gp-lang] {sys.argv[1]}: {done} replacements in {len(cache)} files')
    if missing:
        print('[gp-lang] NOT FOUND (upstream text changed?):')
        for p, f in missing: print(f'  {p}: {f}')
        sys.exit(1)

if __name__ == '__main__':
    main()
