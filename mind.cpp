// Input format:
// First line contains n, the number of points on plane
// N line follows, each having two space separated double values representing coordinates
// Then a query input which is two space separated double values representing coordinates of query input.
/*---------------------------------
SUBMISSION BY <<DEEPANSHU ROHILLA>>
-----------------------------------
*/
#include <iostream>
#include <math.h>
using namespace std;

double distance(double q1,double q2,double a1,double a2){
    return (double) sqrt((q1-a1)*(q1-a1) + (q2-a2)*(q2-a2));
}

int main() {
	int n;
	cin>>n;
	double ar[n][2];
	for(int i=0;i<n;i++){
	    cin>>ar[i][0]>>ar[i][1];
	}
	double q1,q2;
	int index=-1;
	cin>>q1>>q2;
	double dist = -1.0;
	for(int i=0;i<n;i++){
	    double dist1 = distance(q1,q2,ar[i][0],ar[i][1]);
	    if(dist==-1.0 || dist1<dist){
	        dist = dist1;
	        index=i;
	    }
	}
	cout<<"("<<q1<<","<<q2<<") is closest with "<<"("<<ar[index][0]<<","<<ar[index][1]<<") and the distance between them is "<<dist<<endl;
	return 0;
}
