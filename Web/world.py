import os
import csv
import re

def process_text(text):
    # "년", "년경"으로 나누기
    match = re.search(r'(\d+)~?(\d*)\s*년(?:경)?', text)
    if match:
        year = match.group(1)
        year2 = match.group(2)
        context = text[match.end():].replace('"', '').strip()
        return year, year2, context
    else:
        return None

def process_files(input_folder, output_folder):
    # 입력 폴더 내의 모든 CSV 파일 가져오기
    input_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    for input_file in input_files:
        input_filename = os.path.join(input_folder, input_file)

        # 파일 제목을 가져오기
        file_title = os.path.splitext(input_file)[0]

        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.readlines()

        for line in content:
            # 텍스트 처리
            processed_data = process_text(line)

            if processed_data:
                year, year2, context = processed_data

                # CSV 파일에 저장
                output_filename = os.path.join(output_folder, f"{file_title}.csv")
                with open(output_filename, 'a', encoding='utf-8', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)

                    # 파일이 비어있는 경우에만 헤더 쓰기
                    if os.path.getsize(output_filename) == 0:
                        csv_writer.writerow(['year', 'year2', 'context'])
                    
                    csv_writer.writerow([year, year2, context])

if __name__ == "__main__":
    input_folder = "./Web/world"  # 입력 폴더를 실제 폴더 경로로 바꿔주세요
    output_folder = "./Web/final"  # 출력 폴더를 원하는 폴더명으로 바꿔주세요

    # 결과 폴더 생성
    os.makedirs(output_folder, exist_ok=True)

    process_files(input_folder, output_folder)
