namespace std{
class Solution {
public:
    bool isAnagram(string s, string t) {
       int cnt[30]={0};
        int ns = s.length(),nt = t.length();
        if(ns!=nt)return false;
        for(int i = 0;i<ns;i++){
            cnt[s[i]-'a']++;
        }
        for(int i = 0;i<nt;i++){
            cnt[t[i]-'a']--;
        }
        for(int i = 0;i<30;i++){
            if(cnt[i]!=0)return false;
        }
        return true;
    }  
};
}