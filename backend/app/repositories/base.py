from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update
from app.database import Base


class BaseRepository:

    def __init__(self, model: type[Base], session: AsyncSession):
        self.model = model
        self.session = session

    async def find_all(self):
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def find_by(self, id: int):
        result = await self.session.get(self.model, id)
        if not result:
            raise HTTPException(status_code=404, detail="Not found")
        return result

    async def create(self, data):
        db_data = self.model(**data.model_dump())
        self.session.add(db_data)
        await self.session.commit()
        await self.session.refresh(db_data)
        return db_data

    async def edit(self, data, id: int):
        record = await self.find_by(id)
        if not record:
            raise HTTPException(status_code=404, detail="Not found")
        db_data = data.model_dump(exclude_unset=True)
        db_data["id"] = id
        await self.session.execute(update(self.model),[db_data])
        await self.session.commit()
        return await self.find_by(id)

    async def delete(self, id: int):
        record = await self.find_by(id)
        if not record:
            raise HTTPException(status_code=404, detail="Not found")
        await self.session.delete(record)
        await self.session.commit()
        return {"ok": True}
