# QueryFaultToleranceCompatibilityExRequestType

The parameters of *VirtualMachine.QueryFaultToleranceCompatibilityEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_legacy_ft** | **bool** | checks for legacy record-replay FT compatibility only if this is set to true.  | [optional] 

## Example

```python
from vmware_vi.models.query_fault_tolerance_compatibility_ex_request_type import QueryFaultToleranceCompatibilityExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFaultToleranceCompatibilityExRequestType from a JSON string
query_fault_tolerance_compatibility_ex_request_type_instance = QueryFaultToleranceCompatibilityExRequestType.from_json(json)
# print the JSON string representation of the object
print QueryFaultToleranceCompatibilityExRequestType.to_json()

# convert the object into a dict
query_fault_tolerance_compatibility_ex_request_type_dict = query_fault_tolerance_compatibility_ex_request_type_instance.to_dict()
# create an instance of QueryFaultToleranceCompatibilityExRequestType from a dict
query_fault_tolerance_compatibility_ex_request_type_form_dict = query_fault_tolerance_compatibility_ex_request_type.from_dict(query_fault_tolerance_compatibility_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


