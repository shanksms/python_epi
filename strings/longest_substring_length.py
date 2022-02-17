
def lengthOfLongestSubstring(s: str) -> int:
    if s == '':
        return 0
    l = []
    for i in range(len(s)):
        st = list()
        for j in range(i, len(s)):
            if not s[j] in st:
                st.append(s[j])
            else:
                break
        l.append(''.join(st))


    l = sorted(l, key=lambda x: len(x), reverse=True)
    return len(l[0])

def lengthOfLongestSubstring_sliding_window(s: str) -> int:
    n = len(s)
    ans = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans


if __name__ == '__main__':
    #print(lengthOfLongestSubstring("au"))
    print(lengthOfLongestSubstring_sliding_window("abcabcd"))
    #print(lengthOfLongestSubstring("pwwkew"))