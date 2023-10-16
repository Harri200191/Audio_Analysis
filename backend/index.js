const express = require("express");

const app = express();
const PORT = process.env.PORT || 5000;


app.get("/", (req, resp) => {
    resp.send("Home Page");
});

const startserver = async () => {
    try{
        app.listen(PORT, () => {
            console.log("Server running on port: ", PORT);
        });
    }
    catch (error){
        console.warn(error)
    };
};

startserver();
