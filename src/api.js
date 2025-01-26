import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // Базовый URL бекенда

export default {
  // Получение всех пользователей
  async getUsers() {
    const response = await axios.get(`${API_URL}/users/`);
    return response.data;
  },

  // Добавление пользователя
  async registerUser(username, password) {
    const response = await axios.post(`${API_URL}/register/`, {
      username,
      password,
    });
    return response.data;
  },

  // Получение всех кроссовок
  async getSneakers() {
    const response = await axios.get(`${API_URL}/sneakers/`);
    return response.data;
  },

  // Добавление кроссовок
  async addSneaker(sneaker) {
    const response = await axios.post(`${API_URL}/sneakers/`, sneaker);
    return response.data;
  },
};
