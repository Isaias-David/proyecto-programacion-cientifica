class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()  # Ordenar ambición de niños
        s.sort()  # Ordenar tamaño de galletas
        
        child_ptr = 0
        cookie_ptr = 0
        
        while child_ptr < len(g) and cookie_ptr < len(s):
            # Criterio codicioso: si la galleta satisface al niño, se la asignamos
            if s[cookie_ptr] >= g[child_ptr]:
                child_ptr += 1
            # Siempre pasamos a la siguiente galleta
            cookie_ptr += 1
            
        return child_ptr