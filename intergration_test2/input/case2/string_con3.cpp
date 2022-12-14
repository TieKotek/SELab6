# include <iostream>
# include <cstring>

using namespace std;

int main() {
    char a[30];
    char b[30];
    scanf("%s", a);
    scanf("%s", b);
    printf("%s\n",strcat(a, b));
    return 0;
}