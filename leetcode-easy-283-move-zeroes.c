void moveZeroes(int* nums, int numsSize) {
    int w = 0;
    for (int i = 0; i < numsSize; i++) {
        while (nums[i] == 0)
            i++;
        if (i < numsSize)
            nums[w++] = nums[i];
    }
    while(w < numsSize) nums[w++] = 0;
}
