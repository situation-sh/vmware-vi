# VirtualMachineProfileRawData

The extensible data object type encapsulates additional data specific to Virtual Machine and its devices.  This data is provided by vSphere Extensions which are integral part of vSphere.  The data is not persisted in Virtual Machine configuration file but is stored and managed by extensions.  Storage Profile Based Management (SPBM) will be one of the consumers of this data structure. SPBM will provide detailed information about Virtual Machine storage requirements.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | vSphere Extension Identifier  ***Since:*** vSphere API 5.5  | 
**object_data** | **str** | Extension-specific additional data to be associated with Virtual machine and its devices.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_profile_raw_data import VirtualMachineProfileRawData

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineProfileRawData from a JSON string
virtual_machine_profile_raw_data_instance = VirtualMachineProfileRawData.from_json(json)
# print the JSON string representation of the object
print VirtualMachineProfileRawData.to_json()

# convert the object into a dict
virtual_machine_profile_raw_data_dict = virtual_machine_profile_raw_data_instance.to_dict()
# create an instance of VirtualMachineProfileRawData from a dict
virtual_machine_profile_raw_data_form_dict = virtual_machine_profile_raw_data.from_dict(virtual_machine_profile_raw_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


