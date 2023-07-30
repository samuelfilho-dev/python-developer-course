from sqlalchemy import Column, func
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    # Atributos
    id = Column(Integer, primary_key=True)  # Primary Key
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)  # Primary Key
    email_address = Column(String(30), nullable=False)  # String com tamanho 30 # Não Permitir Nulo
    user_id = Column(Integer,
                     ForeignKey("user_account.id"),
                     nullable=False)  # FK relacionando com 'user_account' usando id como atributo

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# Conexão Com o Banco De Dados
engine = create_engine("sqlite://")

# Criando as Classes como Tabelas no Banco De Dados
Base.metadata.create_all(engine)

# Investiga o Esquema De Banco De Dados
inspector_engine = inspect(engine)

print(inspector_engine.has_table("user_account"))  # has_table - Verifica se tem tabela, retorna um Booleano
print(inspector_engine.get_table_names())  # get_table_names - Retorna a lista de nomes das tabelas do BD
print(inspector_engine.default_schema_name)  # default_schema_name - Retorna o Nome do Schema

with Session(engine) as session:
    # Criar os Objetos que irão instanciar a Base De Dados
    Juliana = User(
        name="juliana",
        fullname="Juliana Mascarenhas",
        address=[Address(email_address='julianam@email.com')]
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cardoso",
        # Sera criado dois emails relacionado do a Sandy
        address=[Address(email_address='sandy@email.br'), Address(email_address='sandyc@email.org')]
    )
    patrick = User(name='Patrick', fullname="Patrick Cardoso")

    session.add_all([Juliana, sandy, patrick])  # Enviando para o Banco De Dados(Persitência de Dados)

    session.commit()

# Query para Verificar de Acordo com o Nome
stmt = select(User).where(User.name.in_(["juliana", 'sandy']))

print("Recuperando Usuarios a partir de Condição De Filtragem")
for user in session.scalars(stmt):  # Anda pela sessão com a escala, logo retornado com as intancias da Base De Dados
    print(user)

# Query para Verificar de Acordo com id De Usuario
stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando os Endereços De Sandy")
for address in session.scalars(stmt_address):
    print(address)

# Query Para ordernar os Usuarios de Acordo com nome em ordem Decresente
stmt_order = select(User).order_by(User.fullname)

print("\nRecuperando Info de Maneira Ordenada")
for result in session.scalars(stmt_order):
    print(result)

# Query de Busca De Informações com as tabelas relacionadas
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print("\n")
for result in session.scalars(
        stmt_join):  # scalars - Pega apenas o primeiro resultado, join não consegue com esse metodo
    print(result)

conneciton = engine.connect()  # Criar uma conexão no Banco De Dados
results = (conneciton.execute(stmt_join)  # Execulta a Query na conexão
           .fetchall())  # Pega todos o Resultados da Query Criada

print("\nExecutando statement a partir da Connection")
for result in results:
    print(result)

# Query Para Contagem Das Instâncias Na Tabela 'User'
stmt_count = select(func.count('*')).select_from(User)

print("\n Total De Instâncias em User")
for result in session.scalars(stmt_count):
    print(result)

# Fechar a Sessão
session.close()
