int main() {
    int i;
    string words = "HCS; Data Structures and Algorithms";
    string * wordsPtr = & words;
    char * charPtr;

    cout << sizeof(words) << endl;
    for (i=0; i<sizeof(words); i++) {
        charPtr = reinterpret_cast<char*>(wordsPtr);
        cout << hex << reinterpret_cast<long>(charPtr + i) << dec << " ";
        cout << bitset<8>(*(charPtr + i)) << " ";
        cout << +(*(charPtr + i)) << " ";
        cout << *(charPtr + i) << " ";
        cout << *(wordsPtr + i) << endl;
    }
}