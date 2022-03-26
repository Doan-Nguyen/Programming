import java.util.Stack;
import java.util.TreeSet;

class StackWithMax<Item> extends Stack<Item> {

    private TreeSet<Item> tree = new TreeSet<Item>();

    public Item max() {
        return tree.last();
    }

    public Item push(Item item) {
        super.push(item);
        tree.add(item);
        return item;
    }

    public Item pop() {
        Item item = super.pop();
        tree.remove(item);
        return item;
    }

    public static void main(String[] args) {

        StackWithMax<Integer> stack = new StackWithMax<Integer>();
        int i = 1;
        int N = 100;

        System.out.println("Size: " + stack.size());
        while (i <= N) {
            if (i % 3 == 0) {
                System.out.println("Max: " + stack.max());
            } else {
                System.out.println("Push: " + i);
                stack.push(i);
            }
            ++i;
        }
        System.out.println("Size: " + stack.size());
        while (!stack.isEmpty()) {
            System.out.println("Pop: " + stack.pop());
        }
        System.out.println("Size: " + stack.size());
    }

}