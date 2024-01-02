1. **Sigmoid (Função Logística)**

$ f(x) = \frac{1}{1 + e^{-x}} $

2. **Fórmula do Gradiente Descendente:**

$ \frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)}) x_j^{(i)} $

$ \theta_j := \theta_j - \alpha \frac{\partial J(\theta)}{\partial \theta_j} $

$\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^{m} ((\frac{1}{1 + e^{-\theta^T x^{(i)}}}) - y^{(i)}) x_j^{(i)}$

3. **Entropia Cruzada (Cross-Entropy Loss)**

$ J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)} log(h_{\theta}(x^{(i)})) + (1 - y^{(i)}) log(1 - h_{\theta}(x^{(i)}))] $
