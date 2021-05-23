package com.sa.web;

import com.sa.web.dto.StrokePredictionDto;
import com.sa.web.dto.SampleDataDto;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@CrossOrigin(origins = "*")
@RestController
public class StrokePredictionController {

//    @Value("${sp.logic.api.url}")
//    private String spLogicApiUrl;
    private String spLogicApiUrl = "http://192.168.0.182:5000/";

    @PostMapping("/sample_data")
    public StrokePredictionDto sentimentAnalysis(@RequestBody SampleDataDto sampleDataDto) {
        RestTemplate restTemplate = new RestTemplate();

        return restTemplate.postForEntity(spLogicApiUrl + "/analyse/sample_data",
                sampleDataDto, StrokePredictionDto.class)
                .getBody();
    }

    @GetMapping("/testHealth")
    public void testHealth() {
    }
}
