from Auth.models import CompanyUser
from companies.models import Job, Company


def getMessage(pk:int)->str:
    job=Job.objects.get(id=pk)
    return "Someone send a response to your job "+job.Name




def getReciver(pk:int)->str:
    job = Job.objects.get(id=pk)
    hr= CompanyUser.objects.get(company=job.Company)
    return hr.user.email