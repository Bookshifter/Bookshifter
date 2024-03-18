package com.example.bookshifter.exceptions;

import org.springframework.http.HttpStatusCode;
import org.springframework.web.client.HttpStatusCodeException;

public class ApiException extends HttpStatusCodeException {
    public ApiException(String message, HttpStatusCode statusCode){
        super(statusCode, message);
    }
}
