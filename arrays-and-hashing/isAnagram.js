function isAnagram(s, t) {
        if(s.length !== t.length){
            return false;
        }

        let sSort = s.split("").sort().join();
        let tSort = t.split("").sort().join();
        return sSort == tSort;
    }

console.log(isAnagram("nitin", "abcde"));


