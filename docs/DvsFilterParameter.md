# DvsFilterParameter

This class defines Network Filter parameter.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **List[str]** | List of parameters for a Network Filter.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_filter_parameter import DvsFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of DvsFilterParameter from a JSON string
dvs_filter_parameter_instance = DvsFilterParameter.from_json(json)
# print the JSON string representation of the object
print DvsFilterParameter.to_json()

# convert the object into a dict
dvs_filter_parameter_dict = dvs_filter_parameter_instance.to_dict()
# create an instance of DvsFilterParameter from a dict
dvs_filter_parameter_form_dict = dvs_filter_parameter.from_dict(dvs_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


