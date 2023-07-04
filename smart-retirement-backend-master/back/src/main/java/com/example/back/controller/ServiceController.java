package com.example.back.controller;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

@RestController
@RequestMapping("/back")
public class ServiceController {

    @RequestMapping(value = "/service_num", method = RequestMethod.GET)
    public int getServiceNum(){
        List<String> name = new ArrayList<>();
        List<String> url = new ArrayList<>();
        String s = HttpUtil.get("http://localhost:8080/urls");
        JSONObject jsonObject = JSONObject.parseObject(s);
        Set<String> keySet = jsonObject.keySet();
        for (String key : keySet) {
            String value = jsonObject.getString(key);
            name.add(key);
            url.add(value);
        }
        return url.size()-1;
    }
    @RequestMapping(value = "/service", method = RequestMethod.GET)
    public JSONObject getServiceURL(){
        String s = HttpUtil.get("http://localhost:8080/urls");
        JSONObject jsonObject = JSONObject.parseObject(s);
        return jsonObject;
    }

}
