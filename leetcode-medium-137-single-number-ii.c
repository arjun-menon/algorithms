int singleNumber(int* nums, int numsSize) {
    int w = 8 * sizeof(int);
    unsigned int bits[w];
    for (int i = 0; i < w; i++)
        bits[i] = 0;
    
    int mask = 1;
    for (int i = w - 1; i >= 0; i--) {
        for (int p = 0; p < numsSize; p++) {
            int k = nums[p];
            if (k & mask)
                bits[i] += 1;
        }
        mask <<= 1;
    }

    int result = 0;
    for (int i = 0; i < w; i++) {
        // printf("%d ", bits[i]);
        result <<= 1;
        if (bits[i] % 3 != 0)
            result |= 1;
    }

    return result;
}
