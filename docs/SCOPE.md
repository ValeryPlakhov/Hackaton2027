# Матрица соответствия краткому брифу

| Критерий | Что демонстрировать | Проверка / граница |
|---|---|---|
| Java-монолит около 1000 строк | `LargeMonolith.java`, 1052 строки, 51 метод | Интеграционный тест 15: parse → optimize → compile → compare |
| Загрузка .java | Мультизагрузка UTF-8, файловые вкладки | Воспроизводимо в локальном интерфейсе; простые имена файлов |
| Разбор кода | Стандартный AST javac | Синтаксические ошибки с номером строки |
| Визуальная модель | Узлы методов/инструкций/условий/циклов | Структурная проекция; сложный exception flow не точный CFG |
| Двусторонняя синхронизация | Java auto-parse; узел → span edit → Java | Условие, инструкция, вставка/удаление; произвольная коммутация рёбер не поддержана |
| Пользовательские классы/интерфейсы | LanguageShowcase / Scorer / InvalidValue | Реальный javac, несколько top-level классов |
| Примитивы, обёртки, массивы | `int`, `boolean`, `double`, `Integer`, `int[]` | Компиляция и запуск showcase |
| Арифметика, логика, сравнение, cast | Showcase: `&&`, `!=`, `>=`, `(int)`, `(double)` | Тест 2 |
| if/else, switch, циклы | Граф `flow`, `countPairs` | for/foreach/while/do, switch statement и expression сохраняются |
| break/continue/return | Граф `flow` | Немеченые переходы; метки показаны непрозрачным блоком |
| Методы, конструкторы, поля, static | LanguageShowcase и все примеры | Компиляция поддерживает; граф показывает тела методов |
| try/catch/finally, throw | Showcase checked(), flow() | Граф структурный с консервативными exception edges |
| Object, String, Math, System | Showcase и PairAnalyzer | Стандартная библиотека JDK, без собственного эмулятора |
| System.in/out/err | Все тесты gate | stdout/stderr сравниваются раздельно и точно |
| Scanner, Formatter, format/printf | Showcase / PairAnalyzer | UTF-8 и кириллица проходят реальное выполнение |
| Коллекции java.util | List/Set/Map, ArrayList, LinkedList, HashSet/TreeSet, HashMap/TreeMap | Showcase выполняется на 4 входах |
| Iterable/Collection/Iterator | Showcase | Java type-check + выполнение |
| Collections/Arrays/Comparator/Optional | Showcase | Java type-check + выполнение |
| List.of/Set.of/Map.of | Showcase | Java type-check + выполнение |
| Проверяемые исключения и throws/catch | InvalidValue, IOException | javac проверяет обязательную обработку |
| Unchecked исключения | JVM поведение; неверные исходники отклоняются | Система не перехватывает пользовательские исключения в серверной JVM |
| record, enum, generics, lambda, Stream | Score, Mode, first<T>, scores | Бонусный scope компилируется и сохраняется |
| Дефекты и Big O | Диагноз с line/span, переход к графу | Правила эвристические, без ложного обещания полного статанализа |
| Оптимизация | Чистый pair counter → histogram | Узкий AST-предикат, случайные входы, негативный тест с побочным эффектом |
| Декомпозиция | Static method → helper-файл + delegate | Зависимости проверяются компиляцией; не произвольная нарезка монолита |
| Сохранение поведения | Реальные раздельные сборки и JVM | stdout + stderr + exitCode, не доказательство для всех входов |
| Исходный код и инструкция | src/, web/, README, launch scripts | Ноль библиотечных зависимостей, JDK 21 |
| Веб-демо/сборка | Localhost полная версия, Docker recipe, Sites обзор | Sites без живой JVM, честная метка; Docker не проверен здесь |
| Автотесты и результаты | tests/, docs/test-summary.json, behavior-report.json | Отчёты создаются реальным прогоном |
| Архитектура, scope, ограничения | Этот файл и ARCHITECTURE.md | Полный дополнительный технический документ отсутствует |

Критерии в переданном PDF обозначены как проект: веса и финальную шкалу организаторы утверждают отдельно. Нельзя обоснованно обещать конкретное число баллов или получение 75000 рублей.
