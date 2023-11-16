# ClearComplianceStatusRequestType

The parameters of *ProfileComplianceManager.ClearComplianceStatus*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If specified, clear the ComplianceResult related to the Profile.  ***Since:*** vSphere API 4.0  Refers instances of *Profile*.  | [optional] 
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If specified, clear the ComplianceResult related to the entity. If profile and entity are not specified, all the ComplianceResults will be cleared.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.clear_compliance_status_request_type import ClearComplianceStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ClearComplianceStatusRequestType from a JSON string
clear_compliance_status_request_type_instance = ClearComplianceStatusRequestType.from_json(json)
# print the JSON string representation of the object
print ClearComplianceStatusRequestType.to_json()

# convert the object into a dict
clear_compliance_status_request_type_dict = clear_compliance_status_request_type_instance.to_dict()
# create an instance of ClearComplianceStatusRequestType from a dict
clear_compliance_status_request_type_form_dict = clear_compliance_status_request_type.from_dict(clear_compliance_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


