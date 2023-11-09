from subprocess import Popen, PIPE
 
file =  '/Users/msun/Desktop/김만덕기념관.hwp'
process = Popen(['hwp5txt', file], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
data = stdout.decode('utf-8')
print(data)