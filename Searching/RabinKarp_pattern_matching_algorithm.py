def rabin_karp(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    d = 10
    p = 0
    t = 0
    h = 1
    mod = 13
    for i in range(pattern_len - 1):
        h = (h * d) % mod
    for i in range(pattern_len):
        p = (d * p + ord(pattern[i])) % mod
        t = (d * t + ord(text[i])) % mod
    for i in range(text_len - pattern_len + 1):
        if p == t:
            for j in range(pattern_len):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == pattern_len:
                print("Pattern found at ",i+1)
        if i < (text_len - pattern_len):
            t = (d * (t - ord(text[i]) * h) + ord(text[i + pattern_len])) % mod
            if t < 0:
                t = t + mod
    
    
if __name__ == '__main__':
    text = "AAABCAAAAABABABCB"
    pattern = "ABC"
    rabin_karp(text, pattern)