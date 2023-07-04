package com.example.main;

import com.alibaba.fastjson.JSONObject;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class asd {

    @RequestMapping(value = "/asd/receiveFlask",method = RequestMethod.POST)
    public String asd(@RequestBody JSONObject jsonObject){
        System.out.println(jsonObject);
        String s = (String)jsonObject.get("name");
        String ss = (String)jsonObject.get("job");
        System.out.println(s);
        System.out.println(ss);
        return "asd";
    }


}
