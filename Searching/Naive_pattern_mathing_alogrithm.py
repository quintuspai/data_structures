def naive_pattern_matching(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    for i in range(text_len - pattern_len):
        j = 0
        while j < pattern_len:
            if text[i + j] != pattern[j]:
                break
            j += 1
        
        if j == pattern_len:
            print("Pattern present at {}".format(i))

if __name__ == '__main__':
    text = 'AABAACAADAABAAABAA'
    pattern = 'AABA'
    naive_pattern_matching(text, pattern)
    