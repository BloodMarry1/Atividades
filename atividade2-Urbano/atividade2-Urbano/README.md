## Explicação sobre Segurança e Hash (Atividade 2)

### 1. O que é uma função de hash e por que ela é irreversível?
Uma função de hash (como o SHA-256) é um algoritmo matemático que transforma qualquer entrada de texto (como uma senha) em uma sequência fixa de caracteres. Ela é considerada "irreversível" (ou uma função de mão única) porque é computacionalmente impossível reverter o hash gerado para descobrir qual era a senha original.

### 2. O que é o *salt* e que problema ele resolve?
O *salt* é uma sequência de dados aleatórios adicionada à senha antes de aplicar a função de hash. Ele resolve o problema dos ataques de dicionário e de *Rainbow Tables* (tabelas pré-calculadas). Sem o *salt*, dois usuários que escolhessem a mesma senha gerariam exatamente o mesmo hash no banco de dados, permitindo que um invasor descobrisse ambas de uma só vez. Com o *salt* único para cada usuário, hashes de senhas iguais tornam-se completamente diferentes.

### 3. Por que o *salt* pode ficar gravado ao lado do hash no banco sem ser segredo?
Porque a segurança do sistema não depende de manter o *salt* em segredo. O *salt* serve apenas para garantir que a mesma senha gere hashes diferentes para usuários diferentes e para dificultar ataques em massa. Para validar o login, o sistema precisa obrigatoriamente do *salt* associado àquele usuário específico para recalcular o hash da senha digitada e compará-la com a gravada no banco.