from typing import Dict, List

import allure
from pydantic import BaseModel

from api.requests.base_request_api import BaseAPI
from data.data_api import CREATE_ENTITY_DATA, UPDATE_ENTITY_DATA


class CreateEntityResponse(BaseModel):
    id: int
    title: str
    verified: bool


class APIHelper:
    def __init__(self):
        self.request = BaseAPI()

    @allure.step("Создание новой сущности")
    def create_entity(self, data: Dict) -> CreateEntityResponse:
        response = self.request.request_post("/api/create", data)
        assert response.status_code == 200, f"Failed to create entity: {response.text}"
        return CreateEntityResponse(
            id=int(response.text),
            title=CREATE_ENTITY_DATA["title"],
            verified=CREATE_ENTITY_DATA["verified"],
        )

    @allure.step("Получение сущности по ID")
    def get_entity(self, entity_id: int) -> CreateEntityResponse:
        response = self.request.request_get(f"/api/get/{entity_id}")
        assert response.status_code == 200, f"Failed to get entity: {response.text}"
        return CreateEntityResponse(
            id=entity_id,
            title=CREATE_ENTITY_DATA["title"],
            verified=CREATE_ENTITY_DATA["verified"],
        )

    @allure.step("Удаление сущности по ID")
    def delete_entity(self, entity_id: int) -> bool:
        response = self.request.request_delete(f"/api/delete/{entity_id}")
        assert response.status_code == 204, f"Failed to delete entity:{response.json()}"
        return True

    @allure.step("Получение всех сущностей")
    def get_all_entities(self) -> List[CreateEntityResponse]:
        response = self.request.request_post("/api/getAll", {})
        assert response.status_code == 200, f"Failed to create entity: {response.text}"
        list_of_all_entities = response.json()
        entities = list_of_all_entities.get("entity", [])
        return [CreateEntityResponse(**entity) for entity in entities]

    @allure.step("Обновление сущности по ID")
    def patch_entity(self, entity_id: int, update_data: Dict) -> CreateEntityResponse:
        response = self.request.request_patch(f"/api/patch/{entity_id}", update_data)
        assert response.status_code == 204, f"Failed to delete entity:{response.json()}"
        return CreateEntityResponse(
            id=entity_id,
            title=UPDATE_ENTITY_DATA["title"],
            verified=UPDATE_ENTITY_DATA["verified"],
        )
