# ArrayOfVMwareDVSPortSetting

A boxed array of *VMwareDVSPortSetting*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VMwareDVSPortSetting]**](VMwareDVSPortSetting.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_mware_dvs_port_setting import ArrayOfVMwareDVSPortSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVMwareDVSPortSetting from a JSON string
array_of_v_mware_dvs_port_setting_instance = ArrayOfVMwareDVSPortSetting.from_json(json)
# print the JSON string representation of the object
print ArrayOfVMwareDVSPortSetting.to_json()

# convert the object into a dict
array_of_v_mware_dvs_port_setting_dict = array_of_v_mware_dvs_port_setting_instance.to_dict()
# create an instance of ArrayOfVMwareDVSPortSetting from a dict
array_of_v_mware_dvs_port_setting_form_dict = array_of_v_mware_dvs_port_setting.from_dict(array_of_v_mware_dvs_port_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


