from typing import Optional

from langchain.text_splitter import RecursiveCharacterTextSplitter

from embedchain.chunkers.base_chunker import BaseChunker
from embedchain.config.AddConfig import ChunkerConfig

TEXT_SPLITTER_CHUNK_PARAMS = {
    "chunk_size": 1000,
    "chunk_overlap": 100,
    "length_function": len,
}


class WikipediaChunker(BaseChunker):
    """Chunker for code docs site."""

    def __init__(self, config: Optional[ChunkerConfig] = None):
        if config is None:
            config = TEXT_SPLITTER_CHUNK_PARAMS
        text_splitter = RecursiveCharacterTextSplitter(**config)
        super().__init__(text_splitter)