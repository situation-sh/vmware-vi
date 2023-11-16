# NicSettingMismatch

The number of network adapter settings in the customization specification does not match the number of network adapters present in the virtual machine.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_nics_in_spec** | **int** | The number of network adapter settings specified in the customization specification.  ***Since:*** VI API 2.5  | 
**number_of_nics_in_vm** | **int** | The number of network adapters present in the virtual machine.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.nic_setting_mismatch import NicSettingMismatch

# TODO update the JSON string below
json = "{}"
# create an instance of NicSettingMismatch from a JSON string
nic_setting_mismatch_instance = NicSettingMismatch.from_json(json)
# print the JSON string representation of the object
print NicSettingMismatch.to_json()

# convert the object into a dict
nic_setting_mismatch_dict = nic_setting_mismatch_instance.to_dict()
# create an instance of NicSettingMismatch from a dict
nic_setting_mismatch_form_dict = nic_setting_mismatch.from_dict(nic_setting_mismatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


