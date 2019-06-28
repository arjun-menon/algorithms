// Forward declaration of the knows API.
bool knows(int a, int b);

int findCelebrity(int n) {
    for (int a = 0; a < n; a++) { // celebrity
        bool celeb = true;
        for (int b = 0; b < n; b++) { // others
            if (a == b)
                continue;
            if (knows(a, b)) {
                celeb = false;
                break;
            }
            if (!knows(b, a)) {
                celeb = false;
                break;
            }
        }
        if (celeb)
            return a;
    }
    return -1;
}
