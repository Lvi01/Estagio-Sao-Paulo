//Levi Silva Freitas

//Ao final do processamento o valor de SOMA é 91.
//Aproveitei e fiz um codigo para comprovar que minha resposta esta certa:

#include <bits/stdc++.h> //Biblioteca generalista
using namespace std;

int main() {
    int indice = 13, soma = 0, k = 0;

    while(k < indice)
    {
        k += 1;
        soma += k;
    }
    
    cout << soma << endl;

    return 0;
}
