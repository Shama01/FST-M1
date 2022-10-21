import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity2 {
    public static void main(String[] args) {
        WebDriver driver = new FirefoxDriver();

        driver.get("https://www.training-support.net/");
        driver.getTitle();
        System.out.println(driver.getTitle());
        WebElement aboutus = driver.findElement(By.id("aboutus"));

        driver.close();
    }
}
