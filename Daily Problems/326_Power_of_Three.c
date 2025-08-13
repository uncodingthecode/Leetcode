bool isPowerOfThree(int n) {
    // all powers of 3 are factors of 3^19
    int max = (int)pow(3, 19);
    return n > 0 && max % n == 0;
}
