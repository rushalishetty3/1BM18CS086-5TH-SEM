#include<iostream>
using namespace std;

#define bucketSize 512

void delay(int n){
    while(n>0){
        n--;
    }
}

void bktInput(int a,int b) {
    if(a>bucketSize)
        cout<<"\n\t\tBucket overflow";
    else {
        delay(500);

        while(a>b) {
            cout<<"\n\t\t"<<b<<" bytes outputted.";
            a -= b;
            delay(500);
        }

        if(a>0) 
            cout<<"\n\t\tLast "<<a<<" bytes sent\t";

        cout<<"\n\t\tBucket output successful";
    }
}

int main() {
    int op, pktSize;

    cout<<"Enter output rate : "; 
    cin>>op;

    for(int i=1;i<=5;i++){
        delay(rand()%1000);
        pktSize = rand()%1000;
        cout<<"\nPacket no "<<i<<"\tPacket size = "<<pktSize;
        bktInput(pktSize,op);
    }

    return 0;
}