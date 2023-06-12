from subprocess import Popen, PIPE


hwp_file_path = '/Users/msun/Desktop/김만덕기념관.hwp'
process = Popen(['hwp5txt', hwp_file_path], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
data = stdout.decode('utf-8')

# Split the text into paragraphs
paragraphs = data.split('\n\n\n')

# Remove empty values and paragraphs with length <= 5
filtered_paragraphs = []
for paragraph in paragraphs:
    paragraph = paragraph.strip().replace('<그림>', '').replace('<표>', '')
    if len(paragraph) > 5:
        filtered_paragraphs.append(paragraph.strip())

