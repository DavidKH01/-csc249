
#include <iostream>

using namespace std;

int main() {
    string user_name;
    int user_qt;

    // Create an interactive program where a customer is greeted by name.
    cout << "What is your name: " << endl;
    getline(cin, user_name);
    cout << endl;

    // Advertise to the customer the name of the widget, their unit price, and the overall stock on hand.
    cout << "Hello " << user_name << ", today we have a sale on WidgetCSC. We have in stock 100 WidgetCSC. Each is worth $4.89 dollars." << endl;

    // Ask the user how many widgets they wish to buy.
    cout << "How many would you like to purchase?" << endl;
    cin >> user_qt;
    cout << endl;

    cout << "You have asked for " << user_qt << endl;

    // Tell them the gross price (without taxes, etc.)
    double gross_price = user_qt * 4.89;
    cout << "Your total cost today will be $" << gross_price << endl << endl;

    // Thank them for their business.
    cout << "Thank you for shopping at PetSmart" << endl;

    return 0;}