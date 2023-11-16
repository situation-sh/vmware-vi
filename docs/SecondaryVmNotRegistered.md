# SecondaryVmNotRegistered

This fault is thrown when an attempt is made to unregister a secondary virtual machine from a primary virtual machine with whom it has not been previously registered.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_uuid** | **str** | Instance UUID of the secondary virtual machine.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.secondary_vm_not_registered import SecondaryVmNotRegistered

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryVmNotRegistered from a JSON string
secondary_vm_not_registered_instance = SecondaryVmNotRegistered.from_json(json)
# print the JSON string representation of the object
print SecondaryVmNotRegistered.to_json()

# convert the object into a dict
secondary_vm_not_registered_dict = secondary_vm_not_registered_instance.to_dict()
# create an instance of SecondaryVmNotRegistered from a dict
secondary_vm_not_registered_form_dict = secondary_vm_not_registered.from_dict(secondary_vm_not_registered_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


