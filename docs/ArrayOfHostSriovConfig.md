# ArrayOfHostSriovConfig

A boxed array of *HostSriovConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSriovConfig]**](HostSriovConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_sriov_config import ArrayOfHostSriovConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSriovConfig from a JSON string
array_of_host_sriov_config_instance = ArrayOfHostSriovConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSriovConfig.to_json()

# convert the object into a dict
array_of_host_sriov_config_dict = array_of_host_sriov_config_instance.to_dict()
# create an instance of ArrayOfHostSriovConfig from a dict
array_of_host_sriov_config_form_dict = array_of_host_sriov_config.from_dict(array_of_host_sriov_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


