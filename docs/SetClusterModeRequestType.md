# SetClusterModeRequestType

The parameters of *FailoverClusterManager.setClusterMode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 

## Example

```python
from vmware_vi.models.set_cluster_mode_request_type import SetClusterModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetClusterModeRequestType from a JSON string
set_cluster_mode_request_type_instance = SetClusterModeRequestType.from_json(json)
# print the JSON string representation of the object
print SetClusterModeRequestType.to_json()

# convert the object into a dict
set_cluster_mode_request_type_dict = set_cluster_mode_request_type_instance.to_dict()
# create an instance of SetClusterModeRequestType from a dict
set_cluster_mode_request_type_form_dict = set_cluster_mode_request_type.from_dict(set_cluster_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


