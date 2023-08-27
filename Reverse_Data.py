import hashlib

class Hash_Data:
    def __init__(self):
        self.user = "920427"
        self.password = "Ryin.2018"

    def WUTF(self, text):

        bk = []
        Byte = 0
        
        for i in range(len(text)):
            nums = ord(text[i])
            #print(nums)
            if 0x00 <= nums and nums <= 0x7f:
                Byte += 1
                bk.append(nums)
            elif 0x80 <= nums and nums <= 0x7ff:
                Byte += 2
                bk.append(192 | 31 & nums >> 6)
                bk.append(128 | 63 & nums)
            elif 0x800 <= nums and nums <= 0xd7ff or 0xe000 <= nums and nums <= 0xffff:
                Byte += 3
                bk.append(224 | 15 & nums >> 12)
                bk.append(128 | 63 & nums >> 6)
                bk.append(128 | 63 & nums)
            elif 0x10000 <= nums and nums <= 0x10ffff:
                Byte += 4
                bk.append(240 | 7 & nums >> 18)
                bk.append(128 | 63 & nums >> 12)
                bk.append(128 | 63 & nums >> 6)
                bk.append(128 | 63 & nums)
        
        for i in range(len(bk)):
            bk[i] &= 0xff
        
        if 1:
            return bk
        
        if Byte <= 0xff:
            return [0, Byte] + bk
        else:
            return [Byte >> 8, Byte & 0xff] + bk

    def To_Hex(self, otext):

        Byte = self.WUTF(otext)
        
        hex_str = "0123456789ABCDEF"
        hex = ""
        
        for i in range(len(Byte)):
            hex += hex_str[(Byte[i] & 0xf0) >> 4]
            hex += hex_str[(Byte[i] & 0x0f) >> 0]
        
        return hex

    def To_Query(self, params):

        str = ''
        
        for i in params:
            str += i + '=' + params[i] + '&'
        
        return str[:-1]
        
    def Data_Login(self):
   
        data = {
            "partnerId": self.user,
            "pwd": hashlib.md5(self.password.encode()).hexdigest()
        }
        
        result = self.To_Hex(self.To_Query(data))
        return result        
