"""Vector, Cyrillic-safe defense handout, generated from verified reports."""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
FONT=Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('UI',str(FONT/'segoeui.ttf')))
pdfmetrics.registerFont(TTFont('Bold',str(FONT/'seguisb.ttf')))
pdfmetrics.registerFont(TTFont('Code',str(FONT/'consola.ttf')))
summary=json.loads((ROOT/'docs/test-summary.json').read_text(encoding='utf-8'))
report=json.loads((ROOT/'docs/behavior-report.json').read_text(encoding='utf-8'))
assert summary['passed'] and report['passed'], 'Deliver only verified results'
W,H=1280,720
c=canvas.Canvas(str(OUT/'Java-Blueprints-solution.pdf'),pagesize=(W,H))
c.setTitle('Java Blueprints - решение кейса AXENIX')
c.setAuthor('Java Blueprints')
BG='#0c111b'; PANEL='#141e2d'; BORDER='#2b3b52'; TEXT='#e0e8f7'; MUTED='#8e9eb7'; ACCENT='#a0acff'; GREEN='#68d9b2'; AMBER='#e0bb78'
page=0
def text(x,y,s,size=18,color=TEXT,font='UI'):
    s=str(s).replace('–','-').replace('—','-').replace('\u2011','-')
    c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,H-y,s)
def para(x,y,s,width,size=17,color=MUTED,leading=None,font='UI'):
    leading=leading or size*1.55
    for line in simpleSplit(s,font,size,width):text(x,y,line,size,color,font);y+=leading
    return y
def box(x,y,w,h,fill=PANEL,stroke=BORDER,r=12):
    c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(stroke));c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=1)
def line(x1,y1,x2,y2,color=BORDER):
    c.setStrokeColor(HexColor(color));c.setLineWidth(1);c.line(x1,H-y1,x2,H-y2)
def start(kicker,title,sub=''):
    global page
    page+=1;c.setFillColor(HexColor(BG));c.rect(0,0,W,H,fill=1,stroke=0)
    text(56,42,'B / BLUEPRINTS',12,ACCENT,'Bold');text(980,42,'AXENIX · ENGINEERING CASE',10,MUTED)
    text(56,96,kicker,10,ACCENT,'Bold');text(56,148,title,34,TEXT,'Bold')
    if sub:para(58,185,sub,1120,16)
    line(56,670,1224,670);text(56,696,'JAVA 21  /  SOURCE → AST → GRAPH → JAVA → JVM',9,MUTED);text(1148,696,f'{page:02d} / 09',10,MUTED)
def end():c.showPage()
def bullet(x,y,title,detail,width=500):
    text(x,y,'•',20,ACCENT);text(x+23,y,title,18,TEXT,'Bold');return para(x+23,y+30,detail,width-23,15)+24
def code(x,y,s,size=15,color='#b8d4f4'):
    for row in s.splitlines():text(x,y,row,size,color,'Code');y+=size*1.6
    return y
def arrow(x,y):text(x,y,'→',26,ACCENT)

start('01 / РЕШЕНИЕ','Java. Видеть. Менять. Проверять.','Воспроизводимый инструмент для анализа и преобразования Java-монолита с проверкой наблюдаемого поведения.')
text(58,284,'Один исходник. Два представления.',33,TEXT,'Bold')
para(58,330,'Настоящий AST javac связывает код и визуальную модель. Любое изменение проходит отдельную компиляцию и сравнение вывода обеих версий.',700,20)
for x,big,label in [(58,'1052','строки в тестовом монолите'),(454,str(summary['tests']),'интеграционных сценария'),(850,'0','внешних библиотек / API-ключей')]:
    box(x,475,372,130);text(x+24,532,big,40,ACCENT,'Bold');text(x+24,570,label,15,MUTED)
end()

start('02 / АРХИТЕКТУРА','Проверяемый путь от исходника до результата','HTML / CSS / JavaScript + Java 21. Сервер и стандартная библиотека JDK, без облачного AI в критическом контуре.')
for x,num,title,body in [(58,'01','JavaModel','JavacTask.parse()\nUTF-16 SourcePositions\nКлассы, методы, диагностики'),(459,'02','Граф и преобразования','GraphBuilder + Analyzer\nПравка исходного span\nОптимизация и extraction'),(860,'03','Runner / quality gate','Две независимые сборки\nНовая JVM для каждого stdin\nstdout + stderr + exitCode')]:
    box(x,270,362,230);text(x+24,312,num,13,ACCENT,'Bold');text(x+24,356,title,23,TEXT,'Bold');
    for i,s in enumerate(body.splitlines()):text(x+24,403+i*29,s,16,MUTED)
