"""
Time Conversion
"""


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # input: s format : hh:mm:ssAM or hh:mm:ssPM  (12-hour AM/PM)
    # return: 24-hour format. hh:mm:ss

    # separar horas, min, seg y formato

    #
    form = s[8:]
    hora = s[0:2]
    #print(hora)
    if form == 'AM':
        if hora == '12':
            # h='00'
            hora = '00'
        #else:
            #
    elif form == 'PM':
        if hora != '12':
            numhr = int(hora) + 12
            hora = str(numhr)

    # concatenar nueva hora con resto
    out = hora+':'+s[3:8]
    return(str(out))

