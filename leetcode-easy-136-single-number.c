int singleNumber(int* nums, int numsSize) {
    register int r = 0;
    while(numsSize--)
        r ^= *nums++;
    return r;
}
