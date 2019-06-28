int trap(int* height, int size) {
    #define MAX(a, b) (((a) > (b)) ? (a) : (b))
    
    if (size == 0)
        return 0;
    
    int maxH = -1, first_peak = -1, last_peak = -1;

    for(int i = 0; i < size; i++) {
        if (height[i] > maxH) {
            first_peak = i;
            maxH = height[i];
        }
        if (height[i] == maxH) {
            last_peak = i;
        }
    }
        
    int water = 0, last_max = 0;

    for(int i = 0; i < first_peak; i++) {
        last_max = MAX(height[i], last_max);
        water += last_max - height[i];
    }

    for(int i = first_peak; i < last_peak; i++)
        water += maxH - height[i];

    last_max = 0;
    for(int i = size - 1; i > last_peak; i--) {
        last_max = MAX(height[i], last_max);
        water += last_max - height[i];
    }

    return water;
}

