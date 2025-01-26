<template>
  <div class="auth-page">
    <section class="auth">
      <h1>Войти в аккаунт</h1>
      <form @submit.prevent="login" class="login-form">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />

        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="password" required />

        <button type="submit">Войти</button>
      </form>
      <p>Нет аккаунта? <a href="#" @click.prevent="registerRedirect">Зарегистрируйтесь</a></p>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/login/", {
          username: this.email,
          password: this.password,
        });
        localStorage.setItem("token", response.data.access_token);
        alert("Вы успешно вошли!");
        this.$router.push("/home");
      } catch (error) {
        alert("Ошибка авторизации: " + (error.response?.data?.detail || "Неизвестная ошибка"));
      }
    },
    registerRedirect() {
      this.$router.push("/register"); // Реализуйте регистрацию при необходимости
    },
  },
};
</script>

<style>
.auth {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.login-form input {
  margin-bottom: 10px;
  padding: 5px;
}

.login-form button {
  background: #111;
  color: #fff;
  border: none;
  padding: 10px;
  cursor: pointer;
}
</style>
