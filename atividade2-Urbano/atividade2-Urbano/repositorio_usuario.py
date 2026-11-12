# -*- coding: utf-8 -*-
import hashlib
import secrets
from conexao import conectar

def _gerar_hash(senha, salt):
    """Calcula o hash SHA-256 da senha usando o salt (usado no cadastro e no login)."""
    dk = hashlib.pbkdf2_hmac(
        'sha256',
        senha.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    )
    return dk.hex()

def preparar_senha(senha):
    """Gera um salt de 16 bytes (32 hex) e o hash da senha (64 hex)."""
    salt = secrets.token_hex(16)
    senha_hash = _gerar_hash(senha, salt)
    return senha_hash, salt

def verificar_login(login, senha):
    """Verifica se o login e a senha conferem no banco. Devolve o nome ou None."""
    with conectar() as conexao:
        cursor = conexao.cursor()
        sql = "SELECT nome, senha_hash, salt FROM usuario WHERE login = %s"
        cursor.execute(sql, (login,))
        resultado = cursor.fetchone()
        
        if not resultado:
            return None
            
        nome, senha_hash_banco, salt_banco = resultado
        
        senha_hash_digitada = _gerar_hash(senha, salt_banco)
        
        if senha_hash_digitada == senha_hash_banco:
            return nome
        
        return None