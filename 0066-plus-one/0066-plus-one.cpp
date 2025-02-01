class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len=digits.size()-1,carry=0;
        do{
          if(digits[len]==9){
            digits[len]=0;
            carry=1;
            len--;
          }else {
            digits[len]++;
            carry=0;
          }
        }while(len>-1 && carry!=0);
        if(digits[0]==0 && (digits.size()==1 || digits[1]==0))digits.insert(digits.begin(),1);
        return digits;
    }
};