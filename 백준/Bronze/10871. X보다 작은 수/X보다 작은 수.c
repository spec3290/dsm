#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n, x, cnt = 0;
    int a[10000], b[10000];
    
    scanf("%d %d", &n, &x);  // 쉼표 제거

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] < x) {
            b[cnt++] = a[i];  // 인덱스 0부터 저장
        }
    }

    for (int i = 0; i < cnt; i++) {
        printf("%d ", b[i]);  // 공백으로 구분
    }

    return 0;
}