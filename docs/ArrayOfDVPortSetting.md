# ArrayOfDVPortSetting

A boxed array of *DVPortSetting*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVPortSetting]**](DVPortSetting.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dv_port_setting import ArrayOfDVPortSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVPortSetting from a JSON string
array_of_dv_port_setting_instance = ArrayOfDVPortSetting.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVPortSetting.to_json()

# convert the object into a dict
array_of_dv_port_setting_dict = array_of_dv_port_setting_instance.to_dict()
# create an instance of ArrayOfDVPortSetting from a dict
array_of_dv_port_setting_form_dict = array_of_dv_port_setting.from_dict(array_of_dv_port_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


