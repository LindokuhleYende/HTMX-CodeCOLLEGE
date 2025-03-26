import express from "express";
const app = express();
// Set static folder
app.use(express.static("public"));
// Parse URL-encoded bodies (as sent by HTML forms)
app.use(express.urlencoded({ extended: true }));
// Parse JSON bodies (as sent by API clients)
app.use(express.json());
// Handle POST request for contacts search


// Start the server
app.listen(3050, () => {
    console.log("Server listening on port 3050");
});
