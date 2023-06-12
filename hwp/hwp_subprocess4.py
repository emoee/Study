import csv
from subprocess import Popen, PIPE
import os

# 입력 폴더와 출력 파일 경로 설정
input_folder = '/Users/msun/Desktop/줄글'  # 입력 폴더 경로
output_file = './hwp/output.csv'  # 출력 파일 경로

# CSV 파일에 저장할 데이터 리스트
data_rows = []
title_row = ['관광지명', '이동약자 안내']
data_rows.append(title_row)

# 입력 폴더 내의 모든 HWP 파일에 대해 처리
for filename in os.listdir(input_folder):
    process = Popen(['hwp5txt', os.path.join(input_folder, filename)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    data = stdout.decode('utf-8')

    # Split the text into paragraphs
    paragraphs = data.split('\n\n')

    # Remove empty values and paragraphs with length <= 5
    filtered_paragraphs = [''] * 3
    cnt = 1
    for paragraph in paragraphs:
        paragraph = paragraph.strip().replace('<그림>', '').replace('<표>', '')
        if cnt == 1:
            filtered_paragraphs[0] = paragraph.strip()
            cnt += 1
        if len(paragraph) > 5 and "이동약자를 위한 안내 :" in paragraph:
            filtered_paragraphs[2] = paragraph.strip()

    # Append the filtered paragraphs to the data rows
    data_rows.append(filtered_paragraphs)

# CSV 파일로 데이터 저장
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data_rows:
        writer.writerow(row)

print(f'Data saved to {output_file}')
