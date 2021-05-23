package com.sa.web.dto;

public class StrokePreditctionDto {
    private double probability;

    public StrokePreditctionDto() {
    }

    public StrokePreditctionDto(double probability) {
        this.probability = probability;
    }

    public double getProbability() {
        return probability;
    }

    public void setProbability(double probability) {
        this.probability = probability;
    }
}
