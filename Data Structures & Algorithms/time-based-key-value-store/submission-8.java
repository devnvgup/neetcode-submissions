
class Entry {
    String value;
    int timestamp;

    Entry(String value, int timestamp) {
        this.value = value;
        this.timestamp = timestamp;
    }
}

class TimeMap {
    private Map<String, List<List<Entry>>> map;
    public TimeMap() {
        this.map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        List<List<Entry>> et = map.getOrDefault(key, new ArrayList<>());
        et.add(new ArrayList<>(List.of(new Entry(value, timestamp))));
        map.put(key, et);
    }

    public String get(String key, int timestamp) {
        List<List<Entry>> etL = map.get(key);
        if (etL == null || etL.isEmpty() || etL.get(0) == null || etL.get(0).isEmpty()) {
            return "";
        }

        Entry et = etL.get(0).get(0);
        Map<String, Integer> largestTimeStamp = new HashMap<>();
        largestTimeStamp.put(et.value, et.timestamp);
        // String largestTimeStampString = "";
        return binarySearch(0, etL.size() - 1, etL, timestamp, largestTimeStamp);
    }

    public String binarySearch(int start, int end, List<List<Entry>> list, int timestamp,
        Map<String, Integer> largestTimeStamp) {
        // stop condition

        String key = largestTimeStamp.keySet().iterator().next();
        int value = largestTimeStamp.get(key);

        if (value > timestamp) {
            return "";
        }
        if (start > end) {
            return key;
        }
        int mid = start + (end - start) / 2;
        // if to check left
        List<Entry> et = list.get(mid);
        if (et.get(0).timestamp == timestamp) {
            return et.get(0).value;
        }
        if (et.get(0).timestamp > value && et.get(0).timestamp < timestamp) {
            largestTimeStamp = new HashMap<>();
            largestTimeStamp.put(et.get(0).value, et.get(0).timestamp);
        }
        if (et.get(0).timestamp > timestamp) {
            return binarySearch(0, mid - 1, list, timestamp, largestTimeStamp);
        } else { // else to check right
            return binarySearch(mid + 1, end, list, timestamp, largestTimeStamp);
        }
    }
}

// { alice : [[{happy,1}],[{sad,3}]] }

// case 1 : 0 => return ""
// case 2 : 2 => return test1
// case 3 : 3 => return test3
// case 4 : 6 => return test5

// get
// case 1: test1 1, get 2 => return test1
// case 2: test1 1 , test2 2, test3 3 , get 4. > return test3
// case 3: test1 1, test2 2 , get 0 => return ""

// set