#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys

from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict): 
    authenticator = IAMAuthenticator("oXgdQ5fqeveFxKiRaanSV1HFaN9_msXDiHTDfV0kckY0")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://16a3789a-76a2-4ffd-8d0b-d85ca4333270-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(
                db='reviews',
                document=dict["review"]
            ).get_result()
    try: 
        # result_by_filter=my_database.get_query_result(selector,raw_result=True) 
        result= {
            'headers': {'Content-Type':'application/json'}, 
            'body': {'data':response} 
            }        
        return result
    except:  
        return { 
            'statusCode': 404, 
            'message': 'Something went wrong'
            }
