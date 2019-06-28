void moveZeroes(int* nums, int numsSize) {
    int w = 0;
    for (int i = 0; i < numsSize; i++) {
        while (nums[i] == 0)
            i++;
        if (i < numsSize) {
            if (w < i) nums[w] = nums[i];
            w++;
        }
    }
    while(w < numsSize) nums[w++] = 0;
}
