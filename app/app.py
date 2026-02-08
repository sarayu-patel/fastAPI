from fastapi import FastAPI
import asyncio
class application:
    def __init__(self):
        self.app=None
        
    def createApp(self,title, description,summary, lifespan=None):
        self.app=FastAPI(
            title=title,
            description=description,
            summary=summary,
            docs_url="/docs",
            redoc_url="/redocs",
            lifespan=lifespan,
            openapi_url="/openapi.json" 
        )
        return self.app
    
    async def lifespan(self):
        pass
    
    async def dependencies(self):
        pass
    
    async def middleware(self):
        pass
    
def getApp():
    app=application()
    app.createApp(title="srinivas social media platform",description="media platform",summary="srinivas begs sarayu")
    
    return app.app

app=getApp()
# if __name__=="__main__":
#     asyncio.run(getApp)
        
        