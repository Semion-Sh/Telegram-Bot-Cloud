import pytest
import sqlalchemy
from unittest.mock import AsyncMock
from Handlers.Client import commands_start, commands_help

class Test:
    @pytest.mark.asyncio
    async def test_commands_start(self):
        text_mock = "start"
        # text_help = 'help'
        message_mock = AsyncMock(text=text_mock)
        # message_help = AsyncMock(text=text_help)
        await commands_start(message=message_mock)
        # await commands_help(message=message_help)
        message_mock.answer.assert_called_with(text_mock)
        # message_help.answer.assert_called_with(text_help)

    @pytest.mark.asyncio
    async def test_commands_help(self):
        text_help = "help"
        message_help = AsyncMock(text=text_help)
        await commands_help(message=message_help)
        message_help.answer.assert_called_with(text_help)

