#include <iostream>
using namespace std;


int main(){

int price;
int tickets;
int sum;
double stanPrice;
int extraTickets; 



cout << "Enter the number of tickets";
cin >> tickets;
cout << "Enter the standard ticket price";
cin >> price;




if (tickets <= 5) {
    sum = tickets * price;}
    else
    { extraTickets = tickets - 5;
    sum = (5 * price) + ( extraTickets * price * 1.2);

 }

cout << "Total ticket cost:" << sum << endl;

    return 0;
}