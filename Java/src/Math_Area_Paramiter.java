import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class Math_Area_Paramiter { public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the value of x: ");
    int x = sc.nextInt();

    System.out.println("The Area of the square is : ");
    System.out.println(Area_Square(x));
    System.out.println("The Perimeter of the square is : ");
    System.out.println(Perimeter_Square(x));
    System.out.println("The Area of the circle is : ");
    System.out.println(Area_Circle(x));
    System.out.println("The Perimeter of the circle is : ");
    System.out.println(Perimeter_Circle(x));
    System.out.println("\s\s\s");


    try {TimeUnit.SECONDS.sleep(2);} catch (InterruptedException e) { throw new RuntimeException(e);}


    System.out.println("Do you want to continue?..");
    String choice = sc.nextLine();
    while(!choice.equals(" ")) {
        choice = sc.nextLine();
        if(choice.equalsIgnoreCase("yes")) {
            System.out.println("Enter the value of y: ");
            int y = sc.nextInt();
            System.out.println("The Area of the rectangle is : ");
            System.out.println(Area_Rectangle(x,y));
            System.out.println("The Perimeter of the rectangle is : ");
            System.out.println(Perimeter_Rectangle(x,y));
            break;
        }

    }
    try{TimeUnit.SECONDS.sleep(2);}catch(InterruptedException e){throw new RuntimeException(e);}

    System.out.println("This is for the area and perimeter of the triangle ! ");


    try{TimeUnit.SECONDS.sleep(2);}catch(InterruptedException e){throw new RuntimeException(e);}

    System.out.println("Do you want to continue?..");
    String choice2 = sc.nextLine();
    while(!choice2.equals(" ")) {
        choice2 = sc.nextLine();
        if(choice2.equalsIgnoreCase("yes")) {
            System.out.println("Enter the value for the height: ");
            int h= sc.nextInt();
            System.out.println("Enter the value of the first side of the triangle  ");
            int s1= sc.nextInt();
            System.out.println("Enter the value of the second side of the triangle  ");
            int s2= sc.nextInt();
            System.out.println("Enter the value of the third side of the triangle  ");
            int s3= sc.nextInt();


            System.out.println("The Area of the triangle is : ");
            System.out.println(Area_Triangle(x,h));
            if(s1==s2 && s3!=s2){
                System.out.println("The Perimeter of the two sides triangle is : ");
                System.out.println(Perimeter_Triangle_Two_Sides(s1,s2));
            break;}
            else if(s1 == s2){
                System.out.println("The Perimeter of the equal sides of triangle is : ");
                System.out.println(Perimeter_Triangle_Same_Sides(s1));
            break;}
            else{System.out.println("The Perimeter of the  triangle is : ");
                System.out.println(Perimeter_Triangle_Dif_Sides(s1,s2,s3));break;}

        }
    }


}

    static int End(){return 0;}
    static double Area_Square (double a ){return a*a;}
    static  double Perimeter_Square (double a ){return 4*a;}
    static double Area_Circle  (double r ){return r*r;}
    static double Perimeter_Circle (double r ){return  (2*r*3.14);}
    static double Area_Rectangle (double l , double w ){return l*w;}
    static double Perimeter_Rectangle (double l , double w ){return 2*(l+w);}
    static double Area_Triangle(double a, double h){return 0.5*h*a;}
    static double Perimeter_Triangle_Dif_Sides(double a, double b , double c){return a+b+c;}
    static double Perimeter_Triangle_Same_Sides(double a){return a*3;}
    static double Perimeter_Triangle_Two_Sides(double a, double b){return a+2*b;}

}





