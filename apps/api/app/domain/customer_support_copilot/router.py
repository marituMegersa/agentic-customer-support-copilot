from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.customer_support_copilot.schemas import AgenticCustomerSupportCopilotSessionCreate, AgenticCustomerSupportCopilotSessionResponse
from app.domain.customer_support_copilot.service import AgenticCustomerSupportCopilotService

router = APIRouter(prefix="/api/v1/customer_support_copilot", tags=["Agentic Customer Support Copilot Domain"])

@router.post("/sessions", response_model=AgenticCustomerSupportCopilotSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCustomerSupportCopilotSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Customer Support Copilot.
    """
    return AgenticCustomerSupportCopilotService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCustomerSupportCopilotSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCustomerSupportCopilotService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
