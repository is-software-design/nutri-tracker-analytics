import grpc
from concurrent import futures
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.entities.user import Base
import os
import time
from src.entities.dish import Dish
from src.entities.product import Product
from src.entities.eaten_item import EatenItem
import api_pb2
import api_pb2_grpc

username = os.getenv("db_username")
password = os.getenv("db_password")
host = os.getenv("db_host")
port = os.getenv("db_port")
dbname = os.getenv("db_name")

DATABASE_URL = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}'

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


class AnalyticService(api_pb2_grpc.AnalyticServiceServicer):
    def GetCaloriesStatistic(self, request, context):
        session = Session()
        eaten_items = session.query(EatenItem).filter((EatenItem.user_id == request.user_id) &
                                                      (EatenItem.date_time >= request.start_date) &
                                                      (EatenItem.date_time <= request.end_date)
                                                      ).all()
        c_sum = 0
        for i in eaten_items:
            if i.item_type == "dish":
                c_sum += session.query(Dish).filter_by(dish_id=i.item_id).first().total_calories
            else:
                c_sum += (session.query(Product).filter_by(
                    product_id=i.item_id).first().calories_per_100g * i.amount / 100)
        session.close()
        return api_pb2.GetCaloriesResponse(total_calories=c_sum)

def serve():
    port = os.getenv('PORT', '50056')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    api_pb2_grpc.add_AnalyticServiceServicer_to_server(AnalyticService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"gRPC server is running on port {port}...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
