from django.urls import include, path
from rest_framework import routers

from users.views import CustomUserViewSet
from api.v1.views import (
    SpecializationViewSet,
    CourseViewSet,
    LevelViewSet,
    ExperienceViewSet,
    EmploymentTypeViewSet,
    WorkScheduleViewSet,
    CandidateViewSet,
    HardCandsViewSet,
    LocationViewSet,
    VacancyViewSet,
    ExperienceDetailedViewSet,
    EducationViewSet,
    HardViewSet,
    )


app_name = "api.v1"


router = routers.DefaultRouter()

router.register("users", CustomUserViewSet, "users")
router.register("candidates", CandidateViewSet, "candidates")
router.register("experience_detailed", 
                ExperienceDetailedViewSet, "experience_detailed")
router.register("education", EducationViewSet, "education")
router.register("specialization_id", SpecializationViewSet)
router.register("course", CourseViewSet)
router.register("level_id", LevelViewSet)
router.register("experience_id", ExperienceViewSet)
router.register("employment_type", EmploymentTypeViewSet)
router.register("work_schedule", WorkScheduleViewSet)
router.register("hards_in_cands", HardCandsViewSet)
router.register("location", LocationViewSet)
router.register("vacancies", VacancyViewSet)
router.register("hard", HardViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("v1/candidates/<int:candidate_id>/download-candidate/", 
         CandidateViewSet.as_view({'get': 'download_candidate'})),
]