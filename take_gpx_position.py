import sys
import re

def extract_coordinates_from_gpx(gpx_file, output_file):
    # 讀取GPX檔案內容，指定編碼為UTF-8
    with open(gpx_file, 'r', encoding='utf-8') as file:
        gpx_content = file.read()

    # 使用正則表達式找到座標
    pattern = r'lat="([-+]?\d+\.\d+)" lon="([-+]?\d+\.\d+)"'
    matches = re.findall(pattern, gpx_content)

    # 將座標儲存到.TXT檔案
    with open(output_file, 'w') as f:
        for match in matches:
            f.write(match[0] + ',' + match[1] + '\n')

    print("座標已儲存到", output_file, "檔案中。")

# 檢查命令行參數數量
if len(sys.argv) != 3:
    print("請提供正確的命令行參數。")
    print("使用方式：python extract_coordinates.py gpx_file output_file")
else:
    gpx_file = sys.argv[1]
    output_file = sys.argv[2]
    extract_coordinates_from_gpx(gpx_file, output_file)