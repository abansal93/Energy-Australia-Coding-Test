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

if __name__ == '__main__':

    logging.basicConfig(level = logging.INFO,filename = "testcase.log",format= '[%(asctime)s ---> %(message)s]')
    requestURL = 'https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals'

    testResponse = getAPI_TestData(requestURL)

    # print(f" Status of request is {testResponse.status_code} and its content is {testResponse.text}")

    ## Test Case 0
    
    print(testResponse.text)
    print(isEmpty(testResponse.text))

## Test Case 0    ## --> Wrong URL
    if testResponse.status_code == 404:
        logging.info(f"## FAILED## In-Correct URL --> {requestURL} --> Response is  --> {testResponse.status_code}")
    
## Test Case 1    ##  --> response is 200 
    elif testResponse.status_code == 200:

## Test Case 1.1    ##  --> response is 200  ## EMPTY RESPONSE
        if isEmpty(testResponse.text):
            logging.info(f"## FAILED ##Correct URL --> {requestURL} --> Response is  --> {testResponse.status_code}\
            \nEMPTY RESPONSE")

## Test Case 1.2    ##  --> response is 200  ## CORRECT FORMAT    
        else:
            if isJson(testResponse.text):
                logging.info(f"## SUCCESS ##Correct URL --> {requestURL} --> Response is  --> {testResponse.status_code}\
            \noutput is in Correct format \n {testResponse.text}")

## Test Case 1.3   ##  --> response is 200  ## IN-CORRECT FORMAT
            else:
                logging.info(f"## FAILED ##Correct URL --> {requestURL} --> Response is  --> {testResponse.status_code}\
            \noutput is in-correct format \n {testResponse.text}")
## Test Case 2     ## --> response is not 200
    else:

## Test Case 2.1     ## --> response is not 200 and TOO MANY REQUESTS
        if(testResponse.text == "Too many requests, throttling"):
            logging.info(f"## FAILED ##Correct URL --> {requestURL}--> Response is  -->{testResponse.status_code}\
                \nToo many requests, throttling")
## Test Case 2.2     ## --> response is not 200 and UN-AUTHARIZED REQUESTS
        else:
            logging.info(f"## FAILED ##Correct URL --> {requestURL}--> Response is  -->{testResponse.status_code}")