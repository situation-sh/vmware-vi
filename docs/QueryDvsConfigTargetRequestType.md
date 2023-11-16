# QueryDvsConfigTargetRequestType

The parameters of *DistributedVirtualSwitchManager.QueryDvsConfigTarget*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**dvs** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_dvs_config_target_request_type import QueryDvsConfigTargetRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDvsConfigTargetRequestType from a JSON string
query_dvs_config_target_request_type_instance = QueryDvsConfigTargetRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDvsConfigTargetRequestType.to_json()

# convert the object into a dict
query_dvs_config_target_request_type_dict = query_dvs_config_target_request_type_instance.to_dict()
# create an instance of QueryDvsConfigTargetRequestType from a dict
query_dvs_config_target_request_type_form_dict = query_dvs_config_target_request_type.from_dict(query_dvs_config_target_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


