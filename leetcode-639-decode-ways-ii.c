const uint64_t M = 1000000007;

const char *str = "";
uint64_t *mem;

uint64_t decode(int i) {
    if (mem[i] > 0)
        return mem[i] - 1;

    const char a = str[i];
    if (!a)
        return 1;
    const char b = str[i + 1];

    uint64_t ways = 0;

    if (a != '0') {
        if (a == '*')
            ways = (ways + 9 * decode(i + 1)) % M;
        else
            ways = (ways + decode(i + 1)) % M;
    }
    if (b) {
        if (a == '*') {
            if (b >= '0' && b <= '6' )
                ways = (ways + 2 * decode(i + 2)) % M;
            else if (b > '6' && b <= '9')
                ways = (ways + 1 * decode(i + 2)) % M;
            else if (b == '*')
                ways = (ways + 15 * decode(i + 2)) % M;
        }
        else {
            if (b != '*') {
                if (a == '1' || (a == '2' && ((b >= '0' && b <= '6' ))))
                    ways = (ways + decode(i + 2)) % M;
            }
            else {
                if (a == '1')
                    ways = (ways + 9 * decode(i + 2)) % M;
                else if (a == '2')
                    ways = (ways + 6 * decode(i + 2)) % M;
            }
        }
    }

    mem[i] = ways + 1;
    return ways;
}

int numDecodings(char* s) {
    str = s;
    mem = calloc(strlen(s) + 1, sizeof(uint64_t));
    return decode(0);
}
