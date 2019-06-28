const char *str = "";
int *mem;

int decode(int i) {
    if (mem[i] > 0)
        return mem[i] - 1;

    const char a = str[i];
    if (!a)
        return 1;
    const char b = str[i + 1];

    int ways = 0;

    if (a != '0')
        ways += decode(i + 1);
    if (b && (a == '1' || (a == '2' && ((b >= '0' && b <= '6' )))))
        ways += decode(i + 2);

    mem[i] = ways + 1;
    return ways;
}

int numDecodings(char* s) {
    str = s;
    mem = calloc(strlen(s) + 1, sizeof(int));
    return decode(0);
}
