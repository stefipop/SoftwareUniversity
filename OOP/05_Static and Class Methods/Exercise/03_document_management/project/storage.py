from project.category import Category
from project.topic import Topic
from project.document import Document
from typing import List, Union

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def _find_and_operate(self, element_list: List[Union[Category, Topic, Document]], element_id: int, operation) -> None:
        for element in element_list:
            if element_id == element.id:
                operation(element)
                break

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self._find_and_operate(self.categories, category_id, lambda x: x.edit(new_name))

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self._find_and_operate(self.topics, topic_id, lambda x: x.edit(new_topic, new_storage_folder))

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self._find_and_operate(self.documents, document_id, lambda x: x.edit(new_file_name))

    def delete_category(self, category_id: int) -> None:
        self.categories = [category for category in self.categories if category.id != category_id]

    def delete_topic(self, topic_id: int) -> None:
        self.topics = [topic for topic in self.topics if topic.id != topic_id]

    def delete_document(self, document_id: int) -> None:
        self.documents = [doc for doc in self.documents if doc.id != document_id]

    def get_document(self, document_id: int) -> Document:
        for doc in self.documents:
            if document_id == doc.id:
                return doc

    def __repr__(self) -> str:
        return "\n".join(str(doc) for doc in self.documents)
