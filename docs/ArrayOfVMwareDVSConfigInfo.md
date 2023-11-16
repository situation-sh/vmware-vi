# ArrayOfVMwareDVSConfigInfo

A boxed array of *VMwareDVSConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VMwareDVSConfigInfo]**](VMwareDVSConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_mware_dvs_config_info import ArrayOfVMwareDVSConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVMwareDVSConfigInfo from a JSON string
array_of_v_mware_dvs_config_info_instance = ArrayOfVMwareDVSConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVMwareDVSConfigInfo.to_json()

# convert the object into a dict
array_of_v_mware_dvs_config_info_dict = array_of_v_mware_dvs_config_info_instance.to_dict()
# create an instance of ArrayOfVMwareDVSConfigInfo from a dict
array_of_v_mware_dvs_config_info_form_dict = array_of_v_mware_dvs_config_info.from_dict(array_of_v_mware_dvs_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


