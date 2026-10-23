"""Reproducible source count. No vendored code, generated data or fixture duplication."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {'.java': 'Java', '.mjs': 'JavaScript', '.js': 'JavaScript', '.css': 'CSS', '.html': 'HTML', '.py': 'Python'}

def audit():
    records = []
    for folder in ('src', 'web', 'tests'):
        for path in sorted((ROOT / folder).rglob('*')):
            if not path.is_file() or path.suffix not in EXTENSIONS:
                continue
            relative = path.relative_to(ROOT).as_posix()
            if '/samples/' in relative or '__pycache__' in relative:
                continue
            lines = path.read_text(encoding='utf-8').splitlines()
            records.append({'path': relative, 'language': EXTENSIONS[path.suffix],
                            'physical': len(lines), 'nonempty': sum(bool(line.strip()) for line in lines),
                            'category': 'tests' if folder == 'tests' else 'product'})
    def total(items):
        return {'files': len(items), 'physical': sum(item['physical'] for item in items),
                'nonempty': sum(item['nonempty'] for item in items)}
    result = {'method': 'UTF-8 splitlines; nonempty excludes whitespace-only lines, includes comments.',
              'excluded': ['runtimes and dependencies', 'build/dist', 'JSON and recorded results',
                           'examples and duplicate web/samples', 'documentation and SVG assets'],
              'total': total(records), 'product': total([item for item in records if item['category'] == 'product']),
              'tests': total([item for item in records if item['category'] == 'tests']),
              'languages': {language: total([item for item in records if item['language'] == language])
                            for language in sorted(set(EXTENSIONS.values()))}, 'files': records}
    (ROOT / 'docs/source-audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    rows = ['# Аудит исходников', '', 'Генерация: `python tests/source_audit.py`.', '',
            'Подсчёт физических и непустых строк, включая комментарии. Это метрика объёма, не качества.', '',
            '| Язык | Файлы | Строки | Непустые |', '|---|---:|---:|---:|']
    for language, value in result['languages'].items():
        rows.append(f"| {language} | {value['files']} | {value['physical']} | {value['nonempty']} |")
    for title, key in [('Продукт', 'product'), ('Тесты и инструменты', 'tests'), ('Всего', 'total')]:
        value = result[key]
        rows.append(f"| **{title}** | **{value['files']}** | **{value['physical']}** | **{value['nonempty']}** |")
    rows += ['', 'Не включены зависимости, runtime, сборка, JSON, записи прогонов, примеры, документация, SVG и копии Java в web/samples.', '',
             'CSS показан отдельно. Продукт превышает 12 000 непустых строк и без тестов. Разбивка по каждому файлу: `source-audit.json`.']
    (ROOT / 'docs/SOURCE-AUDIT.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('total', 'product', 'tests', 'languages')}, ensure_ascii=False, indent=2))
    assert result['product']['nonempty'] >= 12000
    return result

if __name__ == '__main__':
    audit()
