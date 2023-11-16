# ArrayOfHostConfigFailed

A boxed array of *HostConfigFailed*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConfigFailed]**](HostConfigFailed.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_config_failed import ArrayOfHostConfigFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConfigFailed from a JSON string
array_of_host_config_failed_instance = ArrayOfHostConfigFailed.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConfigFailed.to_json()

# convert the object into a dict
array_of_host_config_failed_dict = array_of_host_config_failed_instance.to_dict()
# create an instance of ArrayOfHostConfigFailed from a dict
array_of_host_config_failed_form_dict = array_of_host_config_failed.from_dict(array_of_host_config_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


