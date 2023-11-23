#include <iostream>
#include <unistd.h>

using namespace std;

void move(int n, char from, char to, char aux)
{
    if (n == 1)
    {
        cout << "Move disk 1 from " << from << " to " << to << endl;
        cout << "A---B" << endl;
        cout << "|||" << endl;
        cout << "C" << endl;
        return;
    }
    move(n - 1, from, aux, to);
    cout << "Move disk " << n << " from " << from << " to " << to << endl;
    cout << "A---B" << endl;
    cout << "|||" << endl;
    cout << "C" << endl;
    move(n - 1, aux, to, from);
}

int main()
{
    int n;
    cout << "Enter the number of disks: ";
    cin >> n;
    move(n, 'A', 'B', 'C');
    return 0;
}