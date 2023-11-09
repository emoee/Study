from subprocess import Popen, PIPE

hwp_file_path = '/Users/msun/Desktop/김만덕기념관.hwp'
output_file_path = './hwp/output.txt'

# HWP 파일을 텍스트로 변환
process = Popen(['hwp5txt', hwp_file_path], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
decoded_output = stdout.decode('utf-8')

# 변환된 텍스트를 문단 단위로 분리하여 저장
paragraphs = decoded_output.split('\n\n')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for paragraph in paragraphs:
        output_file.write(paragraph + '\n\n')

print(f'HWP file content saved to: {output_file_path}')
