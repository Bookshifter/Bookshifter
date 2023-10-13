package com.example.dslist.bookapi.google;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class ItemsWrapper {
    private VolumeInfo volumeInfo;

    public VolumeInfo getVolumeInfo(){
        return this.volumeInfo;
    }
    public void setVolumeInfo(VolumeInfo volumeInfo) {
        this.volumeInfo = volumeInfo;
    }
}
