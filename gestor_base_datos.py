from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

# Crear la base y el motor de SQLAlchemy
Base = declarative_base()
engine = create_engine('sqlite:///planificador_fiestas.db', echo=False)
Session = sessionmaker(bind=engine)

class PlanFiesta(Base):
    __tablename__ = 'planes_fiesta'
    
    id = Column(Integer, primary_key=True)
    tema = Column(String)
    invitados = Column(Integer)
    presupuesto = Column(Float)
    plan_comida = Column(String)
    plan_musica = Column(String)
    plan_decoracion = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.now)
    
    def a_diccionario(self):
        return {
            'id': self.id,
            'theme': self.tema,
            'guests': self.invitados,
            'budget': self.presupuesto,
            'food_plan': self.plan_comida,
            'music_plan': self.plan_musica,
            'decoration_plan': self.plan_decoracion,
            'created_at': self.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
        }

class GestorBaseDatos:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()
    
    def guardar_plan_fiesta(self, tema, invitados, presupuesto, plan_comida, plan_musica, plan_decoracion):
        """Guarda un nuevo plan de fiesta en la base de datos"""
        nuevo_plan = PlanFiesta(
            tema=tema,
            invitados=invitados,
            presupuesto=presupuesto,
            plan_comida=plan_comida,
            plan_musica=plan_musica,
            plan_decoracion=plan_decoracion
        )
        self.session.add(nuevo_plan)
        self.session.commit()
        return nuevo_plan.id
    
    def obtener_plan_fiesta(self, plan_id):
        """Obtiene un plan de fiesta específico"""
        plan = self.session.query(PlanFiesta).filter(PlanFiesta.id == plan_id).first()
        return plan.a_diccionario() if plan else None
    
    def obtener_fiestas_similares(self, tema, presupuesto, rango_presupuesto=0.2):
        """Busca fiestas similares basadas en el tema y un rango de presupuesto"""
        min_presupuesto = presupuesto * (1 - rango_presupuesto)
        max_presupuesto = presupuesto * (1 + rango_presupuesto)
        
        fiestas_similares = self.session.query(PlanFiesta).filter(
            PlanFiesta.tema.ilike(f"%{tema}%"),
            PlanFiesta.presupuesto.between(min_presupuesto, max_presupuesto)
        ).all()
        
        return [fiesta.a_diccionario() for fiesta in fiestas_similares]
    
    def obtener_estadisticas_fiesta(self):
        """Obtiene estadísticas generales de las fiestas planificadas"""
        total_fiestas = self.session.query(PlanFiesta).count()
        
        if total_fiestas == 0:
            return {
                'total_parties': 0,
                'average_budget': 0,
                'average_guests': 0
            }
            
        avg_presupuesto = self.session.query(func.avg(PlanFiesta.presupuesto)).scalar() or 0
        avg_invitados = self.session.query(func.avg(PlanFiesta.invitados)).scalar() or 0
        
        return {
            'total_parties': total_fiestas,
            'average_budget': round(avg_presupuesto, 2),
            'average_guests': round(avg_invitados, 2)
        }
    
    def cerrar(self):
        """Cierra la sesión de la base de datos"""
        self.session.close() 