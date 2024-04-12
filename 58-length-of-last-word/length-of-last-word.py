class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Stringin sonundaki boşlukları temizle
        s = s.strip()
        
        # İndis değeri
        index = len(s) - 1
        
        # Son kelimenin uzunluğunu bulmak için sondan başlayarak karakterleri say
        while index >= 0 and s[index] != ' ':
            index -= 1
        
        # Son kelimenin uzunluğunu döndür
        return len(s) - index - 1