from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Xeno CRM",
    description="AI-Native Marketing CRM Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from routes.auth_routes import router as auth_router
from routes.customer_routes import router as customer_router
from routes.product_routes import router as product_router
from routes.campaign_routes import router as campaign_router
from routes.ai_routes import router as ai_router
from routes.dashboard_routes import router as dashboard_router
from routes.analytics_routes import router as analytics_router
from routes.communication_routes import router as communication_router
from routes.segment_routes import router as segment_router
from routes.order_routes import router as order_router


app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(customer_router)
app.include_router(campaign_router)
app.include_router(ai_router)
app.include_router(order_router)
app.include_router(communication_router)
app.include_router(segment_router)
app.include_router(analytics_router)
app.include_router(product_router)




@app.get("/")
def home():
    
    return {
        "message": "Xeno CRM Backend Running"
    }