/* eslint-disable */
const redis = require('redis');
const client = redis.createClient();
const { promisify } = require("util");
const getAsync = promisify(client.get).bind(client);


client.on('ready', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};
const displaySchoolValue =  async (schoolName) => {
  const value = await getAsync(schoolName);
  console.log(value);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
