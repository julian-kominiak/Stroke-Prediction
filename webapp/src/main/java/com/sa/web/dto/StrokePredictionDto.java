package com.sa.web.dto;

public class StrokePredictionDto {
    private double probability;

    public StrokePredictionDto() {
    }

    public StrokePredictionDto(double probability) {
        this.probability = probability;
    }

    public double getProbability() {
        return probability;
    }

    public void setProbability(double probability) {
        this.probability = probability;
    }

    @Override
    public String toString() {
        return "StrokePredictionDto{" +
                "probability=" + probability +
                '}';
    }
}
