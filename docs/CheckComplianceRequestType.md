# CheckComplianceRequestType

The parameters of *ProfileComplianceManager.CheckCompliance_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If specified, check compliance against the specified profiles. If not specified, use the profiles associated with the entities. If both Profiles and Entities are specified, Check the compliance of each Entity against each of the profile specified.    For more information, look at the KMap below.    P represents if Profile is specified.    E represents if Entity is specified.                  P                        ^P       ---------------------------------------------------       | Check compliance      |  Profiles associated    |      E|  of each entity       |   with the specified    |       |  against each of the  |   entity will be used   |       |  profiles specified.  |   for checking          |       |                       |   compliance.           |       |                       |                         |       |                       |                         |       ---------------------------------------------------       | All entities          |   InvalidArgument       |       |  associated with the  |   Exception is thrown.  |       |  profile are checked. |                         |     ^E|                       |                         |       |                       |                         |       |                       |                         |       |                       |                         |       ---------------------------------------------------  ***Since:*** vSphere API 4.0  Refers instances of *Profile*.  | [optional] 
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If specified, the compliance check is done against this entity.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.check_compliance_request_type import CheckComplianceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckComplianceRequestType from a JSON string
check_compliance_request_type_instance = CheckComplianceRequestType.from_json(json)
# print the JSON string representation of the object
print CheckComplianceRequestType.to_json()

# convert the object into a dict
check_compliance_request_type_dict = check_compliance_request_type_instance.to_dict()
# create an instance of CheckComplianceRequestType from a dict
check_compliance_request_type_form_dict = check_compliance_request_type.from_dict(check_compliance_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


