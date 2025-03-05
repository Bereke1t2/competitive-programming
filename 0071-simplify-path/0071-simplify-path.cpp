class Solution {
public:
    string simplifyPath(string path) {
        vector<string> v;
        string ans="",temp="";
        for(auto x: path){
            if(x=='/'){
                if(temp==".."){
                    if(v.size()==0)temp="";
                    else v.pop_back();
                    temp="";
                }
                else if(temp==".") temp="";
                if(temp=="")continue;
                v.push_back(temp);
                temp="";
            }
            else temp +=x;
        }
        if(temp.length()!=0 && temp!="."){
            if(temp==".."){
                    if(v.size()==0)temp="";
                    else v.pop_back();
                }else
            v.push_back(temp);
        }
        for(auto x:v)ans +='/'+x;
        return (ans.length()==0) ? "/":ans;

    }
};