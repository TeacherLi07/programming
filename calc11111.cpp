#include <iostream>
#include <gmpxx.h>
#include <gmp.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

bool is_prime4(mpz_class x) {
    if ((x % 6 != 1) && (x % 6 != 5)) {
        return false;
    }
    for (mpz_class i = 5; i * i <= x; i += 6) {
        if ((x % i == 0) || (x % (i + 2) == 0)) {
            return false;
        }
    }
    return true;
}

int main() {
    mpz_class a = 1;
    mpz_class n = 0;
    auto start_time = high_resolution_clock::now();

    while (true) {
        a = a * 10 + 1;
        n++;
        cout << n << "\tstart at " << duration_cast<milliseconds>(high_resolution_clock::now() - start_time).count() << "ms" << endl;
        if ((n % 3 == 0) || (!is_prime4(n))) {
            cout << "\tcontinue" << endl;
            continue;
        }
        if (is_prime4(a)) {
            auto end_time = high_resolution_clock::now();
            auto duration = duration_cast<milliseconds>(end_time - start_time).count();
            cout << "find!" << "\tn = " << n << "\ta = " << a << "\ttime = " << duration << "ms" << endl;
            break;
        }
    }

    return 0;
}
