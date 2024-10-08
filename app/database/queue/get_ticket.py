from sqlalchemy import select

from app.database.models.ticket import Ticket
from app.database.models.engine import async_session


async def get_ticket(ticket_id: int) -> Ticket | None:
    async with async_session() as session:
        async with session.begin():
            ticket = await session.scalar(select(Ticket).where(Ticket.ticket_id == ticket_id))

            data = []

            if ticket:
                data.append(ticket.ticket_id)
                data.append(ticket.telegram_id)
                data.append(ticket.chat_id)
            else:
                return None

            return data