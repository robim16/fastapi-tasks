from passlib.context import CryptContext

# archivo sólo para pruebas no es parte de la app;
#  fue generado para obtener un hash de una contraseña 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "admin123"
hash_value = pwd_context.hash(password)

print(hash_value)
