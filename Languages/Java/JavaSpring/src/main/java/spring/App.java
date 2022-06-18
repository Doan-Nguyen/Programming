package spring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

@SpringBootApplication
public class App {
    public static void main(String[] args){

//        SpringApplication.run(App.class, args);
        //  ApplicationContext ~ container {Beans}
        ConfigurableApplicationContext context = SpringApplication.run(App.class, args);
        // get Bean
        Outfit outfit = context.getBean(Outfit.class);
        //
        System.out.println("Instance: " + outfit);
        outfit.wear();
    }

}
