/**
 * Copyright 2019 {@author Loda} (https://loda.me).
 * This project is licensed under the MIT license.
 *
 * @since 5/11/2019
 * Github: https://github.com/loda-kun
 */
package spring;
/*
 Đánh dấu class bằng @Component
 Class này sẽ được Spring Boot hiểu là một Bean (hoặc dependency)
 Và sẽ được Spring Boot quản lý
*/
import org.springframework.stereotype.Component;

public interface Outfit {
    public void wear();
}
