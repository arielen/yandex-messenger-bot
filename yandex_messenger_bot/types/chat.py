from yandex_messenger_bot.enums import ChatType
from yandex_messenger_bot.types.base import YaBotObject


class Chat(YaBotObject):
    """Represents a chat (private, group, or channel)."""

    id: str | None = None
    type: ChatType
    organization_id: str | None = None
    title: str | None = None
    description: str | None = None
    thread_id: int | None = None

    @property
    def is_channel(self) -> bool:
        """Whether this chat is a channel.

        Derived from :attr:`type` — the only documented channel indicator. A
        wire-level ``is_channel`` field has never been confirmed in a live
        update, so ``type`` is authoritative. See docs/api-inconsistencies.md (#9).
        """
        return self.type == ChatType.CHANNEL
