//Levi Silva Freitas

#include <bits/stdc++.h>
using namespace std;

//Funcao responsavel por inverter cada caracter da string de entrada
string inverterString(const string &str) {
    string invertida = str;
    char aux;
    int n = invertida.length();

    for (int i = 0; i < n / 2; ++i) 
    {
        aux = invertida[i];
        invertida[i] = invertida[n - i - 1];
        invertida[n - i - 1] = aux;
    }

    return invertida;
}

int main() {
    string str;
    
    cout << "Digite uma string: ";
    getline(cin, str);

    string strInvertida = inverterString(str);

    cout << "String original: " << str << endl;
    cout << "String invertida: " << strInvertida << endl;

    return 0;
}
