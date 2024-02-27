
const mongoose = require("mongoose");


const connectDB = async () =>
{
    try
    {
        await mongoose.connect(`mongodb+srv://${process.env.DB_NAME}:${process.env.DB_PASSWORD}@clustermaster.8jcj5di.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMaster`);
        console.log("Connected to MongoDB");
    }
        catch(error)
        {
            console.log(error);
        }
};

module.exports = {connectDB};


