
from typing import Any, List
from code.utils.file_util import FileUtil
from agent_framework._memory import ContextProvider as BaseContextProvider, Context

class ContextProvider(BaseContextProvider):
    """
    Context provider compatible with agent_framework, reads context from a file and returns a Context object.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    async def invoking(self, messages: List[Any], **kwargs) -> Context:
        content = FileUtil.read_file(self.file_path)
        return Context(instructions=content)
