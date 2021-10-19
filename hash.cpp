#include <iostream>
#include <ctime>
#include <math.h>
#include <fstream>
#include <unordered_map>

using namespace std;

int CountUniqueCharacters(string s)
{

    unordered_map<char, int> m;

    for (int i = 0; i < s.length(); i++)
    {
        m[s[i]]++;
    }

    return m.size();
}

/*
    Crear una semilla random generada con ctime.
    Truncar si la entrada es mayor a 25 caracteres / agregar padding si entrada es menor a 25 caracteres, el padding es una secuencia alfabetica.
    Se convierte el mensaje corregido a un int que se suma con la seed.
    Se transforma cada caracter del mensaje corregido a su valor en ASCII y se suman, a esto se le agrega el valor de la seed.
    luego si el valor es menor a 65 o mayor a 122, se ajusta para que el caracter hasheado este entre esos valores.
    El mensaje resultante debe tener 25 caracteres.
*/

string hashea(string message)
{
    time_t seed = time(0);
    //string hashed[25];
    char *hashed = new char[25];
    //string fixedMessage;
    int prehash = 0;
    int middlePoint;
    int i = 0;
    
    while (i < message.length())
    {
        prehash += int(message[i]);
        ++i;
    }
    
    prehash += seed;
    exit;
    
    for (int i = 0; i < 25; ++i)
    {
        middlePoint = prehash % (i + 2);
        while(middlePoint > 122 || middlePoint < 65)
        {
        if (middlePoint < 65)
        {
            middlePoint = middlePoint + (i+2);
        }

        else if (middlePoint > 122)
        {
            middlePoint = middlePoint - (i+2);
        }
        }
        hashed[i] = char(middlePoint);
    }

    return (hashed);
}

/*
    Se revisa el input, si es un string, se hace el hash y el calculo de entropia.
    Si es un file, se hace el hash y el calculo de entropia linea por linea.
*/

int main()
{
    string message;
    string fileName;
    int counter = 0;
    int entropy;
    int inputType;

    cout << "Input por string(1) o file(2)?" << endl;
    cin >> inputType;

    if (inputType == 1)
    {
        cin >> message;
        entropy = message.length() * (log2(CountUniqueCharacters(message)));

        cout << "Entropy: " << entropy << endl;

        cout << "Hash: " << hashea(message) << endl;
    }

    else if (inputType == 2)
    {
        cin >> fileName;
        ifstream f(fileName);

        while (getline(f, message))
        {
            CountUniqueCharacters(message);
            entropy = message.length() * (log2(CountUniqueCharacters(message)));

            cout << "Entropy: " << entropy << endl;
            cout << "Hash: " << hashea(message) << endl;
        }
    }

    return (0);
}