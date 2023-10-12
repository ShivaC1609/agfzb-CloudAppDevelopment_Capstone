async function main(params) {
    const { CloudantV1 } = require('@ibm-cloud/cloudant');
    const { IamAuthenticator } = require('ibm-cloud-sdk-core');
    const authenticator = new IamAuthenticator({ apikey: 'oXgdQ5fqeveFxKiRaanSV1HFaN9_msXDiHTDfV0kckY0' })
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
    });
    cloudant.setServiceUrl('https://16a3789a-76a2-4ffd-8d0b-d85ca4333270-bluemix.cloudantnosqldb.appdomain.cloud');
  
    try {
      if (params.st) {
        const result = await findDealershipByState(cloudant, params.st);
        const code = result.length ? 200 : 404;
        return {
          statusCode: code,
          headers: { 'Content-Type': 'application/json' },
          body: result
        };
      } else if (params.id) {
        const result = await findDealershipById(cloudant, params.id);
        const code = result.length ? 200 : 404;
        return {
          statusCode: code,
          headers: { 'Content-Type': 'application/json' },
          body: result
        };
      } else {
        const result = await findAllDealerships(cloudant);
        const code = result.length ? 200 : 404;
        return {
          statusCode: code,
          headers: { 'Content-Type': 'application/json' },
          body: result
        };
      }
    } catch (err) {
      console.error(err);
      return {
        statusCode: 500,
        headers: { 'Content-Type': 'application/json' },
        body: { error: 'Internal Server Error' }
      };
    }
  }
  
  async function findDealershipByState(cloudant, state) {
    const result = await cloudant.postFind({ db: 'dealerships', selector: { st: state } });
    return result.result.docs;
  }
  
  async function findDealershipById(cloudant, id) {
    const result = await cloudant.postFind({ db: 'dealerships', selector: { id: parseInt(id) } });
    return result.result.docs;
  }
  
  async function findAllDealerships(cloudant) {
    const result = await cloudant.postAllDocs({ db: 'dealerships', includeDocs: true, limit: 10 });
    return result.result.rows;
  }
  