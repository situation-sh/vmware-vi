# SecondaryVmAlreadyEnabled

This fault is thrown when an attempt is made to enable a secondary virtual machine that has already been enabled.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_uuid** | **str** | Instance UUID of the secondary virtual machine.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.secondary_vm_already_enabled import SecondaryVmAlreadyEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryVmAlreadyEnabled from a JSON string
secondary_vm_already_enabled_instance = SecondaryVmAlreadyEnabled.from_json(json)
# print the JSON string representation of the object
print SecondaryVmAlreadyEnabled.to_json()

# convert the object into a dict
secondary_vm_already_enabled_dict = secondary_vm_already_enabled_instance.to_dict()
# create an instance of SecondaryVmAlreadyEnabled from a dict
secondary_vm_already_enabled_form_dict = secondary_vm_already_enabled.from_dict(secondary_vm_already_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


