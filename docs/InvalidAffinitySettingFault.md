# InvalidAffinitySettingFault

An InvalidAffinitySettingsFault is thrown if an invalid affinity setting is specified for a virtual machine.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_affinity_setting_fault import InvalidAffinitySettingFault

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidAffinitySettingFault from a JSON string
invalid_affinity_setting_fault_instance = InvalidAffinitySettingFault.from_json(json)
# print the JSON string representation of the object
print InvalidAffinitySettingFault.to_json()

# convert the object into a dict
invalid_affinity_setting_fault_dict = invalid_affinity_setting_fault_instance.to_dict()
# create an instance of InvalidAffinitySettingFault from a dict
invalid_affinity_setting_fault_form_dict = invalid_affinity_setting_fault.from_dict(invalid_affinity_setting_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


