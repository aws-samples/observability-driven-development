var AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient()

exports.getByIdHandler = async (event, context) => {
  try {
    const id = event.pathParameters.id
    const item = await getItemById(id)
  
    return JSON.stringify(item.Items[0])
  } catch (ex) {
    console.error({functionVersion: context.functionVersion, exception: ex.message})
    return { statusCode: 500, body: JSON.stringify({ message: ex.message }) }
  }
}


const getItemById = async (id) => {
  let response
  try {
    var params = {
      TableName: process.env.SAMPLE_TABLE,
      KeyConditionExpression: "#id = :id",
      ExpressionAttributeNames:{
        "#id": "id"
      },
      ExpressionAttributeValues: {
        ":id": id
      }
    }

    response = await docClient.query(params).promise()
  } catch (err) {
    throw err
  }
  return response
}