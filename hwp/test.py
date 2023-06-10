import olefile
import pandas as pd
import chardet

# HWP 파일 경로 설정
hwp_file_path = '/Users/msun/Desktop/김만덕기념관.hwp'

# 스트림 내용을 저장할 딕셔너리
stream_contents = {}

# HWP 파일 열기
with olefile.OleFileIO(hwp_file_path) as ole:
    #PrvText 스트림 내의 내용을 읽기
    encoded_text = ole.openstream('PrvText').read() 
    #인코딩된 텍스트를 UTF-16으로 디코딩
    decoded_text = encoded_text.decode('UTF-16')
    print(decoded_text)
    list_df = pd.DataFrame(items)