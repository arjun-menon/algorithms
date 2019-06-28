int removeDuplicates(int* nums, int numsSize) {
    if (!numsSize)
        return 0;
    int pos = 0;
    int val = nums[0];
    for(int i=1; i<numsSize; i++)
        if (nums[i] > val)
            nums[++pos] = val = nums[i];
    return pos + 1;
}
