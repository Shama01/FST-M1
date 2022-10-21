package Activities;

public class Activity_2 {

    public static void main(String[] args){
        int [] a= new int [6];
        int b=0;
        int i;
        //int d= 30;
        a[0]= 10;
        a[1]=77;
        a[2]=10;
        a[3]=54;
        a[4]= -11;
        a[5]= 10;

        for(i=0;i<=5;i++)
        {
            if (a[i]==10)
            {
                b = b + 10;
            }

        }
        if (b==30){
            System.out.println("True");
        }
        else if (b>30) {
            System.out.println("False");

        }
        else {
            System.out.println("False");

        }

        }
    }

