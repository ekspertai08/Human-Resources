# import views.main_menu as main_menu

from models.DB_class import Base, engine

Base.metadata.create_all(engine)
