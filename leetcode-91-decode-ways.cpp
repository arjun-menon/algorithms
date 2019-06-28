class Solution {
    const char *s = "";
    vector<int> *mem;

    int decode(int i=0) {
        if (mem->at(i) >= 0)
            return (*mem)[i];
        
        const char a = s[i];
        if (!a)
            return 1;
        const char b = s[i + 1];

        int ways = 0;

        if (a != '0')
            ways += decode(i + 1);
        if (b && (a == '1' || (a == '2' && ((b >= '0' && b <= '6' )))))
            ways += decode(i + 2);

        (*mem)[i] = ways;
        return ways;
    }
    
public:
    int numDecodings(string s) {
        this-> s = s.c_str();
        mem = new vector<int>(s.length() + 1, -1);
        return decode();
    }
};
