# Microsserviços + DevOps  
## currency-report & currency-history

Este projeto implementa dois microsserviços simples (mockados), integrados via Docker Compose e com pipeline básico de CI usando GitHub Actions.

---

## 📌 Arquitetura dos Microsserviços

### 1) currency-report
Fornece dados de câmbio atuais (mock).

**Endpoints:**
- `GET /health`  
  → `{ "status": "UP" }`
- `GET /quote?from=USD&to=BRL`  
  → Exemplo:  
    ```json
    { 
      "from": "USD",
      "to": "BRL",
      "price": 5.42,
      "timestamp": "2025-01-01T12:00:00Z"
    }
    ```

---

### 2) currency-history
Fornece um histórico recente de valores de câmbio (mockado).

**Endpoints:**
- `GET /health`
- `GET /history?from=USD&to=BRL`  
  → Exemplo:
    ```json
    {
      "from": "USD",
      "to": "BRL",
      "values": [
        { "timestamp": "...", "price": 5.42 },
        { "timestamp": "...", "price": 5.47 }
      ]
    }
    ```

---

## 🐳 Como subir o ambiente

Certifique-se de que Docker e Docker Compose estão instalados.

```bash
docker compose up --build
```

## Curls para teste:
 
### 1) currency-report

Health:
```bash
curl http://localhost:8100/health
```
Cotação:
```bash
curl "http://localhost:8100/quote?from=USD&to=BRL"
```
### 2) currency-history
Health:
```bash
curl http://localhost:8101/health
```
Cotação:
```bash
curl "http://localhost:8101/history?from=USD&to=BRL"
```

## CI - GitHub Actions
Pipeline localizado em:
```bash
.github/workflows/ci.yml
```
### Link diretório github:
```bash
https://github.com/RianCV/trab_ES_II
```