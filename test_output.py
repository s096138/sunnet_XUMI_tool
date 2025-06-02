from calendar import c
from test_main import main
from datetime import datetime

import re
nowdatetime = datetime.now().strftime("%Y%m%d%H%M")

def remove_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1B\[[0-?9;]*[mK]') #"\x1B[31m格式\x1B[0m"
    return ansi_escape.sub('', text)

def test_output(capfd):
    result = main()
    captured = capfd.readouterr()
    clean_output = remove_ansi_escape_codes(captured.out)
    print("Captured Output:", clean_output.strip()) #pytest只在失敗時輸出
    
    # 將輸出寫入文件
    with open(f"{nowdatetime}自動化測試.txt", "a") as f:
        f.write(clean_output.strip() + "\n\n")

    assert result == "result"