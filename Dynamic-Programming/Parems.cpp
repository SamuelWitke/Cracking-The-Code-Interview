#include <iostream>
#include <string>
#include <set>
using namespace std;

set<string> genParen(int rem){
	set<string> set = new set<string>;
	if(rem == 0){
		set.add("");
	}else{
		set<string> prev = genParen(rem-1);
		for(string str : prev){
			for(int i=0;i<str.length() ;i++){
					if(s[i] == '('){
						string s = insert(str,i);
						set.add(s);
					}
			
		
