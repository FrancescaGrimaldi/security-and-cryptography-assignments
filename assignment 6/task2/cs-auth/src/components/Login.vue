<template>
    <div class="loginbox">
        <h1>Login</h1>
        <form @submit.prevent="login">
            <input v-model="usernameL" id="usernameL" type="text" placeholder="Username" class="inputbox"><br>
            <input v-model="passwordL" id="passwordL" type="password" placeholder="Password" class="inputbox"><br>
            <button type="submit">Login</button>
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
        name: 'User-Login',

        data() {
            return {
                usernameL: ref(''),
                passwordL: ref(''),
                resultMessage: ref(''),
            };
        },

        methods: {
            isSuccessful() {
                return this.resultMessage.includes('successful') || this.resultMessage.includes('successfully');
            },

            async login() {
                
                // Check if the username field is empty
                if (this.usernameL === null || this.usernameL === '') {
                    this.resultMessage = 'Username field cannot be empty';
                    return;
                }

                // Check if the password field is empty
                if (this.passwordL === null || this.passwordL === '') {
                    this.resultMessage = 'Password field cannot be empty';
                    return;
                }

                // Hash the password with PBKDF2 on the client side
                const salt = this.usernameL + 'saltsalt';
                const hashedPassword = CryptoJS.PBKDF2(this.passwordL, salt, { keySize: 64 / 4, iterations: 2048 }).toString();
                
                try {
                    // Send the login request to the server
                    const response = await axios.post(`${baseURL}/login`, {
                        usernameL: this.usernameL,
                        passwordL: hashedPassword,
                    });

                    this.resultMessage = response.data.message;

                } catch (error) {
                    console.error(error);
                }
            },
        },
    };
</script>