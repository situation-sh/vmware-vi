# ArrayOfHostDateTimeConfig

A boxed array of *HostDateTimeConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDateTimeConfig]**](HostDateTimeConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_date_time_config import ArrayOfHostDateTimeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDateTimeConfig from a JSON string
array_of_host_date_time_config_instance = ArrayOfHostDateTimeConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDateTimeConfig.to_json()

# convert the object into a dict
array_of_host_date_time_config_dict = array_of_host_date_time_config_instance.to_dict()
# create an instance of ArrayOfHostDateTimeConfig from a dict
array_of_host_date_time_config_form_dict = array_of_host_date_time_config.from_dict(array_of_host_date_time_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


