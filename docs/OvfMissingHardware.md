# OvfMissingHardware

The OVF descriptor does not have a description of a required hardware element e.g CPU, Memory  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the missing hardware.  ***Since:*** vSphere API 4.0  | 
**resource_type** | **int** | OVF rasd resource type of the missing hardware.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_missing_hardware import OvfMissingHardware

# TODO update the JSON string below
json = "{}"
# create an instance of OvfMissingHardware from a JSON string
ovf_missing_hardware_instance = OvfMissingHardware.from_json(json)
# print the JSON string representation of the object
print OvfMissingHardware.to_json()

# convert the object into a dict
ovf_missing_hardware_dict = ovf_missing_hardware_instance.to_dict()
# create an instance of OvfMissingHardware from a dict
ovf_missing_hardware_form_dict = ovf_missing_hardware.from_dict(ovf_missing_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


