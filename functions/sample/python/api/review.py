import sys 
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict): 
    authenticator = IAMAuthenticator("oXgdQ5fqeveFxKiRaanSV1HFaN9_msXDiHTDfV0kckY0")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://16a3789a-76a2-4ffd-8d0b-d85ca4333270-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
                db='reviews',
                selector={'dealership': {'$eq': int(dict['id'])}},
            ).get_result()
    try: 
        # Extract only the 'docs' part of the response
        docs = response.get('docs', [])

        result= {
            'headers': {'Content-Type':'application/json'}, 
            'body': docs 
            }        
        return result
    except:  
        return { 
            'statusCode': 404, 
            'message': 'Something went wrong'
            }