arrow(429,390);arrow(831,390)
box(58,540,1164,82);para(82,573,'Истина - Java-текст. Граф хранит точные диапазоны. После правки код повторно разбирается; нетронутые комментарии и форматирование сохраняются.',1110,17)
end()

start('03 / ДВУСТОРОННЯЯ СВЯЗЬ','Изменение узла становится изменением Java','Условия, инструкции и выражения редактируются по исходным диапазонам. Нет промежуточного игрушечного языка.')
box(58,256,556,345);text(80,294,'JAVA / classify()',12,ACCENT,'Bold')
code(82,343,'static String classify(int n) {\n    if (n == 0) {\n        return "пустой набор";\n    }\n    return "другой набор";\n}',18)
for x,y,label,fill,stroke in [(737,260,'method / classify(n)',PANEL,'#617bb5'),(737,370,'if / n == 0','#2b2318','#8b713f'),(686,496,'return "пустой набор"','#122a25','#36705c'),(974,496,'return "другой набор"','#122a25','#36705c')]:
    bw=315 if y<496 else 248;box(x,y,bw,62,fill,stroke,8);text(x+17,y+38,label,14,TEXT,'Code')
line(895,322,895,370,'#7488ad');line(850,432,810,496,'#b39b62');line(947,432,1095,496,'#b39b62');text(795,468,'да',12,MUTED);text(1050,468,'нет',12,MUTED)
para(686,605,'Произвольная перекоммутация рёбер не поддерживается. Перемещение узла меняет раскладку.',530,14)
end()

start('04 / ОПТИМИЗАЦИЯ','Из двух вложенных обходов - индекс частот','Автозамена доступна только для точного чистого AST-шаблона подсчёта упорядоченных равных пар в int[].')
box(58,257,550,270);text(82,296,'ДО / O(n²)',14,AMBER,'Bold');code(82,341,'int matches = 0;\nfor (int a : values) {\n    for (int b : values) {\n        if (a == b) matches++;\n    }\n}\nreturn matches;',16)
box(637,257,585,270);text(661,296,'ПОСЛЕ / O(n), СРЕДНЕЕ',14,GREEN,'Bold');code(661,341,'Map<Integer, Integer> freq = new HashMap<>();\nfor (int x : values)\n    freq.merge(x, 1, Integer::sum);\nint matches = 0;\nfor (int f : freq.values()) matches += f * f;\nreturn matches;',15)
text(60,576,'pairs = sum(f(v) * f(v))',23,ACCENT,'Code')
para(58,614,'Сохранены самопары и модульная int-арифметика. Цена: O(k) памяти. Сторонние эффекты в теле отклоняют шаблон.',1160,15)
end()

start('05 / QUALITY GATE','Зелёный статус появляется после выполнения','Сравниваются хеши исходных байтов stdout и stderr и код завершения; UTF-8 используется для отображения.')
box(58,258,560,322);text(82,303,'РЕАЛЬНЫЙ ДЕМОНСТРАЦИОННЫЙ ПРОГОН',11,ACCENT,'Bold')
for i,label in enumerate(['Пустой набор / один элемент','Повторяющиеся и разные значения','Отрицательные числа / границы int','Некорректный размер / неполный ввод']):text(84,352+i*43,'[OK]  '+label,17,GREEN)
text(84,550,f"{len(report['tests'])} / {len(report['tests'])} входов: поведение совпало",21,TEXT,'Bold')
y=285
y=bullet(665,y,'Отдельная JVM','Каждый тест получает новый процесс и закрытый после передачи stdin.',520)
y=bullet(665,y,'Нет ложного PASS','Ошибка сборки, таймаут и лимит вывода отклоняют проверку.',520)
y=bullet(665,y,'Честный FAIL','Условие n == 0 → n == 1 меняет результат; gate обнаруживает это.',520)
para(58,622,'Конечный набор входов подтверждает поведение на этих данных. Это не формальное доказательство эквивалентности всех Java-программ.',1164,15,AMBER)
end()

