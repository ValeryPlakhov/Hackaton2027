# Перед сдачей

Готовые материалы:

- Исходный код и запуск: README.md, src/, web/, start-local.cmd, start.ps1, start.sh.
- Полная локальная веб-версия: http://localhost:8080 после запуска.
- Монолит: examples/LargeMonolith.java, 1052 строки, 51 метод.
- Обязательный scope и бонусы: examples/LanguageShowcase.java.
- Тесты: tests/test_api.py, результат docs/test-summary.json (22/22), пример docs/behavior-report.json (8/8).
- Архитектура и ограничения: docs/ARCHITECTURE.md, docs/SCOPE.md.
- Защита: docs/DEMO.md, output/pdf/Java-Blueprints-solution.pdf.
- Переносимый архив: output/Java-Blueprints-complete.zip, без JDK и внутренних служебных данных.

Для ссылки на GitHub создайте пустой репозиторий в своём аккаунте и загрузите этот каталог, исключив `.runtime/`, `build/`, `tmp/`, `.git/`, `.openai/`, `web/java-blueprints-source.zip` и архивы output. Правила локального .gitignore уже исключают исполняемую среду и временные файлы.

Если используете отдельную копию из ZIP:

```text
git init
git add .
git commit -m "Build Java Blueprints case solution"
git branch -M main
git remote add origin <URL вашего пустого репозитория>
git push -u origin main
```

Не используйте эти команды поверх служебного checkout Sites: для GitHub возьмите распакованный переносимый архив. В архиве нет Sites identity и чужих Git credentials.

Контакты и даты в исходном PDF - сведения организаторов. Мы не отправляли сообщения HR и не подавали решение от вашего имени. Перед сдачей проверьте официальный технический документ и финальный регламент: в переданном брифе они не раскрыты полностью.

Docker recipe и отдельный Docker runner подготовлены, но Docker в текущей среде отсутствовал. На защите используйте проверенный trusted local путь для своих примеров.
