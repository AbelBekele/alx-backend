/* eslint-disable */
const redis = require('redis');
const client = redis.createClient();

const { promisify } = require('util');
const getAsync = promisify(client.hgetall).bind(client);

/* Function definitions */
const addDataToHash = (data, hashkey) => {
  for (const [key, value] of Object.entries(data)) {
    client.hset(hashkey, key, value, redis.print);
  }
};
const getDataFromHash = async (hashkey) => {
  const getAllData = await getAsync(hashkey);
  console.log(getAllData);
};

/* Setup params + Call functions */
const hashkey = 'HolbertonSchools';
const data = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};
addDataToHash(data, hashkey);
getDataFromHash(hashkey);
