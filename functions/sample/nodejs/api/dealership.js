async function main(params) {
    const { CloudantV1 } = require('@ibm-cloud/cloudant');
    const { IamAuthenticator } = require('ibm-cloud-sdk-core');
    const authenticator = new IamAuthenticator({ apikey: 'oXgdQ5fqeveFxKiRaanSV1HFaN9_msXDiHTDfV0kckY0' })
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
    });
    cloudant.setServiceUrl('https://16a3789a-76a2-4ffd-8d0b-d85ca4333270-bluemix.cloudantnosqldb.appdomain.cloud');
  
    try {
        const result = await findAllDealerships(cloudant);
        const docParts = result.map(item => item.doc);
        /***const code = result.length; ? 200 : 404;*/

        if (result.length == 0) {
            return{
                statusCode: 404,
                body: { error: 'The database is empty' }
            };
        } else {
            return {
                statusCode: 200,
                headers: { 'Content-Type': 'application/json' },
                body: docParts
              };
        }
        
    } catch (err) {
      console.error(err);
      return {
        statusCode: 500,
        headers: { 'Content-Type': 'application/json' },
        body: { error: 'Something went wrong on the server' }
      };
    }
  }
  
  async function findAllDealerships(cloudant) {
    const result = await cloudant.postAllDocs({ db: 'dealerships', includeDocs: true, limit: 10 });
    return result.result.rows;
  }
  