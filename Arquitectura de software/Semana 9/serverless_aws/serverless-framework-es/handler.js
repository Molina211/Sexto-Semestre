exports.hello = async (event) => {
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: "Go Serverless ! Your function executed successfully!",
      }),
    };
  };
  