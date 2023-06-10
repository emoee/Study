import olefile 
 
f = olefile.OleFileIO('/Users/msun/Desktop/김만덕기념관.hwp') # HWP 파일 열기
encoded_text = f.openstream('PrvText').read() # PrvText 스트림의 내용 꺼내기
decoded_text = encoded_text.decode('UTF-16') # 유니코드를 UTF-16으로 디코딩
print(decoded_text)