start('06 / ДЕКОМПОЗИЦИЯ','Выделение ответственности с проверкой зависимостей','Независимый static-метод переносится в BlueprintFunctions.java; исходная сигнатура сохраняется через delegate.')
box(58,263,531,230);text(82,304,'PairAnalyzer.java',18,ACCENT,'Code');code(82,351,'static int countPairs(int[] values) {\n    return BlueprintFunctions\n        .countPairs(values);\n}',17)
box(632,263,590,230);text(656,304,'BlueprintFunctions.java',18,GREEN,'Code');code(656,351,'final class BlueprintFunctions {\n    static int countPairs(int[] values) {\n        // перенесённая реализация\n    }\n}',17)
arrow(598,385)
box(58,532,1164,95);para(82,568,'Сначала компилируется весь проект. Поле или приватный тип, недоступные из helper, отклоняют перенос. Затем нужен quality gate: успешная сборка сама по себе не доказывает сохранение поведения.',1110,17)
end()

start('07 / ВЕРИФИКАЦИЯ','Проверены успехи и отказные сценарии','Интеграционные тесты обращаются к реальному HTTP API, компилятору и дочерним JVM. Без mock-runner.')
items=[('Язык и модель','Классы, интерфейсы, циклы, switch, коллекции, checked exceptions, record, generics, lambda, Stream.'),('Правки и преобразования','UTF-16 с emoji, no-op round trip, редактирование условия, вставка/удаление, extraction и отказ из-за поля.'),('Сохранение поведения','Случайные массивы с seed 75000, пустые данные, отрицательные числа, границы int, stdout/stderr/exitCode.'),('Защита от ложного результата','Ошибка компиляции, бесконечный цикл, flood вывода, разные raw bytes, пустой набор входов, traversal и чужой Origin.')]
for i,(title,detail) in enumerate(items):
    x=58+(i%2)*596;y=260+(i//2)*179;box(x,y,568,156);text(x+22,y+39,title,19,TEXT,'Bold');para(x+22,y+76,detail,520,15)
text(59,642,f"{summary['tests']} / {summary['tests']} сценариев: PASS. Монолит: 1052 строки, 51 метод.",18,GREEN,'Bold')
end()

start('08 / ГРАНИЦЫ','Результат можно проверить и воспроизвести','Сильное решение явно отделяет реализованные гарантии от следующих этапов разработки.')
left=[('Полная Java-семантика','Код исполняется стандартной JVM. Граф - структурная проекция, а не альтернативный интерпретатор.'),('Big O - эвристика','Линейность циклов предполагается. Вызовы и фактические границы требуют отдельного анализа.'),('Не универсальный рефакторинг','Один строгий rewrite-шаблон и перенос независимых static-методов; произвольный граф не генерируется.')]
right=[('Exception flow','Try/catch/finally, метки и сложные выражения сохраняются; CFG не моделирует все исключительные переходы.'),('Trusted local ≠ sandbox','Локальный runner запускает свои исходники. Docker runner подготовлен, но здесь не проверен.'),('Развёрнутый Sites = обзор','Сохранённые AST и реальные результаты явно помечены. Для произвольного Java нужна локальная JVM.')]
for col,items in enumerate([left,right]):
    y=276
    for title,detail in items:y=bullet(58+col*599,y,title,detail,540)
end()

start('09 / ЗАПУСК И ЗАЩИТА','От папки проекта до живого демо - одна команда','Без Maven, npm, ключей API и внешних сервисов во время демонстрации.')
box(58,265,1164,104);text(84,305,'WINDOWS',10,ACCENT,'Bold');code(84,345,'.\\start.ps1 -TrustedLocal     →     http://localhost:8080',22)
for i,(title,body) in enumerate([('01 / Показать проблему','Импорт монолита → countPairs → два вложенных цикла и диагноз.'),('02 / Улучшить и проверить','Оптимизация → новый граф → 8 реальных входов → PASS.'),('03 / Показать честный отказ','Правка n == 0 на n == 1 → FAIL → отмена → extraction → экспорт.')]):
    y=420+i*72;text(60,y,title,17,TEXT,'Bold');para(395,y,body,815,16)
para(59,644,'Материалы: README.md · docs/ARCHITECTURE.md · docs/SCOPE.md · docs/DEMO.md · исходники · автотесты · JSON-отчёты.',1160,14,ACCENT)
end()
c.save()
print(OUT/'Java-Blueprints-solution.pdf')
