import java.util.*;

public class Main {
    static Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {

        Set<String> set = new HashSet<>();

        int N = scan.nextInt();
        int M = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i < N; i++) {
            set.add(scan.nextLine());
        }

        List<String> list = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            list.add(scan.nextLine());
        }

        int count = 0;
        for (int i = 0; i < M; i++) {
            if (set.contains(list.get(i))) {
                count++;
            }
        }

        System.out.println(count);
        
    }
}