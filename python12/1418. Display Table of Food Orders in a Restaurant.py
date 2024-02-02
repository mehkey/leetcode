class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ans = defaultdict(Counter)
        
        styp = set()
        
        for p, tab, typ in orders:
            styp.add(typ)
            ans[tab][typ]+=1

        sind = { v:i+1 for i,v in enumerate(sorted(styp))}

        res = [["0" for _ in range(len(styp)+1)] for _ in range(len(ans) + 1)]
        res[0][0] = 'Table'
        for i,t in enumerate(sorted(ans.keys(), key=lambda x: int(x))):

            res[i+1][0] = t
            for k,v in ans[t].items():
                
                res[i+1][sind[k]] = str(v) 

        for v,i in sind.items():
            res[0][i] = v

        return res

vector<vector<string>> displayTable(vector<vector<string>>& orders) {
    vector<unordered_map<string, int>> tables(501);
    set<string> foods;
    for (auto &v : orders) {
        foods.insert(v[2]);
        ++tables[stoi(v[1])][v[2]];
    }
    vector<vector<string>> res;
    for (auto t = 0; t <= 500; ++t) {
        if (t > 0 && tables[t].empty())
            continue;
        res.push_back(vector<string>());
        res.back().push_back(t == 0 ? "Table" : to_string(t));
        for (auto it = begin(foods); it != end(foods); ++it) {
            res.back().push_back(t == 0 ? *it : to_string(tables[t][*it]));
        }
    }
    return res;
}


public List<List<String>> displayTable(List<List<String>> orders) {
        List<List<String>> res = new ArrayList<>();
        List<String> firstRow = new ArrayList<>();
        firstRow.add("Table");
        TreeSet<String> set = new TreeSet<>();
        TreeMap<Integer,Map<String,Integer>> map = new TreeMap<>();
        for (List<String> order : orders) {
            String dish = order.get(2);
            set.add(dish);
            Integer table = Integer.parseInt(order.get(1));
            map.putIfAbsent(table,new HashMap<>());
            if(map.get(table).containsKey(dish)) {
                Map<String,Integer> m = map.get(table);
                m.put(dish,m.getOrDefault(dish,0)+1);
            } else {
                map.get(table).put(dish,1);
            }
        }

        firstRow.addAll(set);
        res.add(firstRow);
        for (Map.Entry<Integer,Map<String,Integer>> entry : map.entrySet()) {
            List<String> list = new ArrayList<>();
            list.add(entry.getKey()+"");
            Map<String,Integer> m = entry.getValue();
            for (String dish : set) {
                if(m.containsKey(dish)) {
                    list.add(m.get(dish)+"");
                } else {
                    list.add("0");
                }
            }
            res.add(list);
        }
        return res;

    }