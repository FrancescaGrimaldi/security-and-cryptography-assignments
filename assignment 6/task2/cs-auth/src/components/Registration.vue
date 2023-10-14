<template>
    <div class="registrationbox">
        <h1>Registration</h1>
        <form @submit.prevent="register">
            <input v-model="usernameR" id="usernameR" type="text" placeholder="Username" class="inputbox"><br>
            <input v-model="passwordR" id="passwordR" type="password" placeholder="Password" class="inputbox"><br>
            <button type="submit">Register</button>
            <p v-if="resultMessage && isSuccessful()" style="color:green">{{ resultMessage }}</p>
            <p v-if="resultMessage && !isSuccessful()" style="color:red">{{ resultMessage }}</p>
        </form>
    </div>
</template>
  
<script>
    import CryptoJS from 'crypto-js';
    import { ref } from 'vue';
    import axios from 'axios';

    const baseURL = 'http://localhost:8080';

    export default {
        name: 'User-Registration',

        data() {
            return {
                usernameR: ref(''),
                passwordR: ref(''),
                resultMessage: ref(''),
            };
        },

        methods: {
            isSuccessful() {
                return this.resultMessage.includes('successful') || this.resultMessage.includes('successfully');
            },

            async register() {
                
                // Check if the username field is empty
                if (this.usernameR === null || this.usernameR === '') {
                    this.resultMessage = 'Username field cannot be empty';
                    return;
                }
                
                // Check if the password field is empty
                if (this.passwordR === null || this.passwordR === '') {
                    this.resultMessage = 'Password field cannot be empty';
                    return;
                }

                // Hash the password with PBKDF2 on the client side
                const salt = this.usernameR + 'saltsalt';
                const hashedPassword = CryptoJS.PBKDF2(this.passwordR, salt, { keySize: 64 / 4, iterations: 2048 }).toString();

                try {
                    // Send the registration request to the server
                    const response = await axios.post(`${baseURL}/register`, {
                        usernameR: this.usernameR,
                        passwordR: hashedPassword,
                    });

                    this.resultMessage = response.data.message;

                } catch (error) {
                    console.error(error);
                }
            },
        },
    };
</script>