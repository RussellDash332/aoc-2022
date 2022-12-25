import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        Map<Character, Long> h = new HashMap<Character, Long>();
        h.put('0', 0L);
        h.put('1', 1L);
        h.put('2', 2L);
        h.put('-', -1L);
        h.put('=', -2L);

        Map<Long, String> r = new HashMap<Long, String>();
        h.forEach(
            (key, value)
                -> r.put(value, ""+key));

        long n = 0L, rr = 0L;
        String s;
        while (true) {
            try { // desnafu
                s = br.readLine();
                rr = 0L;
                for (int i=0; i<s.length(); i++) {
                    rr = 5*rr + h.get(s.charAt(i));
                }
                n += rr;
            } catch (Exception e) {
                List<String> ss = new ArrayList<String>();
                while (n > 0) {
                    ss.add(r.get(n%5 - 5*(n%5>2 ? 1 : 0)));
                    n = n/5 + (n%5>2 ? 1 : 0);
                }
                Collections.reverse(ss);
                System.out.println("Part 1: " + String.join("", ss));
                System.out.println("Part 2: THE END!");
                break;
            }
        }
    }
}