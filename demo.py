from struct import *

packed_data = pack('abc',1,1.5)
print(unpack('abc',packed_data))