# ArrayOfHostConfigSummary

A boxed array of *HostConfigSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConfigSummary]**](HostConfigSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_config_summary import ArrayOfHostConfigSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConfigSummary from a JSON string
array_of_host_config_summary_instance = ArrayOfHostConfigSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConfigSummary.to_json()

# convert the object into a dict
array_of_host_config_summary_dict = array_of_host_config_summary_instance.to_dict()
# create an instance of ArrayOfHostConfigSummary from a dict
array_of_host_config_summary_form_dict = array_of_host_config_summary.from_dict(array_of_host_config_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


