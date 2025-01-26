<template>
  <header class="header">

    <div class="logo">SneakerShop</div>


    <nav class="nav">
      <router-link to="/">Главная</router-link>
      <router-link to="/products">Каталог</router-link>
      <router-link to="/auth">Войти / Регистрация</router-link>
    </nav>
  </header>

  <router-view></router-view>

  <footer class="footer">
    <p>&copy; 2024 SneakerShop. Все права защищены.</p>
  </footer>

</template>


<style>

body {
  margin: 0;
  font-family: Arial, sans-serif;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #111;
  color: #fff;
  padding: 10px 20px;
}
.logo {
  font-size: 1.5em;
  font-weight: bold;
}
.nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 10px;
}
.nav a:hover, .nav a.active {
  text-decoration: underline;
}
.footer {
  text-align: center;
  padding: 20px;
  background: #111;
  color: #fff;
  margin-top: 20px;
}
</style>
