def cleanHexCodes(decimal):
        
        limitedDecimal = limitRange(decimal, 0, 255)
            
        hexcodeRaw = hex(limitedDecimal)
        if "0x" in hexcodeRaw :
          singleCharHexCode = hexcodeRaw.replace("0x","")

        if len(singleCharHexCode) < 2:
              print("true")
              singleCharHexCode = "0" + singleCharHexCode 
        return singleCharHexCode

def limitRange(decimal, low, high):
        if decimal > high:
            decimal =high
        if decimal < low:
            decimal = low
        return decimal

def rgb(r, g, b):
        answer = cleanHexCodes(r) + cleanHexCodes(g) + cleanHexCodes(b)
        return answer.upper()

print(rgb(255,300,9))
