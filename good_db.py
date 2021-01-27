from sqlalchemy import create_engine, Column, \
    Integer, Float, String, Date, Interval, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship
import os

DB_NAME = 'postgres'
HOST_NAME = '127.0.0.1'
USER_NAME = 'postgres'
PASS = os.environ.get('CONPASS')

engine = create_engine('postgresql+psycopg2://{user}:{pwd}@{host}/{dbname}'
                       .format(dbname=DB_NAME,
                               host=HOST_NAME,
                               user=USER_NAME,
                               pwd=PASS
                               ),
                       echo=False
                       )


Base = declarative_base()


class Good(Base):
    __tablename__ = 'goods'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    cost = Column('cost', Float, nullable=False)
    count = Column('count', Integer, nullable=False)
    made_date = Column('made_date', Date, nullable=False)
    delivery_id = Column('delivery_id', Integer, ForeignKey('deliveries.id'))
    delivery = relationship("Delivery", back_populates="goods")
    suitability_id = Column('suitability_id', Integer, ForeignKey('suitabilities.id'))
    suitability = relationship("Suitability", back_populates="goods")
    provider_id = Column('provider_id', Integer, ForeignKey('providers.id'))
    provider = relationship("Provider", back_populates="goods")


class Provider(Base):
    __tablename__ = 'providers'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    goods = relationship("Good", back_populates="provider")


class Delivery(Base):
    __tablename__ = 'deliveries'
    id = Column('id', Integer, primary_key=True)
    delivery_date = Column('delivery_date', Date, nullable=False)
    goods = relationship("Good", back_populates="delivery")


class Suitability(Base):
    __tablename__ = 'suitabilities'
    id = Column('id', Integer, primary_key=True)
    expiration_time = Column('expiration_time', Interval, nullable=False)
    goods = relationship("Good", back_populates="suitability")


def create_tables():
    """
    This function creates tables 'goods', 'providers', 'deliveries' and

    'suitabilities' in postgres data base.
    """
    engine.connect()
    metadata = MetaData(bind=engine)
    metadata.reflect()
    metadata.drop_all(bind=engine)

    Base.metadata.create_all(engine)


def file_to_db(file_path):
    """
    This function transfers goods data from text file to postgres data base.

    :param file_path: path to text file
    :type file_path: str
    """
    engine.connect()
    session = Session(bind=engine)
    try:
        open_file = open(file_path, "r", encoding="utf-8")
        rows = open_file.readlines()
        open_file.close()
    except Exception:
        print('Не удалось открыть файл')
    if not rows or len(rows) == 0:
        print('Пустой файл!')
        return
    for row in rows:
        list_row = row.split(":")
        if len(list_row) < 7:
            print("Нет данных о товаре")
            continue
        elif not list_row[1].isdigit() or not list_row[2].isdigit():
            print("Неверный формат данных")
            continue
        elif int(list_row[5]) < 0:
            print("Срок годности < 0")
            continue
        list_row[6] = list_row[6].replace("\n", "")
        name = list_row[0]
        cost = float(list_row[1])
        count = int(list_row[2])
        made_date = list_row[3]
        delivery_date = list_row[4]
        expiration_time = int(list_row[5])
        provider = list_row[6]

        exist_provider = session.query(Provider)\
            .filter(Provider.name == provider).first()
        exist_delivery = session.query(Delivery)\
            .filter_by(delivery_date=delivery_date).first()
        exist_suitability = session.query(Suitability)\
            .filter_by(expiration_time=expiration_time).first()
        if not exist_provider:
            exist_provider = Provider(name=provider)
            session.add(exist_provider)
        if not exist_delivery:
            exist_delivery = Delivery(delivery_date=delivery_date)
            session.add(exist_delivery)
        if not exist_suitability:
            exist_suitability = Suitability(expiration_time=expiration_time)
            session.add(exist_suitability)
        new_good = Good(name=name, cost=cost, count=count, made_date=made_date)
        new_good.provider = exist_provider
        new_good.delivery = exist_delivery
        new_good.suitability = exist_suitability
        session.add(new_good)

        session.commit()


def add_to_db(product):
    """
    This function adds data from GoodInfo instance to postgres data base.

    :param product: GoodInfo instance
    :type product: object
    """
    session = Session(bind=engine)

    exist_provider = session.query(Provider)\
        .filter(Provider.name == product.provider).first()
    exist_delivery = session.query(Delivery)\
        .filter(Delivery.delivery_date == product.delivery_date).first()
    exist_suitability = session.query(Suitability)\
        .filter(Suitability.expiration_time == product.expiration_time).first()
    if not exist_provider:
        exist_provider = Provider(name=product.provider)
        session.add(exist_provider)
    if not exist_delivery:
        exist_delivery = Delivery(delivery_date=product.delivery_date)
        session.add(exist_delivery)
    if not exist_suitability:
        exist_suitability = Suitability(expiration_time=product.expiration_time)
        session.add(exist_suitability)
    new_good = Good(name=product.name, cost=product.cost, count=product.count,
                    made_date=product.made_date)
    new_good.provider = exist_provider
    new_good.delivery = exist_delivery
    new_good.suitability = exist_suitability
    session.add(new_good)

    session.commit()


def drop_from_db(name, made_date):
    """
    This function deletes instance of Good from 'goods' table.

    :param name: name of Good instance
    :type name: str
    :param made_date: delivery date from related Delivery instance
    :type made_date: date
    """
    session = Session(bind=engine)

    drop_good = session.query(Good).filter(Good.name == name)\
        .filter(Good.made_date == made_date).one()
    session.delete(drop_good)

    session.commit()


def update_count_db(name, made_date, count):
    session = Session(bind=engine)

    update_good = session.query(Good).filter(Good.name == name)\
        .filter(Good.made_date == made_date).one()
    update_good.count = count

    session.commit()
