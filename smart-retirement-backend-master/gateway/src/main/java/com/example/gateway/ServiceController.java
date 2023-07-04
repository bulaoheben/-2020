package com.example.gateway;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.*;

@RestController
public class ServiceController {
    @Autowired
    private ApplicationUtil applicationUtil;

    @GetMapping("/urls")
    public JSONObject getUrls(){
        String targetName = "homePageUrl";
        JSONObject object = new JSONObject();
//        List<String> urls = new ArrayList<>();
        Map<String, List<ServiceInstance>> map = applicationUtil.serviceUrl();
        Set<String> keySet = map.keySet();
        for (String key : keySet) {
            List<ServiceInstance> value = map.get(key);
            for (ServiceInstance serviceInstance : value) {
                String serviceInstanceStr = JSON.toJSONString(serviceInstance);
                if (serviceInstanceStr != null) {
                    JSONObject jsonObject = JSON.parseObject(serviceInstanceStr);
                    JSONObject instanceInfo = jsonObject.getJSONObject("instanceInfo");
                    String homePageUrl = instanceInfo.getString(targetName);
                    object.put(key, homePageUrl);
                }
            }
        }
        return object;
    }

    @GetMapping("/all_info")
    public Map<String, List<ServiceInstance>> getInfo(){
        return applicationUtil.serviceUrl();
    }

    @GetMapping("/urls/{name}")
    public Boolean urlIsExist(@PathVariable String name){
        return applicationUtil.isExitservice(name);
    }

}
