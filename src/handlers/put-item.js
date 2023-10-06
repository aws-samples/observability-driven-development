var AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient()
const cloudWatch = new AWS.CloudWatch()

exports.putItemHandler = async (event, context) => {
    try {
        const item = await putItem(event)
    
        return JSON.stringify(item)
    } catch (ex) {
        console.error({functionVersion: context.functionVersion, exception: ex.message})
        throw ex
    }
}

const putItem = async (event) => {
    let response
    try {
        let body = "";
        if (event.isBase64Encoded) {
            body = JSON.parse(Buffer.from(event.body, 'base64').toString('ascii'))
        } else {
            body = JSON.parse(event.body)
        }
        
        console.log("asdf1")
        
        const id = body.id
        const name = body.name
        const timestamp = Date.now()//body.timestamp
        const milesTraveled = body.milesTraveled
        const totalTravelTime = body.totalTravelTime
        const price = body.price
        
        const data = { id: id, name: name, timestamp: timestamp, milesTraveled: milesTraveled, totalTravelTime: totalTravelTime, price: price }
        
        var params = {
            TableName: process.env.ODDTable,
            Item: data
        }

        await docClient.put(params).promise()
        response = data
        const cwparams = {
            MetricData: [
            {
                'MetricName': 'TotalPrice',
                'Dimensions': 
                [
                    { 'Name': 'AppName', 'Value': 'Price' }
                ],
                
                'Value': price
            }
            ],
            Namespace: 'builder-session'
        };
        console.log(await cloudWatch.putMetricData(cwparams).promise())

    } catch (err) {
        throw err
    }
    return response
}