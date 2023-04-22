from app.models.activity import ActivityWithMessage
from app.queries.delete_activity_query import DeleteActivityQuery
from app.services.get_activities_service import GetActivityService


class DeleteActivityService:
    def __init__(self, activity_id: int):
        self.activity_id = activity_id

    def perform(self) -> ActivityWithMessage | None:
        activity = GetActivityService(activity_id=self.activity_id).perform()
        if not activity:
            return None

        deleting = DeleteActivityQuery(activity_id=activity.id)
        deleting.execute()
        if not deleting.is_successful:
            return ActivityWithMessage(activity=activity, message=deleting.error_message)

        return ActivityWithMessage(activity=activity)
