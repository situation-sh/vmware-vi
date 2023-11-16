# ArrayOfOvfDeploymentOption

A boxed array of *OvfDeploymentOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfDeploymentOption]**](OvfDeploymentOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_deployment_option import ArrayOfOvfDeploymentOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfDeploymentOption from a JSON string
array_of_ovf_deployment_option_instance = ArrayOfOvfDeploymentOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfDeploymentOption.to_json()

# convert the object into a dict
array_of_ovf_deployment_option_dict = array_of_ovf_deployment_option_instance.to_dict()
# create an instance of ArrayOfOvfDeploymentOption from a dict
array_of_ovf_deployment_option_form_dict = array_of_ovf_deployment_option.from_dict(array_of_ovf_deployment_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


