from typing import List, Optional, Tuple

from tableauserverclient.helpers.logging import logger
from tableauserverclient.models.linked_tasks_item import LinkedTaskItem
from tableauserverclient.models.pagination_item import PaginationItem
from tableauserverclient.server.endpoint.endpoint import QuerysetEndpoint, api
from tableauserverclient.server.request_options import RequestOptions

class LinkedTasks(QuerysetEndpoint[LinkedTaskItem]):
    def __init__(self, parent_srv):
        super().__init__(parent_srv)
        self._parent_srv = parent_srv

    @property
    def baseurl(self) -> str:
        return f"{self.parent_srv.baseurl}/sites/{self.parent_srv.site_id}/tasks/linked"

    @api(version="3.15")
    def get(self, req_options: Optional["RequestOptions"] = None) -> Tuple[List[LinkedTaskItem], PaginationItem]:
        logger.info("Querying all linked tasks on site")
        url = self.baseurl
        server_response = self.get_request(url, req_options)
        pagination_item = PaginationItem.from_response(server_response.content, self.parent_srv.namespace)
        all_group_items = LinkedTaskItem.from_response(server_response.content, self.parent_srv.namespace)
        return all_group_items, pagination_item

