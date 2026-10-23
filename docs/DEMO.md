# Защита за пять минут

Подготовка: JDK21, start-local.cmd, localhost:8080. Local full workflow не зависит от интернета. На Site RECORDED означает запись реального запуска.

1. **0:00 — Монолит.** «Визуальная модель должна быть связана с настоящим кодом». Monolith / 1K, 1052 строки / 51 метод. Выбрать countPairs, открыть canvas: два вложенных цикла, source↔node, O(n²). Pan/zoom меняет layout, не программу.
2. **0:45 — Объяснимый план.** Рефакторинг и diff → Просмотреть патч. Для значения частоты f исходник считает f² упорядоченных пар. Показать before/after, допущения, hash. Применить и проверить → gate 8/8, хеши версий, фактический stdout. «Конечные входы — проверка, не универсальное доказательство».
3. **1:45 — Измерения и тесты тестов.** Test Lab → Бенчмарк → countPairs, 128/1024/4096. Малый n может проиграть из-за HashMap. Старт JVM вне таймера, harness не JMH. Mutation меняет операторы и показывает killed/survived/invalid. Score не line coverage.
4. **2:45 — Ошибка и контрпример.** Открыть исходный Pair Analyzer, заменить a == b на a != b. Gate FAIL. Контрпример → n+n int вход → уменьшить. Показать меньший stillFails и реальные outputs. Глобальный минимум не обещается.
5. **3:45 — Восстановление и архитектура.** History/checkpoint; старый зелёный gate после восстановления не возвращается. Выделить независимый static-метод в helper, повторить gate, показать связь в Architecture. При наличии времени Text Pipeline → StringBuilder rewrite.
6. **4:30 — Сдача.** Evidence ZIP содержит обе версии, stdin, hashes, patch и автономный HTML. SARIF/SVG/Mermaid/DOT отдельно. Режим защиты или PDF, verification-summary 166/166, source audit >12k продукта без deps/fixtures/docs.

## Ответы жюри

| Вопрос | Ответ |
|---|---|
| Парсер на regex? | javac AST; lexer нужен только подсветке. |
| Любой граф → Java? | Структурные правки существующего AST, без произвольных рёбер. |
| Полная эквивалентность? | Только наблюдаемые raw stdout/stderr/exitCode на выбранных входах. |
| 100% mutation — полные тесты? | Доля killed среди выбранных valid mutants. |
| Почему без React/Maven? | JDK достаточно для живого демо; чистые ES-модули тестируются отдельно. |
| Недоверенный код? | Trusted local не sandbox; Docker-путь подготовлен, но не проверен. |
| Что на Site? | UI и помеченные записи запусков; JVM локально. |
| Следующий шаг? | Attributed calls/data flow, exceptional CFG, JMH, проверенная sandbox infrastructure, durable jobs. |
