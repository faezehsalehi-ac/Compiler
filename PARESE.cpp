#include <iostream> 
#include <string> 
#include <fstream> 
#include <sstream> 
#include <cstdlib>
using namespace std;
bool operatorr(char ch) 
{ 
	if (ch == ' ' || ch == ',' || ch == ';' || 
	 ch == '=' || ch == '(' || ch == ')' || 
		  ch == '{' || ch == '}' || ch == '\n'||ch=='\t') 
		return (true); 
	return (false); 
}
bool keyword(string str){
	if(str=="return"|| str=="int")
		return (true); 
	return (false);
}
bool isInteger(string str) 
{ 
	int i, len = str.length(); 

	for(i=0;i<=len;) {

	        if(str[i]<='9'&& str[i]>='0'||str[i]=='.')i++;
			else return (false); 
		}
		return true;} 


void parse(string str) 
{ 
    int j=-1;string temp;string remine;
	for(int i=0;i<str.length();i++){
		if(operatorr(str[i])){
			remine=str.substr(i,1);
		temp= str.substr(j+1,i-j-1);j=i;
		 
		if(!temp.empty()){
								
		 //cout<<"operator="<<str[i]<<endl;
		if(keyword(temp) ) cout<<"keyword="<<temp<<endl;
		else if(isInteger(temp) )cout<<"num="<<temp<<endl;
		else{
		 cout<<"ID="<<temp<<endl;
		 }
		 }
		 if(operatorr(str[i])&& str[i]!=' ') cout<<"operator="<<str[i]<<endl;
		  if(operatorr(str[i])&& str[i]==' ')cout<<"operator="<<"space"<<endl;
	}
	}
}
int main(){
	ifstream myfile;string input;
	cout<< "enter file_name:";cin>>input;
	myfile.open(input.c_str());
	stringstream buf;
	buf<<myfile.rdbuf();
	string input1=buf.str();
	parse(input1);
	return 0;
}
	

