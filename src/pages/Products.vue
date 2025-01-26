<template>
  <div class="products-page">

    <section class="products">
      <h1>Каталог Кроссовок</h1>
      <div class="product-list">
        <div
          class="product-card"
          v-for="(product, index) in products"
          :key="index"
        >
          <img :src="product.image || '/placeholder.jpg'" :alt="product.name" />
          <h2>{{ product.name }}</h2>
          <p>Цена: {{ product.price }} руб.</p>
          <p>Размер: {{ product.size }}</p>
          <button @click="addToCart(product)">Купить</button>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductsPage",
  data() {
    return {
      products: [], // Список продуктов из базы данных
    };
  },
  async created() {
    try {
      // Запрос данных о кроссовках из API
      const response = await axios.get("http://127.0.0.1:8000/sneakers/");
      this.products = response.data;
    } catch (error) {
      console.error("Ошибка загрузки данных:", error.response?.data?.detail || error.message);
    }
  },
  methods: {
    addToCart(product) {
      alert(`Кроссовки "${product.name}" добавлены в корзину!`);
    },
  },
};
</script>

<style scoped>
.products {
  padding: 20px;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
  flex: 1 1 calc(25% - 20px);
  box-sizing: border-box;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.product-card img {
  width: 100%;
  height: 200px;
  object-fit: contain;
  background: #fff;
  border-radius: 5px;
  margin-bottom: 10px;
  transition: transform 0.3s ease;
}

.product-card:hover img {
  transform: scale(1.05);
}

.product-card h2 {
  margin: 10px 0 5px 0;
  font-size: 1.2em;
}

.product-card p {
  margin: 5px 0;
}

.product-card button {
  background: #111;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: auto;
}

.product-card button:hover {
  background: #333;
}

@media (max-width: 768px) {
  .product-list {
    flex-direction: column;
  }
  .product-card {
    flex: 1 1 100%;
  }
}
</style>
