package Activities;

public class Car {

    String color= "Red";
    String transmission= "ABC";
    int make= 123;
    int tyres;
    int doors;
    public Car() {
        tyres = 4;
        doors =4;
    }
    public void displayCharacteristics()
    {
        System.out.println("Color of car is" +" "+color);
        System.out.println("Transmission of the car is "+" " + transmission);
        System.out.println("Make of the Car is"+" " + make);
        System.out.println("No. of tyre"+" " + tyres);
        System.out.println("No.of doors"+ " " + doors);
    }
    public void accelarate() {
        System.out.println("Car is moving forward.");
    }
    public void brake() {
            System.out.println("Car is stopped.");
    }

}

