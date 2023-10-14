const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const cors = require('cors');
const app = express();
const port = 8080;

app.use(cors());

// "Database" for storing user data
const users = [];

// User registration endpoint
app.post('/register', bodyParser.json(), (req, res) => {
    const { usernameR, passwordR } = req.body;

    // Check if the username or password field is empty
    if(usernameR === null || usernameR === '' || passwordR === null || passwordR === ''){
        res.json({ message: 'Fields cannot be empty' });
        return;
    }
    
    // Check if a user with the same username already exists
    const user = users.find((u) => u.username === usernameR);

    if (user) {
        res.json({ message: 'User already exists' });
    } else {
        // Generate a salt and hash the password with the salt server side
        const salt = usernameR + 'saltsalt';
        const hashedPassword = crypto.pbkdf2Sync(passwordR, salt, 2048, 64 / 4, 'sha1').toString();
        // console.log('hashedPassword that will be stored: ', hashedPassword)

        // Store all the user data (username, salt, and hashed password)
        users.push({ username: usernameR, salt: salt, password: hashedPassword });
        res.json({ message: 'User registered successfully' });
    }
});

// User login endpoint
app.post('/login', bodyParser.json(), (req, res) => {
    const { usernameL, passwordL } = req.body;

    // Check if the username or password field is empty
    if(usernameL === null || usernameL === '' || passwordL === null || passwordL === ''){
        res.json({ message: 'Fields cannot be empty' });
        return;
    }

    // Find the user by username
    const user = users.find((u) => u.username === usernameL);
    if (!user) {
        res.json({ message: 'User not found' });
        return;
    }

    // Hash the provided password with the stored salt server side
    const hashedPassword = crypto.pbkdf2Sync(passwordL, user.salt, 2048, 64 / 4, 'sha1').toString();

    if (hashedPassword === user.password) {
        // Passwords match, login successful
        res.json({ message: 'Login successful' });
    } else {
        res.json({ message: 'Login failed' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
