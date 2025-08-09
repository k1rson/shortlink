from datetime import datetime

from sqlalchemy import Integer, String, DateTime, Boolean, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class URL(Base):
    original_url: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="The original URL that the user provided to generate the short URL",
    )
    short_url: Mapped[str] = mapped_column(
        String(12),
        unique=True,
        index=True,
        nullable=False,
        comment="The shortened URL is generated from the original one.",
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, comment="The lifetime of a short link"
    )
    click_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="Number of times the short link was clicked",
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="A flag indicating whether the shortened link is currently active.",
    )

    __table_args__ = (
        CheckConstraint("length(short_url) >= 4", name="short_url_min_length"),
        CheckConstraint("length(short_url) <= 12", name="short_url_max_length"),
        CheckConstraint("click_count >= 0", name="click_count_non_negative"),
    )
