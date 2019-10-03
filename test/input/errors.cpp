#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void segfault_sigaction(int signal, siginfo_t *si, void *arg)
{
    exit(0);
}

int main(int argc, char **)
{
    int *foo = NULL;
    struct sigaction sa;

    memset(&sa, 0, sizeof(struct sigaction));
    sigemptyset(&sa.sa_mask);
    sa.sa_sigaction = segfault_sigaction;
    sa.sa_flags = SA_SIGINFO;

    sigaction(SIGSEGV, &sa, NULL);


    int * p = (int*) malloc(11);

    int ** pp = (int**) malloc(sizeof(int*));
    *pp = (int*) malloc(4 * sizeof(int));

    int * array = (int*) malloc(10 * sizeof(int));
    array[-1] = array[10];
    free(array + 4);

    int a;
    int * z = array + a;
    *z = 3;
    if (a == 0)
    {
        int b = a + 1;
    }
    else
    {
        int c = a + 1;
    }

    int * n = new int[2];
    free(n);

    if (argc > 1)
    {
        void (*fun_ptr)(int) = 0;
        (*fun_ptr)(10);
    }

    return 0;
}
