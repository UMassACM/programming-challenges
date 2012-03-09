#include <iostream>
using namespace std;

int numInput = 0;
int input[1000];

int main() {
	cin >> numInput;
	for (int i=0; i<numInput; i++) {
		cin >> input[i];
	}
	for (int i=0; i<numInput; i++) {
		int numDigits = 1;
		double number = (double)input[i];
		for (int x = number-1; x>0; x--) {
			while (number >= 10.0) {
				numDigits++;
				number /= 10.0;
			}
			number *= x;
		}
		cout << numDigits << endl;
	}
	cin >> numInput;

	return 0;
}