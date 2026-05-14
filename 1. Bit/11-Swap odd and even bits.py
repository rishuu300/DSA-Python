class Solution:
    def swapBits(self,n):
        # Hexadecimal Representation of 5 is 0101.
        # So, 8 times 5 is 32 bits of odd places as set bits.
        oddMask = 0x55555555
        
        # Hexadecimal representation of 10 is A which is 1010.
        # So, 8 timmes A is 32 bits of even places as set bits.
        evenMask = 0xAAAAAAAA
        
        oddBits = n & oddMask
        evenBits = n & evenMask
        
        oddBits = oddBits << 1
        evenBits = evenBits >> 1
        
        return oddBits | evenBits