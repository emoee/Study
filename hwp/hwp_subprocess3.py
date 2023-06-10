from tika import parser

hwp_file_path = '/Users/msun/Desktop/김만덕기념관.hwp'

# Parse the HWP file and extract the content
parsed_data = parser.from_file(hwp_file_path)
content = parsed_data['content']

# Save the extracted content to a text file
output_file_path =  './hwp/output.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'HWP file content saved to: {output_file_path}')
