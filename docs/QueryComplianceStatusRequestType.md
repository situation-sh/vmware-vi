# QueryComplianceStatusRequestType

The parameters of *ProfileComplianceManager.QueryComplianceStatus*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If specified, compliance result for the specified profiles will be returned. This acts like a filtering criteria for the ComplianceResults based on specified profiles.  ***Since:*** vSphere API 4.0  Refers instances of *Profile*.  | [optional] 
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If specified, compliance results for these entities will be returned. This acts like a filtering criteria for the ComplianceResults based on entities.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.query_compliance_status_request_type import QueryComplianceStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryComplianceStatusRequestType from a JSON string
query_compliance_status_request_type_instance = QueryComplianceStatusRequestType.from_json(json)
# print the JSON string representation of the object
print QueryComplianceStatusRequestType.to_json()

# convert the object into a dict
query_compliance_status_request_type_dict = query_compliance_status_request_type_instance.to_dict()
# create an instance of QueryComplianceStatusRequestType from a dict
query_compliance_status_request_type_form_dict = query_compliance_status_request_type.from_dict(query_compliance_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


