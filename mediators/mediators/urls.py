"""django_openhim_mediators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from claim_mediator.views import getClaims
from coverage_mediator.views import getCoverage
from organisation_mediator.views import getOrganisation
from group_mediator.views import getGroup
from patient_mediator.views import getPatient, savePreference, fetchSingleResource, subscriptionHandler
from practitioner_mediator.views import getPractitioner
from contract_mediator.views import getContract
from claimresponse_mediator.views import getClaimResponse
from coverageeligibilityrequest_mediator.views import getCoverageEligibilityRequest
from insuranceplan_mediator.views import getInsurancePlan
from location_mediator.views import getLocation


from coverage_mediator.views import registerCoverageMediator
from claim_mediator.views import registerClaimsMediator
from organisation_mediator.views import registerOrganisationMediator
from group_mediator.views import registerGroupMediator
from patient_mediator.views import registerPatientMediator
from contract_mediator.views import registerContractMediator
from claimresponse_mediator.views import registerClaimResponseMediator
from coverageeligibilityrequest_mediator.views import registerCoverageEligibilityRequestMediator
from insuranceplan_mediator.views import registerInsurancePlanMediator
from location_mediator.views import registerLocationMediator
from codesystem_mediator.views import getCodesystem
from medication_mediator.views import getMedication
from activitydefinition_mediator.views import getActivityDefinition


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api_fhir_r4/Claim', getClaims),
    path('api/api_fhir_r4/Coverage', getCoverage),
    path('api/api_fhir_r4/Organisation', getOrganisation),
    path('api/api_fhir_r4/Patient', getPatient),
    path('api/api_fhir_r4/Resource', fetchSingleResource),
    path('api/api_fhir_r4/SubscriptionHandler', subscriptionHandler),
    path('api/api_fhir_r4/Practitioner', getPractitioner),
    path('api/api_fhir_r4/Group', getGroup),
    path('api/api_fhir_r4/Location', getLocation),
    path('api/api_fhir_r4/Contract', getContract),
    path('api/api_fhir_r4/InsurancePlan', getInsurancePlan),
    path('api/api_fhir_r4/ClaimResponse', getClaimResponse),
    # path("api/api_fhir_r4/savePrefs", savePrefs),
    path("api/api_fhir_r4/savePreference", savePreference),
    path('api/api_fhir_r4/CoverageEligibilityRequest',
         getCoverageEligibilityRequest),
    path('api/api_fhir_r4/CodeSystem',
         getCodesystem),
    path('api/api_fhir_r4/Medication',
         getMedication),
    path('api/api_fhir_r4/ActivityDefinition',
         getActivityDefinition),
]

# register Mediators - once -- uncomment after setting up variables


# registerClaimsMediator()
# registerCoverageMediator()
# registerOrganisationMediator()
# registerGroupMediator()
# registerPatientMediator()
# registerContractMediator()
# registerClaimResponseMediator()
# registerCoverageEligibilityRequestMediator()
# registerInsurancePlanMediator
