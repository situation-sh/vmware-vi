# ArrayOfHostDeploymentInfo

A boxed array of *HostDeploymentInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDeploymentInfo]**](HostDeploymentInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_deployment_info import ArrayOfHostDeploymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDeploymentInfo from a JSON string
array_of_host_deployment_info_instance = ArrayOfHostDeploymentInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDeploymentInfo.to_json()

# convert the object into a dict
array_of_host_deployment_info_dict = array_of_host_deployment_info_instance.to_dict()
# create an instance of ArrayOfHostDeploymentInfo from a dict
array_of_host_deployment_info_form_dict = array_of_host_deployment_info.from_dict(array_of_host_deployment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


