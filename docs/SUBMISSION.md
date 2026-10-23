# Комплект для сдачи

`output/Java-Blueprints-complete.zip`: папка java-blueprints с полными src/web, launch scripts, tests, examples, docs, машиночитаемыми результатами, CI recipe и PDF. Без JDK, .git, runtime dependencies, build/dist и recursive ZIP.

| Файл | Назначение |
|---|---|
| README.md | Возможности, запуск, ограничения |
| examples/LargeMonolith.java | 1052 строки / 51 реально используемый метод |
| examples/LanguageShowcase.java | Основной и бонусный Java scope |
| tests/verify.py | 166 автоматических проверок одной командой |
| docs/verification-summary.json | Итог полного локального прогона |
| docs/source-audit.json | Авторский код с разбивкой по файлам |
| docs/studio-reference-results.json | Реальные измерения и результаты |
| web/studio-demo.json | Полные записанные AST, samples, reports и environment |
| docs/ARCHITECTURE.md, API.md, SCOPE.md | Устройство, контракт, соответствие кейсу |
| docs/DEMO.md | Живая защита и ответы на вопросы |
| output/pdf/Java-Blueprints-solution.pdf | Визуальный материал для защиты |

Studio 2 поставляется только локальным комплектом по выбору владельца. Полная версия находится в архиве; для защиты используйте локальный запуск. Существующий Site https://java-blueprints-lab.husainov-565.chatgpt.site содержит предыдущую версию и не обновлялся; его аудитория не изменялась.

Архив: `python tests/package_solution.py`. Записи: живой trusted-local сервер + `python tests/prepare_studio_demo.py`. PDF: ReportLab и Windows Segoe UI/Consolas (зависимости авторинга, не приложения).

Дополнительный техдок, упомянутый в исходном кейсе, не предоставлен. Scope сопоставлен с переданным PDF. Автоматической отправки организаторам не выполнялось.
