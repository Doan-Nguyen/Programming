/*
 * Copyright 2019 {@author Loda} (https://loda.me).
 * This project is licensed under the MIT license.
 *
 * @since 5/11/2019
 * Github: https://github.com/loda-kun
 */


package spring;

import org.springframework.stereotype.Component;

/*  Thong bao cho Spring biet & quan ly day la mot Bean (~ dependency)*/
@Component
public class Bikini implements Outfit{
    @Override
    public void wear(){
        System.out.println("Victoria Secret");
    }
}
