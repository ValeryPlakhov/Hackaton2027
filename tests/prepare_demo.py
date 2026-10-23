"""Build an honest hosted demo from actual ASTs and a real differential run."""
import json
from pathlib import Path
from test_api import post, compare, method, PAIR, ROOT

INPUTS=['0\n','1\n7\n','5\n1 2 1 2 1\n','6\n-3 0 -3 2147483647 -2147483648 0\n','-1\n','8\n4 4 4 4 4 4 4 4\n','4\n1 2\n','10\n0 1 2 3 4 5 6 7 8 9\n']
before=post('analyze',{'source':PAIR})
optimized=post('optimize',{'source':PAIR,'methodId':method(before,'countPairs')['id']})['source']
after=post('analyze',{'source':optimized})
report=compare({'PairAnalyzer.java':PAIR},{'PairAnalyzer.java':optimized},INPUTS)
assert report['passed'], report
out={'before':{'files':{'PairAnalyzer.java':PAIR},'model':before},'after':{'files':{'PairAnalyzer.java':optimized},'model':after},'report':report}
(ROOT/'web/demo.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'docs/behavior-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print('Demo generated from real JVM:',len(report['tests']),'passed inputs')
