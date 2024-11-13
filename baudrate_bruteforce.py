import serial
# Useless script wrote for a shitty device 
for i in range(115200, -1, -1):
#for i in range(0, 20):
    port = serial.Serial('/dev/ttyUSB0', i)
    out_file=open('serial.log', 'ab')
    data = port.read(size=100)
    message = "\n############### BruteForcing with baudare: `" + str(i) + "` \###############\n\n"
    out_file.write(message)
    out_file.write(data)

    print message
    print data
port.close()
out_file.close()
