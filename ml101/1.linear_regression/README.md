1. **Fórmula da Regressão Linear:**

   $ y = \theta_1 x + \theta_0 $

2. **Fórmula da Solução de Forma Fechada para Regressão Linear:**

   $ \theta_1 = (X^TX)^{-1}X^Ty $

   $ \theta_0 = \bar{y} - \theta_1 \bar{x} $

3. **Fórmula do Gradiente Descendente:**

   $ \theta_{\text{novo}} = \theta_{\text{antigo}} - \alpha \cdot \nabla_{\theta}J(\theta) $

   #### Erro Quadrático Médio (Mean Squared Error - MSE)

   $ J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)})^2 $

   ### Expandindo

   $ h_{\theta}(x) = \theta_1 x + \theta_0 $

   $ J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_{\theta}(x^{(i)}) - y^{(i)} \right)^2 $

   $ J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} \left( \theta_0 + \theta_1 x^{(i)} - y^{(i)} \right)^2 $

   Gradiente de $ \theta_0 $:
    $ \frac{1}{m} \sum_{i=1}^{m} \left( \theta_0 + \theta_1 x^{(i)} - y^{(i)} \right) $

   Gradiente de $ \theta_1 $:
    $ \frac{1}{m} \sum_{i=1}^{m} \left( \left( \theta_0 + \theta_1 x^{(i)} - y^{(i)} \right) x^{(i)} \right) $
