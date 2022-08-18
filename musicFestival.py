from urllib import request
import requests as req
import json
import logging



def getAPI_TestData(requestURL:str):
    resp = req.get(requestURL)
    return resp

def isJson(jsonResponse : str) -> bool:
    try:
        json.loads(jsonResponse)
    except ValueError as v:
        return False
    return True

def isEmpty(jsonResponse : str) -> bool:
    if jsonResponse == '""':
        return True
    else:
        return False

def verifyAllTestCases(respObj: request):
    
## Test Case 0    ## --> Wrong URL
    if respObj.status_code == 404:
        logging.info(f"## FAILED## In-Correct URL --> {requestURL} --> Response is  --> {respObj.status_code}")
    
## Test Case 1    ##  --> response is 200 
    elif respObj.status_code == 200:

## Test Case 1.1    ##  --> response is 200  ## EMPTY RESPONSE
        if isEmpty(respObj.text):
            logging.info(f"## FAILED ##Correct URL --> {requestURL} --> Response is  --> {respObj.status_code}\
            \nEMPTY RESPONSE")

## Test Case 1.2    ##  --> response is 200  ## CORRECT FORMAT    
        else:
            if isJson(respObj.text):
                logging.info(f"## SUCCESS ##Correct URL --> {requestURL} --> Response is  --> {respObj.status_code}\
            \noutput is in Correct format \n {respObj.text}")

## Test Case 1.3   ##  --> response is 200  ## IN-CORRECT FORMAT
            else:
                logging.info(f"## FAILED ##Correct URL --> {requestURL} --> Response is  --> {respObj.status_code}\
            \noutput is in-correct format \n {respObj.text}")
## Test Case 2     ## --> response is not 200
    else:

## Test Case 2.1     ## --> response is not 200 and TOO MANY REQUESTS
        if(respObj.text == "Too many requests, throttling"):
            logging.info(f"## FAILED ##Correct URL --> {requestURL}--> Response is  -->{respObj.status_code}\
                \nToo many requests, throttling")
## Test Case 2.2     ## --> response is not 200 and UN-AUTHARIZED REQUESTS
        else:
            logging.info(f"## FAILED ##Correct URL --> {requestURL}--> Response is  -->{respObj.status_code}")


if __name__ == '__main__':

    logging.basicConfig(level = logging.INFO,filename = "testcase.log",format= '[%(asctime)s ---> %(message)s]')
    requestURL = 'https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals'

    respObj = getAPI_TestData(requestURL)
    verifyAllTestCases(respObj)