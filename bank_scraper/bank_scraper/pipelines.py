# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# pipelines.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunkingPipeline:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=50,
            separators=["\n\n", "\n", ". ", " "]
        )

    def process_item(self, item, spider):
        content = item['content']
        chunks = self.text_splitter.split_text(content)
        item['chunks'] = chunks  # Store chunks in the item
        return item
