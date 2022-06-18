/**
 * Copyright 2019 {@author Loda} (https://loda.me).
 * This project is licensed under the MIT license.
 *
 * @since 5/11/2019
 * Github: https://github.com/loda-kun
 */
package spring;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Girl {
    @Autowired
    Outfit outfit;

    public Girl(Outfit outfit){
        this.outfit = outfit;
    }
}
