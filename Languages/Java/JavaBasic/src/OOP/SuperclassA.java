package OOP;

public class SuperclassA {
    public int superClassVarA;
    public void superClassVoidA(){}
    //
    class SubclassA extends SuperclassA{
        void subclassMethodA(){
            superClassVarA = 10;
        }
    }

    class AnyClassA{
        SuperclassA new_superclass_a = new SuperclassA();
        void anyClassMethodA(){
            new_superclass_a.superClassVoidA();
        }
    }
}
