package com.sa.web.dto;

public class SampleDataDto {
    private int is_female;
    private int age;
    private int is_urban;
    private double is_working;
    private int hypertension;
    private int heart_disease;
    private int ever_married;
    private double avg_glucose_level;
    private int bmi;
    private double smoking_status;

    public SampleDataDto() {
    }

    public int getIs_female() {
        return is_female;
    }

    public void setIs_female(int is_female) {
        this.is_female = is_female;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getIs_urban() {
        return is_urban;
    }

    public void setIs_urban(int is_urban) {
        this.is_urban = is_urban;
    }

    public double getIs_working() {
        return is_working;
    }

    public void setIs_working(double is_working) {
        this.is_working = is_working;
    }

    public int getHypertension() {
        return hypertension;
    }

    public void setHypertension(int hypertension) {
        this.hypertension = hypertension;
    }

    public int getHeart_disease() {
        return heart_disease;
    }

    public void setHeart_disease(int heart_disease) {
        this.heart_disease = heart_disease;
    }

    public int getEver_married() {
        return ever_married;
    }

    public void setEver_married(int ever_married) {
        this.ever_married = ever_married;
    }

    public double getAvg_glucose_level() {
        return avg_glucose_level;
    }

    public void setAvg_glucose_level(double avg_glucose_level) {
        this.avg_glucose_level = avg_glucose_level;
    }

    public int getBmi() {
        return bmi;
    }

    public void setBmi(int bmi) {
        this.bmi = bmi;
    }

    public double getSmoking_status() {
        return smoking_status;
    }

    public void setSmoking_status(double smoking_status) {
        this.smoking_status = smoking_status;
    }

    @Override
    public String toString() {
        return "SampleDataDto{" +
                "is_female=" + is_female +
                ", age=" + age +
                ", is_urban=" + is_urban +
                ", is_working=" + is_working +
                ", hypertension=" + hypertension +
                ", heart_disease=" + heart_disease +
                ", ever_married=" + ever_married +
                ", avg_glucose_level=" + avg_glucose_level +
                ", bmi=" + bmi +
                ", smoking_status=" + smoking_status +
                '}';
    }
}
