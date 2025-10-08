exports.hello = async (event) => {
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: "Jhon Molina y Jhon Caviedes",
      }),
    };
  };
  