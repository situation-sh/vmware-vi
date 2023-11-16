# QueryAvailableDvsSpecRequestType

The parameters of *DistributedVirtualSwitchManager.QueryAvailableDvsSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommended** | **bool** | If set to true, return only the recommended versions. If set to false, return only the not recommended versions. If unset, return all supported versions.  | [optional] 

## Example

```python
from vmware_vi.models.query_available_dvs_spec_request_type import QueryAvailableDvsSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAvailableDvsSpecRequestType from a JSON string
query_available_dvs_spec_request_type_instance = QueryAvailableDvsSpecRequestType.from_json(json)
# print the JSON string representation of the object
print QueryAvailableDvsSpecRequestType.to_json()

# convert the object into a dict
query_available_dvs_spec_request_type_dict = query_available_dvs_spec_request_type_instance.to_dict()
# create an instance of QueryAvailableDvsSpecRequestType from a dict
query_available_dvs_spec_request_type_form_dict = query_available_dvs_spec_request_type.from_dict(query_available_dvs_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


