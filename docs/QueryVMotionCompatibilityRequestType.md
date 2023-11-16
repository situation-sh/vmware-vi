# QueryVMotionCompatibilityRequestType

The parameters of *ServiceInstance.QueryVMotionCompatibility*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The group of hosts to analyze for compatibility.  Refers instances of *HostSystem*.  | 
**compatibility** | **List[str]** | The set of compatibility types to investigate. Each is a string chosen from VMotionCompatibilityType. If this argument is not set, then all compatibility types are investigated.  | [optional] 

## Example

```python
from vmware_vi.models.query_v_motion_compatibility_request_type import QueryVMotionCompatibilityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVMotionCompatibilityRequestType from a JSON string
query_v_motion_compatibility_request_type_instance = QueryVMotionCompatibilityRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVMotionCompatibilityRequestType.to_json()

# convert the object into a dict
query_v_motion_compatibility_request_type_dict = query_v_motion_compatibility_request_type_instance.to_dict()
# create an instance of QueryVMotionCompatibilityRequestType from a dict
query_v_motion_compatibility_request_type_form_dict = query_v_motion_compatibility_request_type.from_dict(query_v_motion_compatibility_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


