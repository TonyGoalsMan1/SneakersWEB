<template>
  <div class="home-page">

    <!-- Герой секция -->
    <section class="hero">
      <div class="hero-overlay">
        <h1>Добро пожаловать в SneakerShop</h1>
        <p>Самые трендовые кроссовки по лучшим ценам!</p>
        <router-link to="/products" class="hero-btn">Купить сейчас</router-link>
      </div>
    </section>

    <!-- О нас -->
    <section class="info">
      <h2>О нас</h2>
      <p>
        Мы - интернет-магазин, специализирующийся на продаже кроссовок.
        У нас вы найдёте классические модели, последние новинки и эксклюзивные релизы.
      </p>
    </section>

    <!-- Секция популярных кроссовок -->
    <section class="products">
      <h2>Популярные кроссовки</h2>
      <div class="products-grid">
        <div v-for="sneaker in sneakers" :key="sneaker.id" class="product-card">
          <h3>{{ sneaker.name }}</h3>
          <p><strong>Цена:</strong> {{ sneaker.price }} ₽</p>
          <p><strong>Размер:</strong> {{ sneaker.size }}</p>
          <router-link :to="{ name: 'productDetails', params: { id: sneaker.id } }" class="details-btn">
            Подробнее
          </router-link>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      sneakers: [], // Список популярных кроссовок
    };
  },
  async mounted() {
    try {
      // Загружаем список популярных кроссовок
      const response = await axios.get("http://127.0.0.1:8000/sneakers/");
      this.sneakers = response.data; // Устанавливаем кроссовки в состояние
    } catch (error) {
      console.error("Ошибка загрузки кроссовок:", error.response?.data?.detail || error.message);
    }
  },
};
</script>

<style>
/* Оригинальные стили твоего файла */
body {
  margin: 0;
  font-family: Arial, sans-serif;
}

.nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 10px;
}

.nav a:hover,
.nav a.router-link-active {
  text-decoration: underline;
}

.hero {
  position: relative;
  width: 100%;
  height: 90vh;
  background: url('/hero-bg.jpg') center/cover no-repeat;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: #fff;
  padding: 20px;
}

.hero-overlay h1 {
  font-size: 3em;
  margin-bottom: 20px;
}

.hero-overlay p {
  font-size: 1.2em;
  margin-bottom: 30px;
}

.hero-btn {
  display: inline-block;
  background: #f90;
  color: #111;
  text-decoration: none;
  padding: 15px 30px;
  font-weight: bold;
  border-radius: 5px;
  font-size: 1em;
}

.hero-btn:hover {
  background: #ffa500;
}

.info {
  padding: 40px 20px;
  max-width: 1200px;
  margin: 0 auto;
  background: #fff;
  text-align: center;
  margin-top: 20px;
  border-radius: 5px;
}

.info h2 {
  margin-top: 0;
  font-size: 2em;
}

.info p {
  font-size: 1.1em;
  margin-top: 20px;
}

/* Новые стили для секции кроссовок */
.products {
  padding: 40px 20px;
  background: #f9f9f9;
  text-align: center;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.product-card {
  background: #fff;
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.product-card h3 {
  margin: 0 0 10px;
}

.product-card p {
  margin: 5px 0;
}

.details-btn {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 15px;
  background: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
}

.details-btn:hover {
  background: #0056b3;
}
</style>
