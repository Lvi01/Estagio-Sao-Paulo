//Levi Silva Freitas

#include <bits/stdc++.h> //Biblioteca generalista
using namespace std;

bool Fib(int num) {
    //Casos base
    if (num == 0 || num == 1) 
        return true;

    int a = 0, b = 1, prox;

    //Cálculo da sequencia Fib
    while (b <= num) 
    {
        prox = a + b;
        if (prox == num) return true;
        a = b;
        b = prox;
    }

    //Se sair do while o proximo numero de Fib eh maior que o numero consultado
    return false;
}

int main() {
    int num;
    cout << "Informe um numero (Apenas digite o numero, ex: 34): ";
    cin >> num;

    if (Fib(num)) 
        cout << num << " pertence a sequência de Fibonacci." << endl;
    else
        cout << num << " nao pertence a sequência de Fibonacci." << endl;

    return 0;
}
